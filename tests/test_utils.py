"""Tests for the utils module."""

import base64
import datetime as dt
import enum
from decimal import Decimal
from typing import Annotated, Any, Union

import httpx
import msgspec
import pytest

from coinapi.utils import utils


class TestSecurityClient:
    """Tests for SecurityClient."""

    def test_init(self) -> None:
        """Test initialization of SecurityClient."""
        client = utils.SecurityClient()
        assert client.client is None
        assert client.timeout == 60
        assert isinstance(client.limits, httpx.Limits)

    def test_send_with_client(self) -> None:
        """Test send method with a client."""
        mock_client = httpx.Client()
        client = utils.SecurityClient(client=mock_client)
        request = httpx.Request("GET", "https://example.com")
        response = client.send(request)
        assert isinstance(response, httpx.Response)

    def test_send_without_client(self) -> None:
        """Test send method without a client."""
        client = utils.SecurityClient()
        request = httpx.Request("GET", "https://example.com")
        response = client.send(request)
        assert isinstance(response, httpx.Response)

    def test_parse_security_scheme_value_api_key_header(self) -> None:
        """Test parsing security scheme value for API key in header."""
        client = utils.SecurityClient()
        scheme_metadata = {"type": "apiKey", "sub_type": "header"}
        security_metadata = {"field_name": "X-API-Key"}

        utils._parse_security_scheme_value(
            client,
            scheme_metadata,
            security_metadata,
            "test_api_key",
        )

        assert client.headers["X-API-Key"] == "test_api_key"

    def test_parse_security_scheme_value_oauth2(self) -> None:
        """Test parsing security scheme value for OAuth2."""
        client = utils.SecurityClient()
        scheme_metadata = {"type": "oauth2", "sub_type": "other"}
        security_metadata = {"field_name": "Authorization"}
        utils._parse_security_scheme_value(
            client,
            scheme_metadata,
            security_metadata,
            "test_token",
        )
        assert client.headers["Authorization"] == "Bearer test_token"

    def test_parse_security_scheme_value_open_id_connect(self) -> None:
        """Test parsing security scheme value for OpenID Connect."""
        client = utils.SecurityClient()
        scheme_metadata = {"type": "openIdConnect"}
        security_metadata = {"field_name": "Authorization"}
        utils._parse_security_scheme_value(
            client,
            scheme_metadata,
            security_metadata,
            "test_token",
        )
        assert client.headers["Authorization"] == "Bearer test_token"

    def test_parse_security_scheme_value_api_key_query(self) -> None:
        """Test parsing security scheme value for API key in query."""
        client = utils.SecurityClient()
        scheme_metadata = {"type": "apiKey", "sub_type": "query"}
        security_metadata = {"field_name": "api_key"}
        utils._parse_security_scheme_value(
            client,
            scheme_metadata,
            security_metadata,
            "test_key",
        )
        assert client.query_params["api_key"] == "test_key"

    def test_parse_security_scheme_value_unsupported(self) -> None:
        """Test parsing security scheme value for unsupported type."""
        client = utils.SecurityClient()
        scheme_metadata = {"type": "unsupported"}
        security_metadata = {"field_name": "test"}
        with pytest.raises(ValueError, match="not supported"):
            utils._parse_security_scheme_value(
                client,
                scheme_metadata,
                security_metadata,
                "test",
            )


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_apply_bearer(self) -> None:
        """Test applying bearer token."""
        assert utils._apply_bearer("test_token") == "Bearer test_token"
        assert utils._apply_bearer("Bearer test_token") == "Bearer test_token"

    def test_get_metadata(self) -> None:
        """Test getting metadata from a field."""

        class TestStruct(msgspec.Struct):
            field: Annotated[str, msgspec.Meta(extra={"test": "metadata"})]

        field_info = msgspec.structs.fields(TestStruct)[0]
        metadata = utils.get_metadata(field_info)
        assert metadata == {"test": "metadata"}


class TestConfigureSecurityClient:
    """Tests for configure_security_client."""

    def test_configure_security_client_no_security(self) -> None:
        """Test configuring security client with no security."""
        client = utils.configure_security_client(None, None)
        assert isinstance(client, utils.SecurityClient)
        assert client.headers == {}
        assert client.query_params == {}

    def test_configure_security_client_with_api_key(self) -> None:
        """Test configuring security client with API key."""

        class Security(msgspec.Struct):
            api_key: Annotated[
                str,
                msgspec.Meta(
                    extra={
                        "security": {
                            "scheme": True,
                            "type": "apiKey",
                            "sub_type": "header",
                            "field_name": "X-API-Key",
                        },
                    },
                ),
            ]
            field_with_no_meta: str = "test"
            none_field: str | None = None

        security = Security(api_key="test_key")
        client = utils.configure_security_client(None, security)
        assert client.headers == {"X-API-Key": "test_key"}

    def test_configure_security_client_with_basic_auth(self) -> None:
        """Test configuring security client with basic auth."""

        class Security(msgspec.Struct):
            username: Annotated[
                str,
                msgspec.Meta(
                    extra={
                        "security": {
                            "scheme": True,
                            "type": "http",
                            "sub_type": "basic",
                            "field_name": "username",
                        },
                    },
                ),
            ]
            password: Annotated[
                str,
                msgspec.Meta(
                    extra={
                        "security": {
                            "scheme": True,
                            "type": "http",
                            "sub_type": "basic",
                            "field_name": "password",
                        },
                    },
                ),
            ]

        security = Security(username="user", password="pass")  # noqa: S106
        client = utils.configure_security_client(None, security)
        expected_auth = base64.b64encode(b"user:pass").decode()
        assert client.headers == {"Authorization": f"Basic {expected_auth}"}

    def test_configure_security_client_with_bearer_token(self) -> None:
        """Test configuring security client with bearer token."""

        class Security(msgspec.Struct):
            bearer_token: Annotated[
                str,
                msgspec.Meta(
                    extra={
                        "security": {
                            "scheme": True,
                            "type": "http",
                            "sub_type": "bearer",
                            "field_name": "Authorization",
                        },
                    },
                ),
            ]

        security = Security(bearer_token="test_token")  # noqa: S106
        client = utils.configure_security_client(None, security)
        assert client.headers == {"Authorization": "Bearer test_token"}

    def test_configure_security_client_with_option(self) -> None:
        """Test configuring security client with security option."""

        class SecurityOption(msgspec.Struct):
            api_key: Annotated[
                str,
                msgspec.Meta(
                    extra={
                        "security": {
                            "scheme": True,
                            "type": "apiKey",
                            "sub_type": "header",
                            "field_name": "X-API-Key",
                        },
                    },
                ),
            ]
            other_field: str = "test"

        class Security(msgspec.Struct):
            option: Annotated[
                SecurityOption,
                msgspec.Meta(
                    extra={
                        "security": {
                            "option": True,
                        },
                    },
                ),
            ]

        security = Security(option=SecurityOption(api_key="test_option_key"))
        client = utils.configure_security_client(None, security)
        assert client.headers == {"X-API-Key": "test_option_key"}


class TestPathParamHandlers:
    """Tests for path param handlers."""

    def test_list_param_handler(self) -> None:
        """Test ListParamHandler."""
        handler = utils.ListParamHandler()
        result = handler.handle([1, "two", 3.0], {})
        assert result == "1,two,3.0"

    def test_dict_param_handler(self) -> None:
        """Test DictParamHandler."""
        handler = utils.DictParamHandler()
        result = handler.handle({"a": 1, "b": "two"}, {"explode": True})
        assert result == "a=1,b=two"

    def test_struct_param_handler(self) -> None:
        """Test StructParamHandler."""

        class TestStruct(msgspec.Struct):
            a: Annotated[
                int,
                msgspec.Meta(extra={"path_param": {"field_name": "a"}}),
            ]
            b: Annotated[
                str,
                msgspec.Meta(extra={"path_param": {"field_name": "b"}}),
            ]

        handler = utils.StructParamHandler()
        result = handler.handle(TestStruct(a=1, b="two"), {"explode": True})
        assert result == "a=1,b=two"

    def test_default_param_handler(self) -> None:
        """Test DefaultParamHandler."""
        handler = utils.DefaultParamHandler()
        result = handler.handle(42, {})
        assert result == "42"


class TestHandleSinglePathParam:
    """Tests for handle_single_path_param."""

    def test_handle_single_path_param_list(self) -> None:
        """Test handling single path param for list."""
        result = utils.handle_single_path_param([1, 2, 3], {})
        assert result == "1,2,3"

    def test_handle_single_path_param_dict(self) -> None:
        """Test handling single path param for dict."""
        result = utils.handle_single_path_param({"a": 1, "b": 2}, {"explode": True})
        assert result == "a=1,b=2"

    def test_handle_single_path_param_struct(self) -> None:
        """Test handling single path param for struct."""

        class TestStruct(msgspec.Struct):
            a: Annotated[
                int,
                msgspec.Meta(extra={"path_param": {"field_name": "a"}}),
            ]
            b: Annotated[
                str,
                msgspec.Meta(extra={"path_param": {"field_name": "b"}}),
            ]

        result = utils.handle_single_path_param(
            TestStruct(a=1, b="two"),
            {"explode": True},
        )
        assert result == "a=1,b=two"

    def test_handle_single_path_param_default(self) -> None:
        """Test handling single path param for default case."""
        result = utils.handle_single_path_param(42, {})
        assert result == "42"


class TestSerializeParam:
    """Tests for serialize_param."""

    def test_serialize_param_json(self) -> None:
        """Test serializing param to JSON."""

        class TestStruct(msgspec.Struct):
            a: int
            b: str

        result = utils.serialize_param(
            TestStruct(a=1, b="two"),
            {"serialization": "json", "field_name": "test"},
            TestStruct,
            "test",
        )
        assert result == {"test": '{"a":1,"b":"two"}'}

    def test_serialize_param_non_json(self) -> None:
        """Test serializing param for non-JSON case."""
        result = utils.serialize_param(42, {}, int, "test")
        assert result == {}

    def test_serialize_param_unsupported(self) -> None:
        """Test serializing param with unsupported serialization."""
        result = utils.serialize_param(
            "test",
            {"serialization": "unsupported"},
            str,
            "test",
        )
        assert result == {}


class TestReplaceUrlPlaceholder:
    """Tests for replace_url_placeholder."""

    def test_replace_url_placeholder(self) -> None:
        """Test replacing URL placeholder."""
        path = "/api/{version}/users/{id}"
        result = utils.replace_url_placeholder(path, "version", "v1")
        assert result == "/api/v1/users/{id}"


class TestIsPathParam:
    """Tests for is_path_param."""

    def test_is_path_param_true(self) -> None:
        """Test is_path_param for true case."""

        class TestStruct(msgspec.Struct):
            param: Annotated[str, msgspec.Meta(extra={"path_param": {}})]

        field = msgspec.structs.fields(TestStruct)[0]
        assert utils.is_path_param(field) is True

    def test_is_path_param_false(self) -> None:
        """Test is_path_param for false case."""

        class TestStruct(msgspec.Struct):
            param: str

        field = msgspec.structs.fields(TestStruct)[0]
        assert utils.is_path_param(field) is False


class TestGetParamValue:
    """Tests for get_param_value."""

    def test_get_param_value_from_path_params(self) -> None:
        """Test getting param value from path params."""

        class PathParams(msgspec.Struct):
            param: str

        field = msgspec.structs.fields(PathParams)[0]
        path_params = PathParams(param="value")
        result = utils.get_param_value(field, path_params, None)
        assert result == "value"

    def test_get_param_value_from_globals(self) -> None:
        """Test getting param value from globals."""

        class PathParams(msgspec.Struct):
            param: str

        field = msgspec.structs.fields(PathParams)[0]
        gbls = {"parameters": {"pathParam": {"param": "global_value"}}}
        result = utils.get_param_value(field, None, gbls)
        assert result == "global_value"

    def test_get_param_value_from_globals_none(self) -> None:
        """Test getting param value from globals when it's None."""

        class PathParams(msgspec.Struct):
            param: str

        field = msgspec.structs.fields(PathParams)[0]
        gbls = {"parameters": {"pathParam": {"param": None}}}
        result = utils.get_param_value(field, None, gbls)
        assert result is None


class TestGenerateUrl:
    """Tests for generate_url."""

    def test_generate_url(self) -> None:
        """Test generating URL."""

        class PathParams(msgspec.Struct):
            version: Annotated[
                str,
                msgspec.Meta(
                    extra={"path_param": {"field_name": "version"}},
                ),
            ]
            id: Annotated[
                int,
                msgspec.Meta(extra={"path_param": {"field_name": "id"}}),
            ]

        path_params = PathParams(version="v1", id=123)
        result = utils.generate_url(
            PathParams,
            "https://api.example.com",
            "/api/{version}/users/{id}",
            path_params,
        )
        assert result == "https://api.example.com/api/v1/users/123"


class TestIsOptional:
    """Tests for is_optional."""

    def test_is_optional_true(self) -> None:
        """Test is_optional for true case."""
        # TODO: this only works with `Union` which is not how optionals are
        # used, fix
        assert utils.is_optional(Union[str, None]) is True  # type: ignore[arg-type]  # noqa: UP007

    def test_is_optional_false(self) -> None:
        """Test is_optional for false case."""
        assert utils.is_optional(str) is False


class TestTemplateUrl:
    """Tests for template_url."""

    def test_template_url(self) -> None:
        """Test templating URL."""
        url = "https://api.example.com/{version}/users/{id}"
        params = {"version": "v1", "id": "123"}
        result = utils.template_url(url, params)
        assert result == "https://api.example.com/v1/users/123"

    def test_init(self) -> None:
        """Test initialization of SecurityClient."""
        client = utils.SecurityClient()
        assert client.client is None
        assert client.timeout == 60
        assert isinstance(client.limits, httpx.Limits)

    def test_send_with_client(self) -> None:
        """Test send method with a client."""
        mock_client = httpx.Client()
        client = utils.SecurityClient(client=mock_client)
        request = httpx.Request("GET", "https://example.com")
        response = client.send(request)
        assert isinstance(response, httpx.Response)

    def test_send_without_client(self) -> None:
        """Test send method without a client."""
        client = utils.SecurityClient()
        request = httpx.Request("GET", "https://example.com")
        response = client.send(request)
        assert isinstance(response, httpx.Response)


class TestProcessQueryParam:
    """Tests for process_query_param."""

    def test_process_query_param_form(self) -> None:
        """Test processing query param with form style."""

        class QueryParams(msgspec.Struct):
            param: Annotated[
                list[str],
                msgspec.Meta(
                    extra={"query_param": {"style": "form", "explode": True}},
                ),
            ]

        field = msgspec.structs.fields(QueryParams)[0]
        result = utils.process_query_param(field, ["a", "b", "c"], None)
        assert result == {"param": ["a", "b", "c"]}

    def test_process_query_param_deep_object(self) -> None:
        """Test processing query param with deepObject style."""

        class QueryParams(msgspec.Struct):
            param: Annotated[
                dict[str, int],
                msgspec.Meta(
                    extra={"query_param": {"style": "deepObject", "explode": True}},
                ),
            ]

        field = msgspec.structs.fields(QueryParams)[0]
        result = utils.process_query_param(field, {"x": 1, "y": 2}, None)
        assert result == {"param[x]": ["1"], "param[y]": ["2"]}

    def test_process_query_param_serialization(self) -> None:
        """Test processing query param with serialization."""

        class QueryParams(msgspec.Struct):
            param: Annotated[
                dict[str, Any],
                msgspec.Meta(extra={"query_param": {"serialization": "json"}}),
            ]

        field = msgspec.structs.fields(QueryParams)[0]
        result = utils.process_query_param(field, {"key": "value"}, None)
        assert result == {"param": ['{"key":"value"}']}

    def test_populate_form_struct(self) -> None:
        """Test populating form for Struct."""

        class TestStruct(msgspec.Struct):
            field1: Annotated[
                str,
                msgspec.Meta(extra={"query_param": {"field_name": "f1"}}),
            ]
            field2: Annotated[
                int,
                msgspec.Meta(extra={"query_param": {"field_name": "f2"}}),
            ]

        obj = TestStruct(field1="test", field2=42)
        result = utils._populate_form(
            "test_field",
            obj,
            utils._get_query_param_field_name,
            ",",
            explode=True,
        )

        assert result == {"f1": ["test"], "f2": ["42"]}

    def test_process_query_param_pipe_delimited(self) -> None:
        """Test processing query param with pipeDelimited style."""

        class QueryParams(msgspec.Struct):
            param: Annotated[
                list[str],
                msgspec.Meta(
                    extra={"query_param": {"style": "pipeDelimited", "explode": False}},
                ),
            ]

        field = msgspec.structs.fields(QueryParams)[0]
        result = utils.process_query_param(field, ["a", "b", "c"], None)
        assert result == {"param": ["a|b|c"]}


class TestGetQueryParams:
    """Tests for get_query_params."""

    def test_get_query_params(self) -> None:
        """Test getting query parameters."""

        class QueryParams(msgspec.Struct):
            param1: Annotated[
                str,
                msgspec.Meta(extra={"query_param": {"field_name": "p1"}}),
            ]
            param2: Annotated[
                int,
                msgspec.Meta(extra={"query_param": {"field_name": "p2"}}),
            ]

        query_params = QueryParams(param1="value1", param2=42)
        result = utils.get_query_params(QueryParams, query_params)
        assert result == {"p1": ["value1"], "p2": ["42"]}


class TestGetHeaders:
    """Tests for get_headers."""

    def test_get_headers(self) -> None:
        """Test getting headers."""

        class Headers(msgspec.Struct):
            header1: Annotated[
                str,
                msgspec.Meta(extra={"header": {"field_name": "X-Header-1"}}),
            ]
            header2: Annotated[
                int,
                msgspec.Meta(extra={"header": {"field_name": "X-Header-2"}}),
            ]

        headers = Headers(header1="value1", header2=42)
        result = utils.get_headers(headers)
        assert result == {"X-Header-1": "value1", "X-Header-2": "42"}

    def test_serialize_header_struct(self) -> None:
        """Test serializing header for Struct."""

        class TestStruct(msgspec.Struct):
            field1: Annotated[
                str,
                msgspec.Meta(extra={"header": {"field_name": "X-Field-1"}}),
            ]
            field2: Annotated[
                int,
                msgspec.Meta(extra={"header": {"field_name": "X-Field-2"}}),
            ]

        obj = TestStruct(field1="test", field2=42)
        result = utils._serialize_header(obj, explode=True)

        assert result == "X-Field-1=test,X-Field-2=42"


class TestSerializeRequestBody:
    """Tests for serialize_request_body."""

    def test_serialize_request_body_json(self) -> None:
        """Test serializing request body to JSON."""

        class RequestBody(msgspec.Struct):
            data: Annotated[
                dict[str, Any],
                msgspec.Meta(
                    extra={"request": {"media_type": "application/json"}},
                ),
            ]

        request = RequestBody(data={"key": "value"})
        result = utils.serialize_request_body(request, "data")
        assert result == ("application/json", '{"key":"value"}', None)

    def test_serialize_request_body_optional(self) -> None:
        """Test serializing request body with optional field."""

        class RequestBody(msgspec.Struct):
            data: Annotated[
                dict[str, Any] | None,
                msgspec.Meta(extra={"request": {"media_type": "application/json"}}),
            ]

        request = RequestBody(data=None)
        result = utils.serialize_request_body(request, "data")
        assert result == (None, None, None)


class TestSerializeContentType:
    """Tests for serialize_content_type."""

    def test_serialize_content_type_json(self) -> None:
        """Test serializing content type to JSON."""
        result = utils.serialize_content_type(
            "data",
            dict,
            "application/json",
            {"key": "value"},  # type: ignore[arg-type]
        )
        assert result == ("application/json", '{"key":"value"}', None)

    def test_serialize_content_type_form(self) -> None:
        """Test serializing content type to form data."""
        result = utils.serialize_content_type(
            "data",
            dict,
            "application/x-www-form-urlencoded",
            {"key": "value"},  # type: ignore[arg-type]
        )
        assert result == ("application/x-www-form-urlencoded", {"key": ["value"]}, None)

    def test_serialize_content_type_multipart(self) -> None:
        """Test serializing content type to multipart form data."""

        class MultipartData(msgspec.Struct):
            file: Annotated[
                File,
                msgspec.Meta(
                    extra={
                        "multipart_form": {
                            "file": True,
                            "content": True,
                            "field_name": "file",
                        },
                    },
                ),
            ]

        data = MultipartData(file=File(filename="test.txt", content=b"content"))
        result = utils.serialize_content_type(
            "data",
            MultipartData,
            "multipart/form-data",
            data,
        )
        assert result[0] == "multipart/form-data"
        assert isinstance(result[2], list)
        assert len(result[2]) == 1
        assert result[2][0][0] == "file"
        assert result[2][0][1][0] == "test.txt"
        assert result[2][0][1][1] == b"content"

    def test_serialize_content_type_invalid(self) -> None:
        """Test serializing content type with invalid media type."""
        with pytest.raises(ValueError, match="invalid request body type"):
            utils.serialize_content_type(
                "field",
                dict,
                "invalid/media-type",
                {"key": "value"},  # type: ignore[arg-type]
            )


class TestSerializeFormData:
    """Tests for serialize_form_data."""

    def test_serialize_form_data_struct(self) -> None:
        """Test serializing form data for Struct."""

        class FormData(msgspec.Struct):
            field1: Annotated[
                str,
                msgspec.Meta(extra={"form": {"field_name": "f1"}}),
            ]
            field2: Annotated[
                int,
                msgspec.Meta(extra={"form": {"field_name": "f2"}}),
            ]

        form_data = FormData(field1="value1", field2=42)
        result = utils.serialize_form_data("data", form_data)
        assert result == {"f1": ["value1"], "f2": ["42"]}

    def test_serialize_form_data_dict(self) -> None:
        """Test serializing form data for dict."""
        result = utils.serialize_form_data("data", {"key1": "value1", "key2": 42})
        assert result == {"key1": ["value1"], "key2": ["42"]}


class TestMarshalJson:
    """Tests for marshal_json."""

    def test_marshal_json(self) -> None:
        """Test marshalling JSON."""

        class TestStruct(msgspec.Struct):
            field1: str
            field2: int

        data = TestStruct(field1="value", field2=42)
        result = utils.marshal_json(data, TestStruct)
        assert result == '{"field1":"value","field2":42}'


class TestMatchContentType:
    """Tests for match_content_type."""

    def test_match_content_type_exact(self) -> None:
        """Test matching content type exactly."""
        assert utils.match_content_type("application/json", "application/json") is True

    def test_match_content_type_wildcard(self) -> None:
        """Test matching content type with wildcard."""
        assert utils.match_content_type("application/json", "*/*") is True

    def test_match_content_type_partial(self) -> None:
        """Test matching content type partially."""
        assert utils.match_content_type("application/json", "application/*") is True


class TestMatchStatusCodes:
    """Tests for match_status_codes."""

    def test_match_status_codes_exact(self) -> None:
        """Test matching status codes exactly."""
        assert utils.match_status_codes(["200", "201"], 200) is True

    def test_match_status_codes_range(self) -> None:
        """Test matching status codes with range."""
        assert utils.match_status_codes(["2XX"], 201) is True

    def test_match_status_codes_no_match(self) -> None:
        """Test matching status codes with no match."""
        assert utils.match_status_codes(["200", "201"], 404) is False


class TestValToString:
    """Tests for _val_to_string."""

    def test_val_to_string_bool(self) -> None:
        """Test converting bool to string."""
        assert utils._val_to_string(True) == "true"  # noqa: FBT003
        assert utils._val_to_string(False) == "false"  # noqa: FBT003

    def test_val_to_string_datetime(self) -> None:
        """Test converting datetime to string."""
        dt_val = dt.datetime(2023, 1, 1, 12, 0, 0, tzinfo=dt.timezone.utc)
        assert utils._val_to_string(dt_val) == "2023-01-01T12:00:00Z"

    def test_val_to_string_enum(self) -> None:
        """Test converting Enum to string."""

        class TestEnum(enum.Enum):
            VALUE = "test_value"

        assert utils._val_to_string(TestEnum.VALUE) == "test_value"

    def test_val_to_string_other(self) -> None:
        """Test converting other types to string."""
        assert utils._val_to_string(42) == "42"
        assert utils._val_to_string("test") == "test"
        assert utils._val_to_string(Decimal("3.14")) == "3.14"


class TestRemoveSuffix:
    """Tests for remove_suffix."""

    def test_remove_suffix_present(self) -> None:
        """Test removing suffix when present."""
        assert utils.remove_suffix("test_string_suffix", "_suffix") == "test_string"

    def test_remove_suffix_not_present(self) -> None:
        """Test removing suffix when not present."""
        assert utils.remove_suffix("test_string", "_suffix") == "test_string"

    def test_remove_suffix_empty(self) -> None:
        """Test removing empty suffix."""
        assert utils.remove_suffix("test_string", "") == "test_string"


class TestSecurityClientSend:
    """Tests for SecurityClient.send."""

    def test_send_with_query_params_and_headers(self) -> None:
        """Test sending request with query parameters and headers."""
        client = utils.SecurityClient(
            query_params={"key": "value"},
            headers={"X-Test": "test"},
        )
        request = httpx.Request("GET", "https://example.com")
        response = client.send(request)
        assert "key=value" in str(response.request.url)
        assert response.request.headers["X-Test"] == "test"


class TestGetQueryParamHandler:
    """Tests for get_query_param_handler."""

    def test_get_query_param_handler_form(self) -> None:
        """Test getting query param handler for form."""
        handler = utils.get_query_param_handler("form")
        assert isinstance(handler, utils.FormQueryParamHandler)

    def test_get_query_param_handler_deep_object(self) -> None:
        """Test getting query param handler for deep object."""
        handler = utils.get_query_param_handler("deepObject")
        assert isinstance(handler, utils.DeepObjectQueryParamHandler)

    def test_get_query_param_handler_pipe_delimited(self) -> None:
        """Test getting query param handler for pipe delimited."""
        handler = utils.get_query_param_handler("pipeDelimited")
        assert isinstance(handler, utils.PipeDelimitedQueryParamHandler)


class File(msgspec.Struct):
    """File struct for testing serialize_multipart_form."""

    filename: Annotated[
        str,
        msgspec.Meta(extra={"multipart_form": {"field_name": "filename"}}),
    ]
    content: Annotated[
        bytes,
        msgspec.Meta(
            extra={
                "multipart_form": {"field_name": "content", "content": True},
            },
        ),
    ]


class TestSerializeMultipartForm:
    """Tests for serialize_multipart_form."""

    def test_serialize_multipart_form(self) -> None:
        """Test serializing multipart form data."""

        class MultipartRequest(msgspec.Struct):
            file: Annotated[
                File,
                msgspec.Meta(extra={"multipart_form": {"file": True}}),
            ]

        request = MultipartRequest(
            file=File(filename="test.txt", content=b"file content"),
        )

        media_type, _, form = utils.serialize_multipart_form(
            "multipart/form-data",
            request,
        )
        assert media_type == "multipart/form-data"
        assert len(form) == 1
        assert form[0][0] == "file"
        assert form[0][1][0] == "test.txt"
        assert form[0][1][1] == b"file content"

    def test_serialize_multipart_form_with_multiple_fields(self) -> None:
        """Test serializing multipart form data with multiple fields."""

        class TestRequest(msgspec.Struct):
            file_field: Annotated[
                File,
                msgspec.Meta(extra={"multipart_form": {"file": True}}),
            ]
            json_field: Annotated[
                dict[str, Any],
                msgspec.Meta(extra={"multipart_form": {"json": True}}),
            ]
            regular_field: Annotated[
                str,
                msgspec.Meta(extra={"multipart_form": {"content": True}}),
            ]

        request = TestRequest(
            file_field=File(filename="test.txt", content=b"test content"),
            json_field={"key": "value"},
            regular_field="test",
        )

        media_type, _, form = utils.serialize_multipart_form(
            "multipart/form-data",
            request,
        )

        assert media_type == "multipart/form-data"
        assert len(form) == 3
        assert any(item[0] == "file_field" for item in form)
        assert any(item[0] == "json_field" for item in form)
        assert any(item[0] == "regular_field" for item in form)

    def test_serialize_multipart_form_invalid_file(self) -> None:
        """Test serializing multipart form with invalid file."""

        class InvalidFile(msgspec.Struct):
            invalid: str

        class MultipartRequest(msgspec.Struct):
            file: Annotated[
                InvalidFile,
                msgspec.Meta(extra={"multipart_form": {"file": True}}),
            ]

        request = MultipartRequest(file=InvalidFile(invalid="test"))

        with pytest.raises(ValueError, match="Invalid multipart/form-data file"):
            utils.serialize_multipart_form("multipart/form-data", request)


class TestMultipartFormSerializer:
    """Tests for MultipartFormSerializer."""

    def test_serialize_file_field(self) -> None:
        """Test serializing file field."""
        serializer = utils.MultipartFormSerializer()
        field = utils.MultipartFormField(
            name="file",
            value=File(filename="test.txt", content=b"file content"),
            metadata={"file": True},
        )
        result = serializer._get_serializer(field).serialize(field)
        assert result == [["file", ["test.txt", b"file content"]]]

    def test_serialize_json_field(self) -> None:
        """Test serializing JSON field."""
        serializer = utils.MultipartFormSerializer()
        field = utils.MultipartFormField(
            name="json_data",
            value={"key": "value"},
            metadata={"json": True},
        )
        result = serializer._get_serializer(field).serialize(field)
        assert result == [["json_data", [None, '{"key":"value"}', "application/json"]]]

    def test_serialize_regular_field(self) -> None:
        """Test serializing regular field."""
        serializer = utils.MultipartFormSerializer()
        field = utils.MultipartFormField(name="text", value="content", metadata={})
        result = serializer._get_serializer(field).serialize(field)
        assert result == [["text", [None, "content"]]]

"""Tests for the utils module."""

import base64
import datetime as dt
import enum
from decimal import Decimal
from typing import Annotated, Any, Union

import httpx
import msgspec

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

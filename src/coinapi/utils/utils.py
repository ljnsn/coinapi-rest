"""Utilities."""

import base64
import datetime as dt
import re
from collections.abc import Callable
from decimal import Decimal
from email.message import Message
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Protocol,
    Union,
    cast,
    get_args,
    get_origin,
)
from xmlrpc.client import boolean

import httpx
import msgspec
from typing_inspect import is_optional_type

NOT_SUPPORTED = "not supported"


class SecurityClient:
    """Client with security settings."""

    client: httpx.Client | None
    query_params: ClassVar[dict[str, str]] = {}
    headers: ClassVar[dict[str, str]] = {}

    def __init__(self, client: httpx.Client | None = None, timeout: int = 60) -> None:
        self.client = client
        self.timeout = timeout
        self.limits = httpx.Limits(max_keepalive_connections=1, max_connections=1)

    def send(
        self,
        request: httpx.Request,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send a request."""
        request.url = request.url.copy_merge_params(self.query_params)
        request.headers.update(self.headers)
        if self.client is not None:
            return self.client.send(request, **kwargs)
        with httpx.Client(timeout=self.timeout, limits=self.limits) as client:
            return client.send(request, **kwargs)


def configure_security_client(
    session: httpx.Client | None,
    security: msgspec.Struct | None,
) -> SecurityClient:
    """Configure a client with security settings."""
    client = SecurityClient(session)

    if security is None:
        return client

    sec_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(security)
    for sec_field in sec_fields:
        value = getattr(security, sec_field.name)
        if value is None:
            continue

        metadata = get_metadata(sec_field).get("security")
        if metadata is None:
            continue
        if metadata.get("option"):
            _parse_security_option(client, value)
            return client
        if metadata.get("scheme"):
            # Special case for basic auth which could be a flattened struct
            if metadata.get("sub_type") == "basic" and not isinstance(
                value,
                msgspec.Struct,
            ):
                _parse_security_scheme(client, metadata, security)
            else:
                _parse_security_scheme(client, metadata, value)

    return client


def _parse_security_option(client: SecurityClient, option: msgspec.Struct) -> None:
    """Parse a security option."""
    opt_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(option)
    for opt_field in opt_fields:
        metadata = get_metadata(opt_field).get("security")
        if metadata is None or metadata.get("scheme") is None:
            continue
        _parse_security_scheme(client, metadata, getattr(option, opt_field.name))


def _parse_security_scheme(
    client: SecurityClient,
    scheme_metadata: dict[str, Any],
    scheme: Any,
) -> None:
    """Parse a security scheme."""
    scheme_type = scheme_metadata.get("type")
    sub_type = scheme_metadata.get("sub_type")

    if isinstance(scheme, msgspec.Struct):
        if scheme_type == "http" and sub_type == "basic":
            _parse_basic_auth_scheme(client, scheme)
            return

        scheme_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
            scheme,
        )
        for scheme_field in scheme_fields:
            metadata = get_metadata(scheme_field).get("security")
            if metadata is None or metadata.get("field_name") is None:
                continue

            value = getattr(scheme, scheme_field.name)

            _parse_security_scheme_value(client, scheme_metadata, metadata, value)
    else:
        _parse_security_scheme_value(client, scheme_metadata, scheme_metadata, scheme)


def _parse_security_scheme_value(
    client: SecurityClient,
    scheme_metadata: dict[str, Any],
    security_metadata: dict[str, Any],
    value: Any,
) -> None:
    """Parse a security scheme value."""
    scheme_type = scheme_metadata.get("type")
    sub_type = scheme_metadata.get("sub_type")

    header_name = security_metadata.get("field_name")

    if header_name is None:
        return

    if scheme_type == "apiKey":
        if sub_type == "header":
            client.headers[header_name] = value
        elif sub_type == "query":
            client.query_params[header_name] = value
        else:
            raise ValueError(NOT_SUPPORTED)
    elif scheme_type == "openIdConnect":
        client.headers[header_name] = _apply_bearer(value)
    elif scheme_type == "oauth2":
        if sub_type != "client_credentials":
            client.headers[header_name] = _apply_bearer(value)
    elif scheme_type == "http":
        if sub_type == "bearer":
            client.headers[header_name] = _apply_bearer(value)
        else:
            raise ValueError(NOT_SUPPORTED)
    else:
        raise ValueError(NOT_SUPPORTED)


def _apply_bearer(token: str) -> str:
    return token.lower().startswith("bearer ") and token or f"Bearer {token}"


def _parse_basic_auth_scheme(client: SecurityClient, scheme: msgspec.Struct) -> None:
    """Parse a basic auth scheme."""
    username = ""
    password = ""

    scheme_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
        scheme,
    )
    for scheme_field in scheme_fields:
        metadata = get_metadata(scheme_field).get("security")
        if metadata is None or metadata.get("field_name") is None:
            continue

        field_name = metadata.get("field_name")
        value = getattr(scheme, scheme_field.name)

        if field_name == "username":
            username = value
        if field_name == "password":
            password = value

    data = f"{username}:{password}".encode()
    client.headers["Authorization"] = f"Basic {base64.b64encode(data).decode()}"


def get_metadata(field_info: msgspec.structs.FieldInfo) -> dict[str, Any]:
    """Get metadata on a field."""
    type_info = msgspec.inspect.type_info(field_info.type)
    if isinstance(type_info, msgspec.inspect.Metadata):
        return type_info.extra or {}
    return {}


class PathParamHandler(Protocol):
    """Protocol for path parameter handlers."""

    def handle(self, param: Any, metadata: dict[str, Any]) -> str:
        """Handle a path parameter."""
        ...


class ListParamHandler:
    """Handler for list parameters."""

    def handle(self, param: list[Any], _metadata: dict[str, Any]) -> str:
        """Handle a list parameter."""
        pp_vals = [_val_to_string(pp_val) for pp_val in param if pp_val is not None]
        return ",".join(pp_vals)


class DictParamHandler:
    """Handler for dictionary parameters."""

    def handle(self, param: dict[str, Any], metadata: dict[str, Any]) -> str:
        """Handle a dictionary parameter."""
        pp_vals = []
        for pp_key, pp_value in param.items():
            if pp_value is None:
                continue
            if metadata.get("explode"):
                pp_vals.append(f"{pp_key}={_val_to_string(pp_value)}")
            else:
                pp_vals.append(f"{pp_key},{_val_to_string(pp_value)}")
        return ",".join(pp_vals)


class StructParamHandler:
    """Handler for msgspec.Struct parameters."""

    def handle(self, param: msgspec.Struct, metadata: dict[str, Any]) -> str:
        """Handle a msgspec.Struct parameter."""
        pp_vals = []
        param_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
            param,
        )
        for param_field in param_fields:
            param_value_metadata = get_metadata(param_field).get("path_param")
            if not param_value_metadata:
                continue

            parm_name = param_value_metadata.get("field_name", param_field.name)
            param_field_val = getattr(param, param_field.name)
            if param_field_val is None:
                continue
            if metadata.get("explode"):
                pp_vals.append(f"{parm_name}={_val_to_string(param_field_val)}")
            else:
                pp_vals.append(f"{parm_name},{_val_to_string(param_field_val)}")
        return ",".join(pp_vals)


class DefaultParamHandler:
    """Handler for default parameter types."""

    def handle(
        self,
        param: str | complex | bool | Decimal,
        _metadata: dict[str, Any],
    ) -> str:
        """Handle a default parameter type."""
        return _val_to_string(param)


def get_param_handler(param: Any) -> PathParamHandler:
    """Get the appropriate parameter handler based on the parameter type."""
    if isinstance(param, list):
        return ListParamHandler()
    if isinstance(param, dict):
        return DictParamHandler()
    if isinstance(param, msgspec.Struct):
        return StructParamHandler()
    return DefaultParamHandler()


def handle_single_path_param(param: Any, metadata: dict[str, Any]) -> str:
    """Handle a single path parameter."""
    handler = get_param_handler(param)
    return handler.handle(param, metadata)


def serialize_param(
    param: Any,
    metadata: dict[str, Any],
    field_type: type[Any],
    field_name: str,
) -> dict[str, str]:
    """Serialize a parameter based on metadata."""
    params: dict[str, str] = {}
    serialization = metadata.get("serialization", "")
    if serialization == "json":
        params[metadata.get("field_name", field_name)] = marshal_json(param, field_type)
    return params


def replace_url_placeholder(path: str, field_name: str, value: str) -> str:
    """Replace a placeholder in the URL path."""
    return path.replace("{" + field_name + "}", value, 1)


def is_path_param(field: msgspec.structs.FieldInfo) -> bool:
    """Check if a field is a path parameter."""
    return get_metadata(field).get("path_param") is not None


def get_param_value(
    field: msgspec.structs.FieldInfo,
    path_params: msgspec.Struct | None,
    gbls: dict[str, dict[str, dict[str, Any]]] | None,
) -> Any:
    """Get the parameter value from path_params or globals."""
    param = getattr(path_params, field.name) if path_params is not None else None
    return _populate_from_globals(field.name, param, "pathParam", gbls)


def generate_url(
    clazz: type[msgspec.Struct],
    server_url: str,
    path: str,
    path_params: msgspec.Struct | None,
    gbls: dict[str, dict[str, dict[str, Any]]] | None = None,
) -> str:
    """Generate a URL."""
    path_param_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
        clazz,
    )
    for field in path_param_fields:
        if not is_path_param(field):
            continue

        param = get_param_value(field, path_params, gbls)
        if param is None:
            continue

        metadata = get_metadata(field).get("path_param", {})
        f_name = metadata.get("field_name", field.name)
        serialization = metadata.get("serialization", "")

        if serialization:
            serialized_params = serialize_param(param, metadata, field.type, f_name)
            for key, value in serialized_params.items():
                path = replace_url_placeholder(path, key, value)
        elif metadata.get("style", "simple") == "simple":
            serialized_value = handle_single_path_param(param, metadata)
            path = replace_url_placeholder(path, f_name, serialized_value)

    return remove_suffix(server_url, "/") + path


def is_optional(field: type[Any]) -> bool:
    """Check if a field is optional."""
    return get_origin(field) is Union and type(None) in get_args(field)


def template_url(url_with_params: str, params: dict[str, str]) -> str:
    """Template a URL with parameters."""
    for key, value in params.items():
        url_with_params = url_with_params.replace("{" + key + "}", value)

    return url_with_params


class QueryParamHandler(Protocol):
    """Protocol for query parameter handlers."""

    def handle(
        self,
        metadata: dict[str, Any],
        field_name: str,
        value: Any,
    ) -> dict[str, list[str]]:
        """Handle query parameter processing."""
        ...


class FormQueryParamHandler:
    """Handler for form style query parameters."""

    def handle(
        self,
        metadata: dict[str, Any],
        field_name: str,
        value: Any,
    ) -> dict[str, list[str]]:
        """Process form style query parameters."""
        return _get_delimited_query_params(metadata, field_name, value, ",")


class DeepObjectQueryParamHandler:
    """Handler for deepObject style query parameters."""

    def handle(
        self,
        metadata: dict[str, Any],
        field_name: str,
        value: Any,
    ) -> dict[str, list[str]]:
        """Process deepObject style query parameters."""
        return _get_deep_object_query_params(metadata, field_name, value)


class PipeDelimitedQueryParamHandler:
    """Handler for pipeDelimited style query parameters."""

    def handle(
        self,
        metadata: dict[str, Any],
        field_name: str,
        value: Any,
    ) -> dict[str, list[str]]:
        """Process pipeDelimited style query parameters."""
        return _get_delimited_query_params(metadata, field_name, value, "|")


def get_query_param_handler(style: str) -> QueryParamHandler:
    """Get the appropriate query parameter handler based on style."""
    handlers = {
        "form": FormQueryParamHandler(),
        "deepObject": DeepObjectQueryParamHandler(),
        "pipeDelimited": PipeDelimitedQueryParamHandler(),
    }
    # Default to form style
    return handlers.get(style, FormQueryParamHandler())  # type: ignore[return-value]


def process_query_param(
    field: msgspec.structs.FieldInfo,
    value: Any,
    _gbls: dict[str, dict[str, dict[str, Any]]] | None,
) -> dict[str, list[str]]:
    """Process a single query parameter."""
    metadata = get_metadata(field).get("query_param", {})
    field_name = metadata.get("field_name", field.name)

    if metadata.get("serialization"):
        serialized_params = _get_serialized_params(
            metadata,
            field.type,
            field_name,
            value,
        )
        return {key: [value] for key, value in serialized_params.items()}

    style = metadata.get("style", "form")
    handler = get_query_param_handler(style)
    return handler.handle(metadata, field_name, value)


def get_query_params(
    clazz: type[msgspec.Struct],
    query_params: msgspec.Struct,
    gbls: dict[str, dict[str, dict[str, Any]]] | None = None,
) -> dict[str, list[str]]:
    """Get query parameters for a request."""
    params: dict[str, list[str]] = {}

    for field in msgspec.structs.fields(clazz):
        if get_metadata(field).get("request") is not None:
            continue

        if not get_metadata(field).get("query_param"):
            continue

        value = getattr(query_params, field.name) if query_params is not None else None
        value = _populate_from_globals(field.name, value, "queryParam", gbls)

        if value is None:
            continue

        params.update(process_query_param(field, value, gbls))

    return params


def get_headers(headers_params: msgspec.Struct | None) -> dict[str, str]:
    """Get headers."""
    if headers_params is None:
        return {}

    headers: dict[str, str] = {}

    param_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
        headers_params,
    )
    for field in param_fields:
        metadata = get_metadata(field).get("header")
        if not metadata:
            continue

        value = _serialize_header(
            metadata.get("explode", False),
            getattr(headers_params, field.name),
        )

        if value != "":
            headers[metadata.get("field_name", field.name)] = value

    return headers


def _get_serialized_params(
    metadata: dict[str, Any],
    field_type: type[msgspec.Struct],
    field_name: str,
    obj: msgspec.Struct,
) -> dict[str, str]:
    """Get serialized parameters."""
    params: dict[str, str] = {}

    serialization = metadata.get("serialization", "")
    if serialization == "json":
        params[metadata.get("field_name", field_name)] = marshal_json(obj, field_type)

    return params


def _get_deep_object_query_params(  # noqa: PLR0912, C901
    metadata: dict[str, Any],
    field_name: str,
    obj: Any,
) -> dict[str, list[str]]:
    """Get deep object query parameters."""
    params: dict[str, list[str]] = {}

    if obj is None:
        return params

    if isinstance(obj, msgspec.Struct):
        obj_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(obj)
        for obj_field in obj_fields:
            obj_param_metadata = get_metadata(obj_field).get("query_param")
            if not obj_param_metadata:
                continue

            obj_val = getattr(obj, obj_field.name)
            if obj_val is None:
                continue

            if isinstance(obj_val, list):
                for val in obj_val:
                    if val is None:
                        continue

                    if (
                        params.get(
                            f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]',
                        )
                        is None
                    ):
                        params[
                            f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'
                        ] = []

                    params[
                        f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'
                    ].append(_val_to_string(val))
            else:
                params[
                    f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'
                ] = [_val_to_string(obj_val)]
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if value is None:
                continue

            if isinstance(value, list):
                for val in value:
                    if val is None:
                        continue

                    if (
                        params.get(f'{metadata.get("field_name", field_name)}[{key}]')
                        is None
                    ):
                        params[f'{metadata.get("field_name", field_name)}[{key}]'] = []

                    params[f'{metadata.get("field_name", field_name)}[{key}]'].append(
                        _val_to_string(val),
                    )
            else:
                params[f'{metadata.get("field_name", field_name)}[{key}]'] = [
                    _val_to_string(value),
                ]
    return params


def _get_query_param_field_name(obj_field: msgspec.structs.FieldInfo) -> str:
    """Get the query param field name."""
    obj_param_metadata = get_metadata(obj_field).get("query_param")

    if not obj_param_metadata:
        return ""

    return cast(str, obj_param_metadata.get("field_name", obj_field.name))


def _get_delimited_query_params(
    metadata: dict[str, Any],
    field_name: str,
    obj: Any,
    delimiter: str,
) -> dict[str, list[str]]:
    """Get delimited query parameters."""
    return _populate_form(
        field_name,
        metadata.get("explode", True),
        obj,
        _get_query_param_field_name,
        delimiter,
    )


SERIALIZATION_METHOD_TO_CONTENT_TYPE = {
    "json": "application/json",
    "form": "application/x-www-form-urlencoded",
    "multipart": "multipart/form-data",
    "raw": "application/octet-stream",
    "string": "text/plain",
}


def serialize_request_body(
    request: msgspec.Struct,
    request_field_name: str,
) -> tuple[str | None, Any, Any]:
    """Serialize the request body."""
    request_val = getattr(request, request_field_name)
    request_type = next(
        field
        for field in msgspec.structs.fields(request)
        if field.name == request_field_name
    ).type

    if request_val is None and is_optional_type(request_type):
        return None, None, None

    request_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(
        request,
    )
    request_metadata = None

    for field in request_fields:
        if field.name == request_field_name:
            request_metadata = get_metadata(field).get("request")
            break

    if request_metadata is None:
        raise ValueError("invalid request type")

    return serialize_content_type(
        request_field_name,
        request_type,
        request_metadata.get("media_type", "application/octet-stream"),
        request_val,
    )


def serialize_content_type(
    field_name: str,
    request_type: Any,
    media_type: str,
    request: msgspec.Struct,
    encoder: Callable[..., Any] | None = None,
) -> tuple[str, Any, list[list[Any]] | None]:
    """Serialize a content type."""
    if re.match(r"(application|text)/.*?\+*json.*", media_type) is not None:
        return media_type, marshal_json(request, request_type, encoder), None
    if re.match(r"multipart/.*", media_type) is not None:
        return serialize_multipart_form(media_type, request)
    if re.match(r"application/x-www-form-urlencoded.*", media_type) is not None:
        return media_type, serialize_form_data(field_name, request), None
    if isinstance(request, bytes | bytearray):
        return media_type, request, None
    if isinstance(request, str):
        return media_type, request, None

    msg = f"invalid request body type {type(request)} for mediaType {media_type}"
    raise ValueError(msg)


def serialize_multipart_form(  # noqa: PLR0912, C901
    media_type: str,
    request: msgspec.Struct,
) -> tuple[str, Any, list[list[Any]]]:
    """Serialize a multipart form."""
    form: list[list[Any]] = []
    request_fields = msgspec.structs.fields(request)

    for field in request_fields:
        val = getattr(request, field.name)
        if val is None:
            continue

        field_metadata = get_metadata(field).get("multipart_form")
        if not field_metadata:
            continue

        if field_metadata.get("file") is True:
            file_fields = msgspec.structs.fields(val)

            file_name = ""
            field_name = ""
            content = b""

            for file_field in file_fields:
                file_metadata = get_metadata(file_field).get("multipart_form")
                if file_metadata is None:
                    continue

                if file_metadata.get("content") is True:
                    content = getattr(val, file_field.name)
                else:
                    field_name = file_metadata.get("field_name", file_field.name)
                    file_name = getattr(val, file_field.name)
            if field_name == "" or file_name == "" or content == b"":
                raise ValueError("invalid multipart/form-data file")

            form.append([field_name, [file_name, content]])
        elif field_metadata.get("json") is True:
            to_append = [
                field_metadata.get("field_name", field.name),
                [None, marshal_json(val, field.type), "application/json"],
            ]
            form.append(to_append)
        else:
            field_name = field_metadata.get("field_name", field.name)
            if isinstance(val, list):
                for value in val:
                    if value is None:
                        continue
                    form.append([field_name + "[]", [None, _val_to_string(value)]])
            else:
                form.append([field_name, [None, _val_to_string(val)]])
    return media_type, None, form


def serialize_dict(
    original: dict[str, Any],
    explode: bool,  # noqa: FBT001
    field_name: str,
    existing: dict[str, list[str]] | None,
) -> dict[str, list[str]]:
    """Serialize a dictionary."""
    if existing is None:
        existing = {}

    if explode is True:
        for key, val in original.items():
            if key not in existing:
                existing[key] = []
            existing[key].append(val)
    else:
        temp = []
        for key, val in original.items():
            temp.append(str(key))
            temp.append(str(val))
        if field_name not in existing:
            existing[field_name] = []
        existing[field_name].append(",".join(temp))
    return existing


def serialize_form_data(field_name: str, data: Any) -> dict[str, Any]:
    """Serialize form data."""
    form: dict[str, list[str]] = {}

    if isinstance(data, msgspec.Struct):
        for field in msgspec.structs.fields(data):
            val = getattr(data, field.name)
            if val is None:
                continue

            metadata = get_metadata(field).get("form")
            if metadata is None:
                continue

            field_name = metadata.get("field_name", field.name)

            if metadata.get("json"):
                form[field_name] = [marshal_json(val, field.type)]
            elif metadata.get("style", "form") == "form":
                form = {
                    **form,
                    **_populate_form(
                        field_name,
                        metadata.get("explode", True),
                        val,
                        _get_form_field_name,
                        ",",
                    ),
                }
            else:
                msg = f"Invalid form style for field {field.name}"
                raise ValueError(msg)
    elif isinstance(data, dict):
        for key, value in data.items():
            form[key] = [_val_to_string(value)]
    else:
        msg = f"Invalid request body type for field {field_name}"
        raise TypeError(msg)

    return form


def _get_form_field_name(obj_field: msgspec.structs.FieldInfo) -> str:
    """Get the form field name."""
    obj_param_metadata = get_metadata(obj_field).get("form")

    if not obj_param_metadata:
        return ""

    return cast(str, obj_param_metadata.get("field_name", obj_field.name))


def _populate_form(  # noqa: PLR0912, C901
    field_name: str,
    explode: bool,  # noqa: FBT001
    obj: Any,
    get_field_name_func: Callable[..., str],
    delimiter: str,
) -> dict[str, list[str]]:
    """Populate a form."""
    params: dict[str, list[str]] = {}

    if obj is None:
        return params

    if isinstance(obj, msgspec.Struct):
        items = []

        obj_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(obj)
        for obj_field in obj_fields:
            obj_field_name = get_field_name_func(obj_field)
            if obj_field_name == "":
                continue

            val = getattr(obj, obj_field.name)
            if val is None:
                continue

            if explode:
                params[obj_field_name] = [_val_to_string(val)]
            else:
                items.append(f"{obj_field_name}{delimiter}{_val_to_string(val)}")

        if len(items) > 0:
            params[field_name] = [delimiter.join(items)]
    elif isinstance(obj, dict):
        items = []
        for key, value in obj.items():
            if value is None:
                continue

            if explode:
                params[key] = _val_to_string(value)  # type: ignore[assignment]
            else:
                items.append(f"{key}{delimiter}{_val_to_string(value)}")

        if len(items) > 0:
            params[field_name] = [delimiter.join(items)]
    elif isinstance(obj, list):
        items = []

        for value in obj:
            if value is None:
                continue

            if explode:
                if field_name not in params:
                    params[field_name] = []
                params[field_name].append(_val_to_string(value))
            else:
                items.append(_val_to_string(value))

        if len(items) > 0:
            params[field_name] = [delimiter.join([str(item) for item in items])]
    else:
        params[field_name] = [_val_to_string(obj)]

    return params


def _serialize_header(explode: bool, obj: Any) -> str:  # noqa: PLR0912, C901, FBT001
    """Serialize a header."""
    if obj is None:
        return ""

    if isinstance(obj, msgspec.Struct):
        items = []
        obj_fields: tuple[msgspec.structs.FieldInfo, ...] = msgspec.structs.fields(obj)
        for obj_field in obj_fields:
            obj_param_metadata = get_metadata(obj_field).get("header")

            if not obj_param_metadata:
                continue

            obj_field_name = obj_param_metadata.get("field_name", obj_field.name)
            if obj_field_name == "":
                continue

            val = getattr(obj, obj_field.name)
            if val is None:
                continue

            if explode:
                items.append(f"{obj_field_name}={_val_to_string(val)}")
            else:
                items.append(obj_field_name)
                items.append(_val_to_string(val))

        if len(items) > 0:
            return ",".join(items)
    elif isinstance(obj, dict):
        items = []

        for key, value in obj.items():
            if value is None:
                continue

            if explode:
                items.append(f"{key}={_val_to_string(value)}")
            else:
                items.append(key)
                items.append(_val_to_string(value))

        if len(items) > 0:
            return ",".join([str(item) for item in items])
    elif isinstance(obj, list):
        items = []

        for value in obj:
            if value is None:
                continue

            items.append(_val_to_string(value))

        if len(items) > 0:
            return ",".join(items)
    else:
        return f"{_val_to_string(obj)}"

    return ""


def marshal_json(
    val: msgspec.Struct | None,
    typ: type[Any],
    encoder: Callable[..., Any] | None = None,
) -> str:
    """Marshal JSON."""
    if not is_optional_type(typ) and val is None:
        msg = f"Could not marshal None into non-optional type: {typ}"
        raise ValueError(msg)
    return msgspec.json.encode(val, enc_hook=encoder, order="sorted").decode("utf-8")


def match_content_type(content_type: str, pattern: str) -> boolean:
    """Match a content type."""
    if pattern in (content_type, "*", "*/*"):
        return True

    msg = Message()
    msg["content-type"] = content_type
    media_type = msg.get_content_type()

    if media_type == pattern:
        return True

    parts = media_type.split("/")
    return len(parts) == 2 and pattern in (f"{parts[0]}/*", f"*/{parts[1]}")  # noqa: PLR2004


def match_status_codes(status_codes: list[str], status_code: int) -> bool:
    """Match status codes."""
    for code in status_codes:
        if code == str(status_code):
            return True

        if code.endswith("XX") and code.startswith(str(status_code)[:1]):
            return True
    return False


def _val_to_string(val: Any) -> str:
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, dt.datetime):
        return val.isoformat().replace("+00:00", "Z")
    if isinstance(val, Enum):
        return str(val.value)

    return str(val)


def _populate_from_globals(
    param_name: str,
    value: Any,
    param_type: str,
    gbls: dict[str, dict[str, dict[str, Any]]] | None,
) -> Any:
    if (
        value is None
        and gbls is not None
        and "parameters" in gbls
        and param_type in gbls["parameters"]
        and param_name in gbls["parameters"][param_type]
    ):
        global_value = gbls["parameters"][param_type][param_name]
        if global_value is not None:
            value = global_value

    return value


def remove_suffix(input_string: str, suffix: str) -> str:
    """Remove a suffix from a string."""
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string

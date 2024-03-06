"""Base class for operation collections."""

import enum
from typing import TypeVar

import httpx
import msgspec
from httpx import codes

from coinapi import utils
from coinapi._hooks import HookContext
from coinapi.config import CoinAPIConfig
from coinapi.models import errors
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class AcceptEnum(str, enum.Enum):
    """Valid accept header values."""

    APPLICATION_JSON = "application/json"
    TEXT_JSON = "text/json"
    TEXT_PLAIN = "text/plain"
    APPLICATION_X_MSGPACK = "application/x-msgpack"
    ANY = "*/*"


RequestT = TypeVar("RequestT", bound=CoinAPIRequest)
ResponseT = TypeVar("ResponseT", bound=CoinAPIResponse)


class Base:
    """Base class for operation collections."""

    def __init__(self, sdk_config: CoinAPIConfig) -> None:
        self.sdk_configuration = sdk_config

    def _make_request(  # noqa: PLR0912, C901
        self,
        operation_id: str,
        request: RequestT,
        response_cls: type[ResponseT],
        accept_header_override: AcceptEnum | None = None,
    ) -> ResponseT:
        """Send a request."""
        hook_ctx = HookContext(
            operation_id=operation_id,
            oauth2_scopes=[],
            security_source=self.sdk_configuration.security,
        )
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        url = utils.generate_url(type(request), base_url, request.endpoint, request)  # type: ignore[arg-type]
        headers = {}
        data, form = None, None
        if request.method in {"POST", "PUT", "PATCH"}:
            req_content_type, data, form = utils.serialize_request_body(
                request,
                "body",
            )
            if req_content_type is not None and req_content_type not in (
                "multipart/form-data",
                "multipart/mixed",
            ):
                headers["content-type"] = req_content_type
        query_params = utils.get_query_params(type(request), request) or None  # type: ignore[arg-type]
        if accept_header_override is not None:
            headers["Accept"] = accept_header_override.value
        else:
            headers["Accept"] = (
                "application/json;q=1, text/json;q=0.8, text/plain;q=0.5, application/x-msgpack;q=0"
            )
        headers["user-agent"] = self.sdk_configuration.user_agent

        security = (
            self.sdk_configuration.security()
            if callable(self.sdk_configuration.security)
            else self.sdk_configuration.security
        )
        client = utils.configure_security_client(
            self.sdk_configuration.client,
            security,
        )

        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx,  # type: ignore[arg-type]
                httpx.Request(
                    request.method,
                    url,
                    params=query_params,
                    data=data,
                    files=form,
                    headers=headers,
                ),
            )
            http_res = client.send(req)
        except Exception as e:  # noqa: BLE001
            _, exc = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)  # type: ignore[arg-type]
            raise exc from e  # type: ignore[misc]

        if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
            http_res, exc = self.sdk_configuration.get_hooks().after_error(  # type: ignore[assignment]
                hook_ctx,  # type: ignore[arg-type]
                http_res,
                None,
            )
            if exc:
                raise exc
        else:
            result = self.sdk_configuration.get_hooks().after_success(
                hook_ctx,  # type: ignore[arg-type]
                http_res,
            )
            if isinstance(result, Exception):
                raise result
            http_res = result

        content_type = http_res.headers.get("Content-Type", "")

        res = response_cls(
            status_code=http_res.status_code,
            content_type=content_type,
            raw_response=http_res,
        )

        if httpx.codes.is_success(http_res.status_code):
            if utils.match_content_type(content_type, "text/plain"):
                res.content_plain = http_res.text
            elif utils.match_content_type(
                content_type,
                "application/json",
            ) or utils.match_content_type(content_type, "text/json"):
                content_cls = next(
                    field
                    for field in msgspec.structs.fields(response_cls)
                    if field.name == "content"
                ).type
                out = msgspec.json.decode(http_res.content, type=content_cls)
                res.content = out
            elif utils.match_content_type(content_type, "application/x-msgpack"):
                res.body = http_res.content
            else:
                msg = f"unknown content-type received: {content_type}"
                raise errors.CoinAPIError(
                    msg,
                    http_res.status_code,
                    http_res.text,
                    http_res,
                )
        elif codes.is_client_error(http_res.status_code) or codes.is_server_error(
            http_res.status_code,
        ):
            raise errors.CoinAPIError(
                "API error occurred",
                http_res.status_code,
                http_res.text,
                http_res,
            )

        return res

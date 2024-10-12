"""Base class for operation collections."""

import enum
from typing import Any, TypeVar

import httpx
import msgspec
from httpx import codes

from coinapi import utils
from coinapi._hooks import BeforeRequestContext, HookContext
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

    def _make_request(  # type: ignore[return]
        self,
        operation_id: str,
        request: RequestT,
        response_cls: type[ResponseT],
        accept_header_override: AcceptEnum | None = None,
    ) -> ResponseT:
        """Send an HTTP request."""
        hook_ctx = self._create_hook_context(operation_id)
        prepared_request = self._prepare_request(request, accept_header_override)
        client = self._configure_security_client()

        try:
            http_res = self._execute_request(hook_ctx, prepared_request, client)
            return self._process_response(http_res, response_cls)
        except Exception as e:  # noqa: BLE001
            self._handle_request_error(hook_ctx, e)

    def _create_hook_context(self, operation_id: str) -> BeforeRequestContext:
        """Create a hook context."""
        return BeforeRequestContext(
            operation_id=operation_id,
            oauth2_scopes=[],
            security_source=self.sdk_configuration.security,
        )

    def _prepare_request(
        self,
        request: RequestT,
        accept_header_override: AcceptEnum | None,
    ) -> httpx.Request:
        """Prepare an HTTP request."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        url = utils.generate_url(type(request), base_url, request.endpoint, request)
        headers = self._prepare_headers(request, accept_header_override)
        data, form = self._prepare_body(request)
        query_params = utils.get_query_params(type(request), request) or None

        return httpx.Request(
            request.method,
            url,
            params=query_params,
            data=data,
            files=form,
            headers=headers,
        )

    def _prepare_headers(
        self,
        request: RequestT,
        accept_header_override: AcceptEnum | None,
    ) -> dict[str, str]:
        """Prepare request headers."""
        headers = {}
        if request.method in {"POST", "PUT", "PATCH"}:
            req_content_type, _, _ = utils.serialize_request_body(request, "body")
            if req_content_type is not None and req_content_type not in (
                "multipart/form-data",
                "multipart/mixed",
            ):
                headers["content-type"] = req_content_type

        headers["Accept"] = (
            accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/json;q=0.8, text/plain;q=0.5, application/x-msgpack;q=0"
        )
        headers["user-agent"] = self.sdk_configuration.user_agent
        return headers

    def _prepare_body(self, request: RequestT) -> tuple[Any, Any]:
        """Prepare request body."""
        if request.method in {"POST", "PUT", "PATCH"}:
            _, data, form = utils.serialize_request_body(request, "body")
            return data, form
        return None, None

    def _configure_security_client(self) -> utils.SecurityClient:
        """Configure the security client."""
        security = (
            self.sdk_configuration.security()
            if callable(self.sdk_configuration.security)
            else self.sdk_configuration.security
        )
        return utils.configure_security_client(self.sdk_configuration.client, security)

    def _execute_request(
        self,
        hook_ctx: BeforeRequestContext,
        prepared_request: httpx.Request,
        client: utils.SecurityClient,
    ) -> httpx.Response:
        """Execute an HTTP request."""
        req = self.sdk_configuration.get_hooks().before_request(
            hook_ctx,
            prepared_request,
        )
        return client.send(req)

    def _process_response(
        self,
        http_res: httpx.Response,
        response_cls: type[ResponseT],
    ) -> ResponseT:
        """Process an HTTP response."""
        if utils.match_status_codes(["4XX", "5XX"], http_res.status_code):
            self._handle_error_response(http_res)

        content_type = http_res.headers.get("Content-Type", "")
        res = response_cls(
            status_code=http_res.status_code,
            content_type=content_type,
            raw_response=http_res,
        )

        if httpx.codes.is_success(http_res.status_code):
            self._set_response_content(res, http_res, content_type, response_cls)

        return res

    def _set_response_content(
        self,
        res: ResponseT,
        http_res: httpx.Response,
        content_type: str,
        response_cls: type[ResponseT],
    ) -> None:
        """Set the response content."""
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

    def _handle_error_response(self, http_res: httpx.Response) -> None:
        """Handle an error response."""
        if codes.is_client_error(http_res.status_code) or codes.is_server_error(
            http_res.status_code,
        ):
            raise errors.CoinAPIError(
                "API error occurred",
                http_res.status_code,
                http_res.text,
                http_res,
            )

    def _handle_request_error(self, hook_ctx: HookContext, error: Exception) -> None:
        """Handle a request error."""
        _, exc = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, error)  # type: ignore[arg-type]
        raise exc from error  # type: ignore[misc]

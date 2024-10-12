"""SDK Hooks Module."""

from typing import ClassVar

import httpx

from coinapi._hooks.hook_types import (
    AfterErrorContext,
    AfterErrorHook,
    AfterSuccessContext,
    AfterSuccessHook,
    BeforeRequestContext,
    BeforeRequestHook,
    Hooks,
    SDKInitHook,
)


class SDKHooks(Hooks):
    """SDK Hooks."""

    sdk_init_hooks: ClassVar[list[SDKInitHook]] = []
    before_request_hooks: ClassVar[list[BeforeRequestHook]] = []
    after_success_hooks: ClassVar[list[AfterSuccessHook]] = []
    after_error_hooks: ClassVar[list[AfterErrorHook]] = []

    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        """Register an SDK init hook."""
        self.sdk_init_hooks.append(hook)

    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        """Register a before request hook."""
        self.before_request_hooks.append(hook)

    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        """Register an after success hook."""
        self.after_success_hooks.append(hook)

    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        """Register an after error hook."""
        self.after_error_hooks.append(hook)

    def sdk_init(
        self,
        base_url: str,
        client: httpx.Client | None,
    ) -> tuple[str, httpx.Client | None]:
        """Run the SDK init hooks."""
        for hook in self.sdk_init_hooks:
            base_url, client = hook.sdk_init(base_url, client)
        return base_url, client

    def before_request(
        self,
        hook_ctx: BeforeRequestContext,
        request: httpx.Request,
    ) -> httpx.Request:
        """Run the before request hooks."""
        brequest: httpx.Request | Exception = request
        for hook in self.before_request_hooks:
            brequest = hook.before_request(hook_ctx, request)
            if isinstance(brequest, Exception):
                raise brequest

        return brequest  # type: ignore[return-value]

    def after_success(
        self,
        hook_ctx: AfterSuccessContext,
        response: httpx.Response,
    ) -> httpx.Response:
        """Run the after success hooks."""
        aresponse: httpx.Response | Exception = response
        for hook in self.after_success_hooks:
            aresponse = hook.after_success(hook_ctx, response)
            if isinstance(aresponse, Exception):
                raise aresponse
        return aresponse  # type: ignore[return-value]

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: httpx.Response | None,
        error: Exception | None,
    ) -> tuple[httpx.Response | None, Exception | None]:
        """Run the after error hooks."""
        for hook in self.after_error_hooks:
            result = hook.after_error(hook_ctx, response, error)
            if isinstance(result, Exception):
                raise result
            response, error = result
        return response, error

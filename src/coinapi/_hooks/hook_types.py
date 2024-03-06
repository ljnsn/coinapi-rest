"""Hook types."""

import abc
from collections.abc import Callable
from typing import Any

import httpx


class HookContext:
    """Hook context."""

    operation_id: str
    oauth2_scopes: list[str] | None = None
    security_source: Any | Callable[[], Any] | None = None

    def __init__(
        self,
        operation_id: str,
        oauth2_scopes: list[str] | None,
        security_source: Any | Callable[[], Any] | None,
    ) -> None:
        self.operation_id = operation_id
        self.oauth2_scopes = oauth2_scopes
        self.security_source = security_source


class BeforeRequestContext(HookContext):
    pass


class AfterSuccessContext(HookContext):
    pass


class AfterErrorContext(HookContext):
    pass


class SDKInitHook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sdk_init(
        self,
        base_url: str,
        client: httpx.Client | None,
    ) -> tuple[str, httpx.Client | None]:
        pass


class BeforeRequestHook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def before_request(
        self,
        hook_ctx: BeforeRequestContext,
        request: httpx.Request,
    ) -> httpx.Request | Exception:
        pass


class AfterSuccessHook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def after_success(
        self,
        hook_ctx: AfterSuccessContext,
        response: httpx.Response,
    ) -> httpx.Response | Exception:
        pass


class AfterErrorHook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: httpx.Response | None,
        error: Exception | None,
    ) -> tuple[httpx.Response | None, Exception | None] | Exception:
        pass


class Hooks(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        pass

    @abc.abstractmethod
    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        pass

    @abc.abstractmethod
    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        pass

    @abc.abstractmethod
    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        pass

"""SDK Config."""

from collections.abc import Callable
from importlib.metadata import version
from typing import ClassVar

import httpx
import msgspec

from coinapi._hooks import SDKHooks
from coinapi.models import components
from coinapi.utils import utils

SERVERS = [
    "https://rest.coinapi.io",
]
"""Contains the list of available CoinAPI servers"""


class CoinAPIConfig(msgspec.Struct):
    """The configuration for the SDK."""

    version: ClassVar[str] = version("coinapi-rest")

    client: httpx.Client | None
    security: components.Security | Callable[[], components.Security] | None = None
    server_url: str | None = ""
    server_idx: int | None = 0
    openapi_doc_version: str = "v1"
    user_agent: str = "coinapi-rest/python 0.0.1 CoinAPI v1"
    _hooks: SDKHooks | None = None

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        """Get the server details."""
        if self.server_url:
            return utils.remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}

    def get_hooks(self) -> SDKHooks:
        """Get the hooks."""
        assert self._hooks is not None  # noqa: S101
        return self._hooks

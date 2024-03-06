"""Operation base class."""

from typing import Any, ClassVar

import httpx
import msgspec


class CoinAPIRequest(msgspec.Struct, frozen=True):
    """CoinAPI request."""

    method: ClassVar[str]
    r"""HTTP method for this operation."""
    endpoint: ClassVar[str]
    r"""HTTP endpoint for this operation."""


class CoinAPIResponse(msgspec.Struct, omit_defaults=True):
    """CoinAPI response."""

    content_type: str = msgspec.field()
    r"""HTTP response content type for this operation"""
    status_code: int = msgspec.field()
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response = msgspec.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    content_plain: str | None = msgspec.field(default=None)
    r"""successful operation"""
    content: Any = msgspec.field(default=None)
    r"""successful operation"""
    body: bytes | None = msgspec.field(default=None)
    r"""successful operation"""

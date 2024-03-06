"""Get current quotes by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_quotetrade
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1QuotesSymbolIDCurrentRequest(CoinAPIRequest, frozen=True):
    """Request for operation GetV1QuotesSymbolIDCurrent."""

    method = "GET"
    endpoint = "/v1/quotes/{symbol_id}/current"
    symbol_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "symbol_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""The symbol identifier (from the Metadata -> Symbols)"""


class GetV1QuotesSymbolIDCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response for operation GetV1QuotesSymbolIDCurrent."""

    content: v1_quotetrade.V1QuoteTrade | None = msgspec.field(default=None)
    r"""successful operation"""

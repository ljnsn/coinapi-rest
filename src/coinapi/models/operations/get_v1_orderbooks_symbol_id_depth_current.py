"""Get order book depth by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_orderbookdepth
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1OrderbooksSymbolIDDepthCurrentRequest(CoinAPIRequest, frozen=True):
    """Get current orderbook for the given symbol."""

    method = "GET"
    endpoint = "/v1/orderbooks/{symbol_id}/depth/current"
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
    r"""The symbol ID (from the Metadata -> Symbols)"""
    limit_levels: Annotated[
        int | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "limit_levels",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The maximum number of levels to include in the response."""


class GetV1OrderbooksSymbolIDDepthCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response schema for operation GetV1OrderbooksSymbolIDDepthCurrent."""

    content: v1_orderbookdepth.V1OrderBookDepth | None = msgspec.field(default=None)
    r"""successful operation"""

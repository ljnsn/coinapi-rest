"""Get currelt order books by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_orderbookbase
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1OrderbooksSymbolIDCurrentRequest(CoinAPIRequest, frozen=True):
    """Get current order book for specified symbol."""

    method = "GET"
    endpoint = "/v1/orderbooks/{symbol_id}/current"
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


class GetV1OrderbooksSymbolIDCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Get current order book for specified symbol."""

    content: v1_orderbookbase.V1OrderBookBase | None = msgspec.field(default=None)
    r"""successful operation"""

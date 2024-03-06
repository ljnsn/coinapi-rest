"""Get current L3 order books by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_orderbookbase
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1Orderbooks3SymbolIDCurrentRequest(CoinAPIRequest, frozen=True):
    """[order book l3] Current order book by symbol_id."""

    method = "GET"
    endpoint = "/v1/orderbooks3/{symbol_id}/current"
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


class GetV1Orderbooks3SymbolIDCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """HTTP response for get_v1_orderbooks3_symbol_id_current operation."""

    content: v1_orderbookbase.V1OrderBookBase | None = msgspec.field(default=None)
    r"""successful operation"""

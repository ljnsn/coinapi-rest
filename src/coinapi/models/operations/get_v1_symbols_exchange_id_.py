"""Get symbols by exchange ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_symbol as components_v1_symbol
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1SymbolsExchangeIDRequest(CoinAPIRequest, frozen=True):
    """Get v1 symbols exchange id request."""

    method = "GET"
    endpoint = "/v1/symbols/{exchange_id}"
    exchange_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "exchange_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""The ID of the exchange (from the Metadata -> Exchanges)"""
    filter_symbol_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_symbol_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The filter for symbol ID."""
    filter_asset_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_asset_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The filter for asset ID."""


class GetV1SymbolsExchangeIDResponse(CoinAPIResponse, omit_defaults=True):
    """Get v1 symbols exchange id response."""

    content: list[components_v1_symbol.V1Symbol] | None = msgspec.field(default=None)
    r"""successful operation"""

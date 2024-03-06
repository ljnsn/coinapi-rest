"""Get symbols."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_symbol as components_v1_symbol
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1SymbolsRequest(CoinAPIRequest, frozen=True):
    """V1 symbols request."""

    method = "GET"
    endpoint = "/v1/symbols"
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
    r"""Comma or semicolon delimited parts of symbol identifier used to filter response. (optional, eg. `BITSTAMP`_ or `BINANCE_SPOT_`)"""
    filter_exchange_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_exchange_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The filter for exchange ID."""
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


class GetV1SymbolsResponse(CoinAPIResponse, omit_defaults=True):
    """V1 symbols response."""

    content: list[components_v1_symbol.V1Symbol] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

"""Get trade history by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_trade
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1TradesSymbolIDHistoryRequest(CoinAPIRequest, frozen=True):
    """Historical data trades request."""

    method = "GET"
    endpoint = "/v1/trades/{symbol_id}/history"
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
    r"""Symbol identifier for requested timeseries (from the Metadata -> Symbols)"""
    time_start: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "time_start",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Starting time in ISO 8601 (required)"""
    time_end: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "time_end",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Timeseries ending time in ISO 8601 (optional, if not supplied then the data is returned to the end or when result elements count reaches the limit)"""
    limit: Annotated[
        int | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "limit",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=100)
    r"""Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request)"""
    include_id: Annotated[
        bool | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "include_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=False)
    r"""Information that additional exchange trade identifier should be included in the `id_trade` parameter of the trade if exchange providing identifiers."""


class GetV1TradesSymbolIDHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """Historical data trades response."""

    content: list[v1_trade.V1Trade] | None = msgspec.field(default=None)
    r"""successful operation"""

"""Get latest OHLCV by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_timeseriesitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1OhlcvSymbolIDLatestRequest(CoinAPIRequest, frozen=True):
    """GetV1OhlcvSymbolIDLatestRequest holds the parameters for GetV1OhlcvSymbolIDLatest."""

    method = "GET"
    endpoint = "/v1/ohlcv/{symbol_id}/latest"
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
    r"""Symbol identifier of requested timeseries (from the Metadata -> Symbols)"""
    period_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "period_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Identifier of requested timeseries period (required, e.g. `5SEC` or `2MTH`)"""
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
    include_empty_items: Annotated[
        bool | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "include_empty_items",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=False)
    r"""Include items with no activity? (optional, default value is `false`, possible values are `true` or `false`)"""


class GetV1OhlcvSymbolIDLatestResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1OhlcvSymbolIDLatestResponse holds the response data for GetV1OhlcvSymbolIDLatest."""

    content: list[v1_timeseriesitem.V1TimeseriesItem] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

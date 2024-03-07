"""Get exchange rate history between two assets."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_exchangeratestimeseriesitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1PairHistoryRequest(CoinAPIRequest, frozen=True):
    """Get historical exchange rate data for a specific asset pair and time period."""

    method = "GET"
    endpoint = "/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history"
    asset_id_base: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "asset_id_base",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""Requested exchange rates base asset identifier (from the Metadata -> Assets)"""
    asset_id_quote: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "asset_id_quote",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""Requested exchange rates base asset identifier (from the Metadata -> Assets)"""
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
    r"""Identifier of requested timeseries period (required, e.g. `5SEC` or `1HRS`)"""
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
    r"""Timeseries starting time in ISO 8601 (required)"""
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
    r"""Timeseries ending time in ISO 8601 (required)"""
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


class GetV1PairHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """Get historical exchange rate data for a specific asset pair and time period."""

    content: (
        list[v1_exchangeratestimeseriesitem.V1ExchangeRatesTimeseriesItem] | None
    ) = msgspec.field(default=None)
    r"""successful operation"""

"""Get OHLCV history by exchange ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import models_exchangetimeseriesitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1OhlcvExchangesExchangeIDHistoryRequest(CoinAPIRequest, frozen=True):
    """GetV1OhlcvExchangesExchangeIDHistoryRequest holds the parameters for GetV1OhlcvExchangesExchangeIDHistory."""

    method = "GET"
    endpoint = "/v1/ohlcv/exchanges/{exchange_id}/history"
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
    r"""Exchange identifier of requested timeseries (from the Metadata -> Exchanges)"""
    period_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "period_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""Identifier of requested timeseries period (e.g. `5SEC` or `2MTH`)"""
    time_start: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "time_start",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""Timeseries starting time in ISO 8601"""
    time_end: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "time_end",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""Timeseries ending time in ISO 8601"""


class GetV1OhlcvExchangesExchangeIDHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1OhlcvExchangesExchangeIDHistoryResponse holds the response data for GetV1OhlcvExchangesExchangeIDHistory."""

    content: list[models_exchangetimeseriesitem.ModelsExchangeTimeseriesItem] | None = (
        msgspec.field(default=None)
    )
    r"""successful operation"""

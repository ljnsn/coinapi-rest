"""Get current exchange metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_generaldata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsExchangeCurrentRequest(CoinAPIRequest, frozen=True):
    """Get current exchange rate for any cryptocurrency in any other currency."""

    method = "GET"
    endpoint = "/v1/metrics/exchange/current"
    exchange_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "exchange_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""The exchange identifier (from the Metadata -> Exchanges)"""
    metric_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "metric_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The metric identifier (from the Metrics -> Listing)"""


class GetV1MetricsExchangeCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response schema for get_v1_metrics_exchange_current operation."""

    content: list[v1_generaldata.V1GeneralData] | None = msgspec.field(default=None)
    r"""successful operation"""

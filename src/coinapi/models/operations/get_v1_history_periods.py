"""Get exchange rate history periods."""

from __future__ import annotations

import msgspec

from coinapi.models.components import (
    v1_timeseriesperiod as components_v1_timeseriesperiod,
)
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1HistoryPeriodsRequest(CoinAPIRequest, frozen=True):
    """Get historical exchange rate data for a specific asset pair and time period."""

    method = "GET"
    endpoint = "/v1/exchangerate/history/periods"


class GetV1HistoryPeriodsResponse(CoinAPIResponse, omit_defaults=True):
    """Get historical exchange rate data for a specific asset pair and time period."""

    content: list[components_v1_timeseriesperiod.V1TimeseriesPeriod] | None = (
        msgspec.field(default=None)
    )
    r"""successful operation"""

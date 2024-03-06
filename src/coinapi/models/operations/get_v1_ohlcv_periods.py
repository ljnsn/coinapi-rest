"""Get OHLCV periods."""

from __future__ import annotations

import msgspec

from coinapi.models.components import v1_timeseriesperiod
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1OhlcvPeriodsRequest(CoinAPIRequest, frozen=True):
    """GetV1OhlcvPeriodsRequest holds the parameters for GetV1OhlcvPeriods."""

    method = "GET"
    endpoint = "/v1/ohlcv/periods"


class GetV1OhlcvPeriodsResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1OhlcvPeriodsResponse holds the response data for GetV1OhlcvPeriods."""

    content: list[v1_timeseriesperiod.V1TimeseriesPeriod] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

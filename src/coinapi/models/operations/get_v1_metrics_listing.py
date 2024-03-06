"""List metrics."""

from __future__ import annotations

import msgspec

from coinapi.models.components import v1_metric
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsListingRequest(CoinAPIRequest, frozen=True):
    """Request of get_v1_metrics_listing operation."""

    endpoint = "/v1/metrics/listing"
    method = "GET"


class GetV1MetricsListingResponse(CoinAPIResponse, omit_defaults=True):
    """Response of get_v1_metrics_listing operation."""

    content: list[v1_metric.V1Metric] | None = msgspec.field(default=None)
    r"""successful operation"""

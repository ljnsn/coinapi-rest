"""List exchange metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_listingitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsExchangeListingRequest(CoinAPIRequest, frozen=True):
    """Request of get_v1_metrics_exchange_listing operation."""

    method = "GET"
    endpoint = "/v1/metrics/exchange/listing"
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


class GetV1MetricsExchangeListingResponse(CoinAPIResponse, omit_defaults=True):
    """Response of get_v1_metrics_exchange_listing operation."""

    content: list[v1_listingitem.V1ListingItem] | None = msgspec.field(default=None)
    r"""successful operation"""

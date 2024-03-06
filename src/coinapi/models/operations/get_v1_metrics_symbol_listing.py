"""List symbol metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_listingitem as components_v1_listingitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsSymbolListingRequest(CoinAPIRequest, frozen=True):
    """Get v1 metrics symbol listing."""

    method = "GET"
    endpoint = "/v1/metrics/symbol/listing"
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
    r"""Metric identifier (from the Metrics -> Listing)"""
    exchange_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "exchange_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Exchange identifier (from the Metadata -> Exchanges)"""
    symbol_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "symbol_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Symbol identifier (from the Metadata -> Symbols)"""


class GetV1MetricsSymbolListingResponse(CoinAPIResponse, omit_defaults=True):
    """Response of GetV1MetricsSymbolListingRequest."""

    content: list[components_v1_listingitem.V1ListingItem] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

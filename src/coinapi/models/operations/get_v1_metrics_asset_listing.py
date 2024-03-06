"""List asset metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_listingitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsAssetListingRequest(CoinAPIRequest, frozen=True):
    """Get v1 metrics asset listing request."""

    method = "GET"
    endpoint = "/v1/metrics/asset/listing"
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
    chain_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "chain_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Chain identifier"""
    network_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "network_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Network identifier"""
    asset_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "asset_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Asset identifier (from the Metadata -> Assets)"""
    asset_id_external: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "asset_id_external",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The asset external identifier"""


class GetV1MetricsAssetListingResponse(CoinAPIResponse, omit_defaults=True):
    """Response of GetV1MetricsAssetListing."""

    content: list[v1_listingitem.V1ListingItem] | None = msgspec.field(default=None)
    r"""successful operation"""

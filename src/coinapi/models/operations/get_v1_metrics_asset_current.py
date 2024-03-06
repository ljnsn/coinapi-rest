"""Get current asset metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_generaldata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsAssetCurrentRequest(CoinAPIRequest, frozen=True):
    """Get current data for an asset."""

    method = "GET"
    path = "/v1/metrics/asset/current"
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
    r"""Exchange asset identifier"""
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


class GetV1MetricsAssetCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response of GetV1MetricsAssetCurrent."""

    content: list[v1_generaldata.V1GeneralData] | None = msgspec.field(default=None)
    r"""successful operation"""
    body: bytes | None = msgspec.field(default=None)

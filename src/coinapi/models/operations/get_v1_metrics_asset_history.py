"""Get asset metrics history."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

import msgspec

from coinapi.models.components import v1_metricdata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsAssetHistoryRequest(CoinAPIRequest, frozen=True):
    """Get historical data for an asset and a metric."""

    method = "GET"
    endpoint = "/v1/metrics/asset/history"
    metric_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "metric_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""Metric identifier (from the Metrics -> Listing)"""
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
    r"""Exchange identifier (from the Metadata -> Exchanges)"""
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
    time_start: Annotated[
        datetime | None,
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
    r"""Starting time in ISO 8601"""
    time_end: Annotated[
        datetime | None,
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
    r"""Ending time in ISO 8601"""
    time_format: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "time_format",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""If set, returned values will be in unix timestamp format (valid values: unix_sec, unix_millisec, unix_microsec, unix_nanosec)"""
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
    r"""Identifier of requested timeseries period (e.g. `5SEC` or `2MTH`), default value is `1SEC`"""
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


class GetV1MetricsAssetHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """Get historical data for an asset and a metric."""

    content: list[v1_metricdata.V1MetricData] | None = msgspec.field(default=None)
    r"""successful operation"""

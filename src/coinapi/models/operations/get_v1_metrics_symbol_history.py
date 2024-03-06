"""Get symbol metrics history."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

import msgspec

from coinapi.models.components import v1_metricdata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsSymbolHistoryRequest(CoinAPIRequest, frozen=True):
    """Get v1 metrics symbol history request."""

    method = "GET"
    endpoint = "/v1/metrics/symbol/history"
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
    symbol_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "symbol_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field()
    r"""Symbol identifier (from the Metadata -> Symbols)"""
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


class GetV1MetricsSymbolHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """Get v1 metrics symbol history response."""

    content: list[v1_metricdata.V1MetricData] | None = msgspec.field(default=None)
    r"""successful operation"""

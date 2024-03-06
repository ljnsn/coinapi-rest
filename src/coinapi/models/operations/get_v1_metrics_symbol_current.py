"""Get current symbol metrics."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_generaldata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetricsSymbolCurrentRequest(CoinAPIRequest, frozen=True):
    """Get v1 metrics symbol current."""

    method = "GET"
    endpoint = "/v1/metrics/symbol/current"
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
    r"""Exchange id (from the Metadata -> Exchanges)"""


class GetV1MetricsSymbolCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response of GetV1MetricsSymbolCurrentRequest."""

    content: list[v1_generaldata.V1GeneralData] | None = msgspec.field(default=None)
    r"""successful operation"""

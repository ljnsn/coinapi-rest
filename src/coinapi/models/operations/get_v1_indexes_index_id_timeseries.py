"""Get index timeseries."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

import msgspec

from coinapi.models.components import v1_indextimeseriesitem
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1IndexesIndexIDTimeseriesRequest(CoinAPIRequest, frozen=True):
    """Get index timeseries data request."""

    method = "GET"
    endpoint = "/v1/indexes/{index_id}/timeseries"
    index_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "index_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
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


class GetV1IndexesIndexIDTimeseriesResponse(CoinAPIResponse, omit_defaults=True):
    """Get index timeseries data response."""

    content: list[v1_indextimeseriesitem.V1IndexTimeseriesItem] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

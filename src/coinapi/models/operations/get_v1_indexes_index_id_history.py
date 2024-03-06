"""Get index composition history."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

import msgspec

from coinapi.models.components import v1_indexvalue as components_v1_indexvalue
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1IndexesIndexIDHistoryRequest(CoinAPIRequest, frozen=True):
    """Get index history request."""

    method = "GET"
    endpoint = "/v1/indexes/{index_id}/history"
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


class GetV1IndexesIndexIDHistoryResponse(CoinAPIResponse, omit_defaults=True):
    """Get index history response."""

    content: list[components_v1_indexvalue.V1IndexValue] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

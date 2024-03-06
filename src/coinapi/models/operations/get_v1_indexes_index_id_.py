"""Get an index by ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_indexdata as components_v1_indexdata
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1IndexesIndexIDRequest(CoinAPIRequest, frozen=True):
    """Request of get_v1_indexes_index_id_ operation."""

    method = "GET"
    endpoint = "/v1/indexes/{index_id}"
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


class GetV1IndexesIndexIDResponse(CoinAPIResponse, omit_defaults=True):
    """Response of get_v1_indexes_index_id_ operation."""

    content: components_v1_indexdata.V1IndexData | None = msgspec.field(default=None)
    r"""successful operation"""

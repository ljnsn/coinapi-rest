"""Create an index."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_indexdata, v1_indexdataresponse
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class PostV1IndexesJSONRequest(CoinAPIRequest, frozen=True):
    """Request of post_v1_indexes_json operation."""

    method = "POST"
    endpoint = "/v1/indexes"
    body: Annotated[
        v1_indexdata.V1IndexData | None,
        msgspec.Meta(extra={"request": {"media_type": "application/json"}}),
    ] = msgspec.field(default=None)


class PostV1IndexesJSONResponse(CoinAPIResponse, omit_defaults=True):
    """Response of post_v1_indexes_json operation."""

    content: v1_indexdataresponse.V1IndexDataResponse | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

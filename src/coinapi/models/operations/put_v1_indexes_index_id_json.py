"""Update an index."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_indexdata as components_v1_indexdata
from coinapi.models.components import (
    v1_indexdataresponse as components_v1_indexdataresponse,
)
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class PutV1IndexesIndexIDJSONRequest(CoinAPIRequest, frozen=True):
    """Update index request."""

    method = "PUT"
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
    body: Annotated[
        components_v1_indexdata.V1IndexData | None,
        msgspec.Meta(extra={"request": {"media_type": "application/json"}}),
    ] = msgspec.field(default=None)


class PutV1IndexesIndexIDJSONResponse(CoinAPIResponse, omit_defaults=True):
    """Update index response."""

    content: components_v1_indexdataresponse.V1IndexDataResponse | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

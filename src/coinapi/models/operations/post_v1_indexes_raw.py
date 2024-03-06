"""Create an index."""

from __future__ import annotations

import msgspec

from coinapi.models.components import v1_indexdataresponse
from coinapi.models.operations.base import CoinAPIResponse


class PostV1IndexesRawResponse(CoinAPIResponse, omit_defaults=True):
    """Raw index data response."""

    content: v1_indexdataresponse.V1IndexDataResponse | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

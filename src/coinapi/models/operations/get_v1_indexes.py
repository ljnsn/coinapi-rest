"""Get indexes."""

from __future__ import annotations

import msgspec

from coinapi.models.components import v1_index as components_v1_index
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1IndexesRequest(CoinAPIRequest, frozen=True):
    """Request of get_v1_indexes operation."""

    method = "GET"
    endpoint = "/v1/indexes"


class GetV1IndexesResponse(CoinAPIResponse, omit_defaults=True):
    """Response of get_v1_indexes operation."""

    content: list[components_v1_index.V1Index] | None = msgspec.field(default=None)
    r"""successful operation"""

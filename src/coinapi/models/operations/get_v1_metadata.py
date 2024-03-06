"""Get metadata."""

from __future__ import annotations

from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1MetadataRequest(CoinAPIRequest, frozen=True):
    """GetV1MetadataRequest request."""

    method = "GET"
    endpoint = "/v1/metadata"


class GetV1MetadataResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1MetadataResponse response."""

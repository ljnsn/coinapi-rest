"""Get assets."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_asset as components_v1_asset
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1AssetsRequest(CoinAPIRequest, frozen=True):
    """Get assets request."""

    method = "GET"
    endpoint = "/v1/assets"
    filter_asset_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_asset_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Comma or semicolon delimited asset identifiers used to filter response. (optional, eg. `BTC;ETH`)."""
    include_supply: Annotated[
        bool | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "include_supply",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=False)
    r"""Flag indicating whether to include supply information."""


class GetV1AssetsResponse(CoinAPIResponse):
    """V1 assets response."""

    content: list[components_v1_asset.V1Asset] | None = msgspec.field(default=None)
    r"""successful operation"""

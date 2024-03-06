"""Get an asset by ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_asset as components_v1_asset
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1AssetsAssetIDRequest(CoinAPIRequest, frozen=True):
    """Get asset by ID."""

    method = "GET"
    endpoint = "/v1/assets/{asset_id}"
    asset_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "asset_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""The asset ID."""


class GetV1AssetsAssetIDResponse(CoinAPIResponse, omit_defaults=True):
    """V1 assets response."""

    content: list[components_v1_asset.V1Asset] | None = msgspec.field(default=None)
    r"""successful operation"""

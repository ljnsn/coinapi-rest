"""Get asset icons."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_icon as components_v1_icon
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1AssetsIconsSizeRequest(CoinAPIRequest, frozen=True):
    """Request for operation GetV1AssetsIconsSize."""

    method = "GET"
    endpoint = "/v1/assets/icons/{size}"
    size: Annotated[
        int,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "size",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""The size of the icons."""


class GetV1AssetsIconsSizeResponse(CoinAPIResponse, omit_defaults=True):
    """Response for operation GetV1AssetsIconsSize."""

    content: list[components_v1_icon.V1Icon] | None = msgspec.field(default=None)
    r"""successful operation"""

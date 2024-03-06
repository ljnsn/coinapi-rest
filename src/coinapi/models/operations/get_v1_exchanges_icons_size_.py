"""Get exchange icons."""

from __future__ import annotations

import dataclasses
from typing import Annotated

import msgspec

from coinapi.models.components import v1_icon as components_v1_icon
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1ExchangesIconsSizeRequest(CoinAPIRequest, frozen=True):
    """GetV1ExchangesIconsSizeRequest request."""

    method = "GET"
    endpoint = "/v1/exchanges/icons/{size}"
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
    ] = dataclasses.field()
    r"""The size of the icons."""


class GetV1ExchangesIconsSizeResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1ExchangesIconsSizeResponse response."""

    content: list[components_v1_icon.V1Icon] | None = dataclasses.field(default=None)
    r"""successful operation"""

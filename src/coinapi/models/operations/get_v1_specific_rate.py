"""Get a specific exchange rate."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_exchangerate as components_v1_exchangerate
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1SpecificRateRequest(CoinAPIRequest, frozen=True):
    """[exchange rates] Get specific rate."""

    method = "GET"
    endpoint = "/v1/exchangerate/{asset_id_base}/{asset_id_quote}"
    asset_id_base: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "asset_id_base",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""Requested exchange rate base asset identifier (from the Metadata -> Assets)"""
    asset_id_quote: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "asset_id_quote",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""Requested exchange rate quote asset identifier (from the Metadata -> Assets)"""
    time: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {"field_name": "time", "style": "form", "explode": True},
            },
        ),
    ] = msgspec.field(default=None)
    r"""Time at which exchange rate is calculated (optional, if not supplied then current rate is returned)"""


class GetV1SpecificRateResponse(CoinAPIResponse, omit_defaults=True):
    """[exchange rates] Get specific rate."""

    content: components_v1_exchangerate.V1ExchangeRate | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

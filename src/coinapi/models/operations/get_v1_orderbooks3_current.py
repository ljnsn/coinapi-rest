"""Get current L3 order books."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_orderbookbase
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1Orderbooks3CurrentRequest(CoinAPIRequest, frozen=True):
    """[order book l3] Current order books."""

    method = "GET"
    endpoint = "/v1/orderbooks3/current"
    filter_symbol_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_symbol_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Comma or semicolon delimited parts of symbol identifier used to filter the response."""
    limit_levels: Annotated[
        int | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "limit_levels",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""The maximum number of levels to include in the response."""


class GetV1Orderbooks3CurrentResponse(CoinAPIResponse, omit_defaults=True):
    """HTTP response for get_v1_orderbooks3_current operation."""

    content: list[v1_orderbookbase.V1OrderBookBase] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

"""Get current quotes."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_quotetrade
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1QuotesCurrentRequest(CoinAPIRequest, frozen=True):
    """Request for operation GetV1QuotesCurrent."""

    method = "GET"
    endpoint = "/v1/quotes/current"
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
    r"""Comma or semicolon delimited parts of symbol identifier used to filter response. (optional)"""


class GetV1QuotesCurrentResponse(CoinAPIResponse, omit_defaults=True):
    """Response for operation GetV1QuotesCurrent."""

    content: list[v1_quotetrade.V1QuoteTrade] | None = msgspec.field(default=None)
    r"""successful operation"""

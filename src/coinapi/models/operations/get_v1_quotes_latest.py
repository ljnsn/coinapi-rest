"""Get latest quotes."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_quote
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1QuotesLatestRequest(CoinAPIRequest, frozen=True):
    """Request for operation GetV1QuotesLatest."""

    method = "GET"
    endpoint = "/v1/quotes/latest"
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
    limit: Annotated[
        int | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "limit",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=100)
    r"""Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request)"""


class GetV1QuotesLatestResponse(CoinAPIResponse, omit_defaults=True):
    """Response for operation GetV1QuotesLatest."""

    content: list[v1_quote.V1Quote] | None = msgspec.field(default=None)
    r"""successful operation"""

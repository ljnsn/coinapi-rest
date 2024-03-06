"""Get latest quotes by symbol ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_quote
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1QuotesSymbolIDLatestRequest(CoinAPIRequest, frozen=True):
    """Request for operation GetV1QuotesSymbolIDLatest."""

    method = "GET"
    endpoint = "/v1/quotes/{symbol_id}/latest"
    symbol_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "symbol_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""Symbol identifier of requested timeseries (from the Metadata -> Symbols)"""
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


class GetV1QuotesSymbolIDLatestResponse(CoinAPIResponse, omit_defaults=True):
    """Response for operation GetV1QuotesSymbolIDLatest."""

    content: list[v1_quote.V1Quote] | None = msgspec.field(default=None)
    r"""successful operation"""

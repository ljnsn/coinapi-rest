"""Get exchanges."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_exchange as components_v1_exchange
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1ExchangesRequest(CoinAPIRequest, frozen=True):
    """GetV1ExchangesRequest request."""

    method = "GET"
    endpoint = "/v1/exchanges"
    filter_exchange_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_exchange_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Comma or semicolon delimited exchange identifiers used to filter response. (optional, eg. `BITSTAMP;GEMINI`)"""


class GetV1ExchangesResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1ExchangesResponse response."""

    content: list[components_v1_exchange.V1Exchange] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

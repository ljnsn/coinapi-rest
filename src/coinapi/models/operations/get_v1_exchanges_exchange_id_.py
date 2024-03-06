"""Get an exchange by ID."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_exchange as components_v1_exchange
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1ExchangesExchangeIDRequest(CoinAPIRequest, frozen=True):
    """GetV1ExchangesExchangeIDRequest request."""

    method = "GET"
    endpoint = "/v1/exchanges/{exchange_id}"
    exchange_id: Annotated[
        str,
        msgspec.Meta(
            extra={
                "path_param": {
                    "field_name": "exchange_id",
                    "style": "simple",
                    "explode": False,
                },
            },
        ),
    ] = msgspec.field()
    r"""The ID of the exchange."""


class GetV1ExchangesExchangeIDResponse(CoinAPIResponse, omit_defaults=True):
    """GetV1ExchangesExchangeIDResponse response."""

    content: list[components_v1_exchange.V1Exchange] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

"""Get symbols map for an exchange."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_symbolmapping as components_v1_symbolmapping
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1SymbolsMapExchangeIDRequest(CoinAPIRequest, frozen=True):
    """Get v1 symbols map exchange id request."""

    method = "GET"
    endpoint = "/v1/symbols/map/{exchange_id}"
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
    r"""The ID of the exchange (from the Metadata -> Exchanges)"""


class GetV1SymbolsMapExchangeIDResponse(CoinAPIResponse, omit_defaults=True):
    """Get v1 symbols map exchange id response."""

    content: list[components_v1_symbolmapping.V1SymbolMapping] | None = msgspec.field(
        default=None,
    )
    r"""successful operation"""

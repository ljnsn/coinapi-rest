"""Get exchange rates for a base asset."""

from __future__ import annotations

from typing import Annotated

import msgspec

from coinapi.models.components import v1_exchangeratesrate
from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse


class GetV1BaseRatesRequest(CoinAPIRequest, frozen=True):
    """Get specific exchange rate for a specific base and quote asset at a given time or the current rate."""

    method = "GET"
    endpoint = "/v1/exchangerate/{asset_id_base}"
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
    r"""Requested exchange rates base asset identifier (from the Metadata -> Assets)"""
    filter_asset_id: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "filter_asset_id",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=None)
    r"""Comma or semicolon delimited asset identifiers used to filter response (optional)"""
    invert: Annotated[
        bool | None,
        msgspec.Meta(
            extra={
                "query_param": {
                    "field_name": "invert",
                    "style": "form",
                    "explode": True,
                },
            },
        ),
    ] = msgspec.field(default=False)
    r"""True will invert all the rates (optional, if true then rates will be calculated as `rate = 1 / actual_rate` eg. `USD/BTC` as `BTC/USD`)"""
    time: Annotated[
        str | None,
        msgspec.Meta(
            extra={
                "query_param": {"field_name": "time", "style": "form", "explode": True},
            },
        ),
    ] = msgspec.field(default=None)
    r"""Time for historical rates (optional)"""


# NOTE: the spec for this response is wrong. Supposedly, the `V1ExchangeRatesRate` array is returned directly,
#       but the actual response is a JSON object with a `rates` field containing the array.
class GetV1BaseRatesResponse(CoinAPIResponse, omit_defaults=True):
    """Get specific exchange rate for a specific base and quote asset at a given time or the current rate."""

    content: v1_exchangeratesrate.V1ExchangeRates | None = msgspec.field(default=None)
    r"""successful operation"""

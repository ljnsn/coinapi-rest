"""Last trade."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1LastTrade(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents the last executed transaction."""

    time_exchange: dt.datetime = msgspec.field()
    r"""The exchange time of the last trade."""
    time_coinapi: dt.datetime = msgspec.field()
    r"""The CoinAPI time when the last trade was received."""
    uuid: str = msgspec.field()
    r"""The UUID of the last trade."""
    price: float = msgspec.field()
    r"""The price of the last trade."""
    size: float = msgspec.field()
    r"""The size of the last trade."""
    taker_side: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The taker side of the last trade."""

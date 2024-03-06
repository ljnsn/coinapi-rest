"""Order book depth."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1OrderBookDepth(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents the depth of an order book."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier."""
    time_exchange: dt.datetime = msgspec.field()
    r"""The exchange time of the order book."""
    time_coinapi: dt.datetime = msgspec.field()
    r"""The CoinAPI time when the order book was received."""
    ask_levels: int = msgspec.field()
    r"""The number of ask levels in the order book."""
    bid_levels: int = msgspec.field()
    r"""The number of bid levels in the order book."""
    ask_depth: float = msgspec.field()
    r"""The depth of the ask side of the order book."""
    bid_depth: float = msgspec.field()
    r"""The depth of the bid side of the order book."""

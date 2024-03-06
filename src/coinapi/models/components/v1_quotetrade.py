"""Quote trade."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.models.components.v1_lasttrade import V1LastTrade
from coinapi.utils.aliases import OptionalFloatOrUnset, OptionalStrOrUnset


class V1QuoteTrade(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a quote trade data model."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier."""
    time_exchange: dt.datetime = msgspec.field()
    r"""The exchange time of the quote trade."""
    time_coinapi: dt.datetime = msgspec.field()
    r"""The CoinAPI time when the quote trade was received."""
    ask_price: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The best asking price."""
    ask_size: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume resting on the best ask. If the value is equal to zero, then the size is unknown."""
    bid_price: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The best bidding price."""
    bid_size: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume resting on the best bid. If the value is equal to zero, then the size is unknown."""
    last_trade: V1LastTrade = msgspec.field()
    r"""Represents the last executed transaction."""

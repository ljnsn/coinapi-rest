"""Trade."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1Trade(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a trade executed on the exchange."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier."""
    time_exchange: dt.datetime = msgspec.field()
    r"""The time of trade reported by the exchange."""
    time_coinapi: dt.datetime = msgspec.field()
    r"""The time when the trade was received by CoinAPI."""
    uuid: str = msgspec.field()
    r"""The unique identifier for the trade."""
    price: float = msgspec.field()
    r"""The price of the transaction."""
    size: float = msgspec.field()
    r"""The base asset amount traded in the transaction."""
    taker_side: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The aggressor side of the transaction (BUY/SELL/BUY_ESTIMATED/SELL_ESTIMATED/UNKNOWN)."""
    id_trade: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The trade identifier."""
    id_order_maker: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The order maker identifier."""
    id_order_taker: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The order taker identifier."""

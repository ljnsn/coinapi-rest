"""Order book."""

from __future__ import annotations

import datetime as dt
from typing import Any

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1OrderBook(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an order book with additional information and functionality."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier."""
    time_exchange: dt.datetime = msgspec.field()
    r"""The exchange time of the order book."""
    time_coinapi: dt.datetime = msgspec.field()
    r"""The CoinAPI time when the order book was received."""
    asks: Any | None | msgspec.UnsetType = msgspec.field(default=msgspec.UNSET)
    r"""The asks made by market makers."""
    bids: Any | None | msgspec.UnsetType = msgspec.field(default=msgspec.UNSET)
    r"""The bids made by market makers."""

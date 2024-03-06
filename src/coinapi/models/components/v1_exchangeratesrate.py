"""Exchange rates rate."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1ExchangeRatesRate(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    r"""Represents an exchange rate within a collection of exchange rates."""

    time: dt.datetime = msgspec.field()
    r"""Gets or sets the time of the exchange rate."""
    asset_id_quote: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the quote asset ID of the exchange rate."""
    rate: float = msgspec.field()
    r"""Gets or sets the exchange rate value."""


class V1ExchangeRates(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a collection of exchange rates."""

    asset_id_base: str = msgspec.field()
    r"""Gets or sets the base asset ID of the exchange rates."""
    rates: list[V1ExchangeRatesRate] = msgspec.field(default_factory=list)
    r"""Gets or sets the exchange rates."""

"""Exchange rate timeseries item."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalDatetimeOrUnset, OptionalFloatOrUnset


class V1ExchangeRatesTimeseriesItem(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    r"""Represents an item in the exchange rate timeseries."""

    time_period_start: dt.datetime = msgspec.field()
    r"""Gets or sets the start time of the period."""
    time_period_end: dt.datetime = msgspec.field()
    r"""Gets or sets the end time of the period."""
    time_open: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the opening time of the period."""
    time_close: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the closing time of the period."""
    rate_open: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the opening rate for the period."""
    rate_high: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the highest rate for the period."""
    rate_low: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the lowest rate for the period."""
    rate_close: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the closing rate for the period."""

"""Timeseries item."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalDatetimeOrUnset, OptionalFloatOrUnset


class V1TimeseriesItem(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a timeseries item with price and volume information."""

    time_period_start: dt.datetime = msgspec.field()
    r"""The start time of the time period."""
    time_period_end: dt.datetime = msgspec.field()
    r"""The end time of the time period."""
    time_open: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The time when the price opened."""
    time_close: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The time when the price closed."""
    price_open: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The opening price."""
    price_high: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The highest price during the time period."""
    price_low: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The lowest price during the time period."""
    price_close: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The closing price."""
    volume_traded: float = msgspec.field()
    r"""The total volume traded during the time period."""
    trades_count: int = msgspec.field()
    r"""The number of trades executed during the time period."""

"""Index timeseries item."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalDatetimeOrUnset, OptionalFloatOrUnset


class V1IndexTimeseriesItem(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    r"""Represents a timeseries item with value information."""

    time_period_start: dt.datetime = msgspec.field()
    r"""The start time of the time period."""
    time_period_end: dt.datetime = msgspec.field()
    r"""The end time of the time period."""
    time_open: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The time when the value opened."""
    time_close: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The time when the value closed."""
    value_open: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The opening value."""
    value_high: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The highest value during the time period."""
    value_low: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The lowest value during the time period."""
    value_close: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The closing value."""
    value_count: int = msgspec.field()
    r"""The number of values during the time period."""

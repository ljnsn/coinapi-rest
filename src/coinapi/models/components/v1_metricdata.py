"""Metric data."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1MetricData(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a data model for metric data."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the symbol id."""
    time: dt.datetime = msgspec.field()
    r"""Gets or sets the time at which the value is recorded."""
    value: float = msgspec.field()
    r"""Gets or sets the value of the metric."""

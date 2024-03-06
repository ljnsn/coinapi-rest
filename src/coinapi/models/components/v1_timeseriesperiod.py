"""Timeseries period."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalIntOrUnset, OptionalStrOrUnset


class V1TimeseriesPeriod(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a timeseries period used in exchange rate data."""

    period_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The period ID."""
    length_seconds: int = msgspec.field()
    r"""The length of the period in seconds."""
    length_months: int = msgspec.field()
    r"""The length of the period in months."""
    unit_count: OptionalIntOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The unit count."""
    unit_name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The unit name."""
    display_name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The display name of the timeseries period."""

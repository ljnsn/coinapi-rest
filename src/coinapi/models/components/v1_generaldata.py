"""General data."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import (
    OptionalDatetimeOrUnset,
    OptionalFloatOrUnset,
    OptionalStrOrUnset,
)


class V1GeneralData(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Class representation of general metric data. This class is an XML type with name 'general_data' and inherits from the BaseCsvModel class."""

    entry_time: dt.datetime = msgspec.field()
    r"""Gets or sets the entry time for the data point."""
    recv_time: dt.datetime = msgspec.field()
    r"""Gets or sets the received time for the data point."""
    exchange_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the identifier for the exchange."""
    asset_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the identifier for the asset."""
    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the identifier for the symbol."""
    metric_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the identifier for the metric."""
    value_decimal: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the decimal value for the metric."""
    value_text: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the textual representation of the value for the metric."""
    value_time: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the timestamp value for the metric."""

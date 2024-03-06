"""Exchange."""

from __future__ import annotations

import msgspec

from coinapi.models.components.v1_icon import V1Icon
from coinapi.utils.aliases import (
    OptionalDatetimeOrUnset,
    OptionalFloatOrUnset,
    OptionalIntOrUnset,
    OptionalStrOrUnset,
)


class V1Exchange(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an exchange."""

    exchange_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the exchange ID."""
    website: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the website URL of the exchange."""
    name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the name of the exchange."""
    data_start: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    data_end: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    data_quote_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the start date of quote data."""
    data_quote_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the end date of quote data."""
    data_orderbook_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the start date of order book data."""
    data_orderbook_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the end date of order book data."""
    data_trade_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the start date of trade data."""
    data_trade_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the end date of trade data."""
    data_trade_count: OptionalIntOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the number of trades."""
    data_symbols_count: OptionalIntOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the number of symbols."""
    volume_1hrs_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 hour."""
    volume_1day_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 day."""
    volume_1mth_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 month."""
    metric_id: list[str] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the list of metric IDs."""
    icons: list[V1Icon] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the list of icons for the exchange."""

"""Asset."""

from __future__ import annotations

from typing import Literal

import msgspec

from coinapi.utils.aliases import (
    OptionalDatetimeOrUnset,
    OptionalFloatOrUnset,
    OptionalIntOrUnset,
    OptionalStrOrUnset,
)


class V1Asset(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an asset."""

    asset_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the asset ID."""
    name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the name of the asset."""
    type_is_crypto: Literal[0, 1] = msgspec.field()
    r"""Gets or sets a value indicating whether the asset is a cryptocurrency."""
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
    data_symbols_count: OptionalIntOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the number of symbols."""
    volume_1hrs_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 hour."""
    volume_1day_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 day."""
    volume_1mth_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD volume in the last 1 month."""
    price_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the USD price of the asset."""
    id_icon: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the ID of the icon for the asset."""
    supply_current: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the current supply of the asset."""
    supply_total: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the total supply of the asset."""
    supply_max: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the maximum supply of the asset."""
    data_start: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    data_end: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)

"""Symbol mapping."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalFloatOrUnset, OptionalStrOrUnset


class V1SymbolMapping(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents symbol mapping information for exchange symbols."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol ID."""
    symbol_id_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The exchange-specific symbol ID."""
    asset_id_base_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The exchange-specific base asset ID."""
    asset_id_quote_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The exchange-specific quote asset ID."""
    asset_id_base: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The base asset ID."""
    asset_id_quote: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The quote asset ID."""
    price_precision: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The price precision."""
    size_precision: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The size precision."""

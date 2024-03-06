"""Listing item."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1ListingItem(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a listing item."""

    metric_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the metric ID."""
    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the symbol ID."""
    symbol_id_external: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the symbol ID from the exchange."""
    exchange_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the exchange ID."""
    asset_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the asset ID."""
    asset_id_external: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the asset ID from the exchange."""
    chain_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the chain id."""
    network_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the network id."""

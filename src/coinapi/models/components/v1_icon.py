"""Icons."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1Icon(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an icon."""

    exchange_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the exchange ID associated with the icon."""
    asset_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the asset ID associated with the icon."""
    url: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the URL of the icon."""

"""Index."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1Index(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an index."""

    index_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the index ID associated with the index."""
    name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the name associated with the index."""
    description: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the descripion of the index."""

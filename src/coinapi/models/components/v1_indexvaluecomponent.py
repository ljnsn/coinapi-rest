"""Index value component."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1IndexValueComponent(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    """Index value component."""

    component_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    component_value: float = msgspec.field()

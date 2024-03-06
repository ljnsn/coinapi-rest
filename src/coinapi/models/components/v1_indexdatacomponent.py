"""Index data component."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1IndexDataComponent(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    """Index data component."""

    component_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    evaluation_method: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    evaluation_method_parameters: (
        dict[
            str,
            str,
        ]
        | None
        | msgspec.UnsetType
    ) = msgspec.field(default=msgspec.UNSET)

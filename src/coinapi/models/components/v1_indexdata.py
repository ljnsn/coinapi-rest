"""Index data."""

from __future__ import annotations

import msgspec

from coinapi.models.components.v1_indexdatacomponent import V1IndexDataComponent
from coinapi.utils.aliases import OptionalBoolOrUnset, OptionalStrOrUnset


class V1IndexData(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a data model for index data."""

    index_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the index ID associated with the index."""
    name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the name associated with the index."""
    description: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the descripion of the index."""
    index_method: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the index method."""
    index_method_parameters: dict[str, str] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the parameters of the index method."""
    period_recalculation: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the period recalculation of the index."""
    visibility_public: OptionalBoolOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the visibility public of the index."""
    notify_emails: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the notify emails of the index."""
    components: list[V1IndexDataComponent] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the components of the index."""

"""Index data response."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1IndexDataResponse(
    msgspec.Struct,
    kw_only=True,
    frozen=True,
    omit_defaults=True,
):
    """Index data response."""

    index_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    status: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)

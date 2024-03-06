"""Index value."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.models.components.v1_indexvaluecomponent import V1IndexValueComponent


class V1IndexValue(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    """Index value."""

    timestamp: dt.datetime = msgspec.field()
    value: float = msgspec.field()
    composition: list[V1IndexValueComponent] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )

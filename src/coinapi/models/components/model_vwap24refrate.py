"""VWAP24 Ref Rate."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class ModelVwap24RefRate(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    """VWAP24 Ref Rate."""

    time: dt.datetime = msgspec.field()
    asset: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    rate: float = msgspec.field()
    volume: float = msgspec.field()

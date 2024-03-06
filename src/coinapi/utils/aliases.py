"""Utility types."""

import datetime as dt

import msgspec

OptionalStrOrUnset = str | None | msgspec.UnsetType
OptionalIntOrUnset = int | None | msgspec.UnsetType
OptionalFloatOrUnset = float | None | msgspec.UnsetType
OptionalDatetimeOrUnset = dt.datetime | None | msgspec.UnsetType
OptionalBoolOrUnset = bool | None | msgspec.UnsetType

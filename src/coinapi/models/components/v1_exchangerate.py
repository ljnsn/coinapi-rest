"""Exchange rate."""

from __future__ import annotations

import datetime as dt

import msgspec

from coinapi.models.components.model_vwap24refrate import ModelVwap24RefRate
from coinapi.utils.aliases import OptionalStrOrUnset


class V1ExchangeRate(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents an exchange rate."""

    time: dt.datetime = msgspec.field()
    r"""Gets or sets the time of the exchange rate."""
    asset_id_base: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the base asset ID of the exchange rate."""
    asset_id_quote: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the quote asset ID of the exchange rate."""
    rate: float = msgspec.field()
    r"""Gets or sets the exchange rate value."""
    src_side_base: list[ModelVwap24RefRate] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the VWAP24 reference rates for the base asset."""
    src_side_quote: list[ModelVwap24RefRate] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Gets or sets the VWAP24 reference rates for the quote asset."""

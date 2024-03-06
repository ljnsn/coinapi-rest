"""Symbol."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import (
    OptionalBoolOrUnset,
    OptionalDatetimeOrUnset,
    OptionalFloatOrUnset,
    OptionalStrOrUnset,
)


class V1Symbol(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a symbol data model."""

    symbol_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier."""
    exchange_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The exchange identifier."""
    symbol_type: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol type."""
    asset_id_base: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The base asset identifier."""
    asset_id_quote: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The quote asset identifier."""
    asset_id_unit: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The unit asset identifier."""
    future_contract_unit: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The contract unit for futures."""
    future_contract_unit_asset: OptionalStrOrUnset = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""The asset used as the unit for futures contract."""
    future_delivery_time: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The future delivery time for futures contract."""
    option_type_is_call: OptionalBoolOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Indicates whether the option type is a call."""
    option_strike_price: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The strike price for options."""
    option_contract_unit: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The contract unit for options."""
    option_exercise_style: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The exercise style for options."""
    option_expiration_time: OptionalDatetimeOrUnset = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""The expiration time for options."""
    contract_delivery_time: OptionalDatetimeOrUnset = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""The delivery time for contracts."""
    contract_unit: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The contract unit for contracts."""
    contract_unit_asset: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The asset used as the unit for contracts."""
    contract_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The contract identifier."""
    contract_display_name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The display name of the contract."""
    contract_display_description: OptionalStrOrUnset = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""The display description of the contract."""
    data_start: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    data_end: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    data_quote_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The start date of quote data."""
    data_quote_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The end date of quote data."""
    data_orderbook_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The start date of order book data."""
    data_orderbook_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The end date of order book data."""
    data_trade_start: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The start date of trade data."""
    data_trade_end: OptionalDatetimeOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The end date of trade data."""
    index_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The index identifier."""
    index_display_name: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The display name of the index."""
    index_display_description: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The display description of the index."""
    volume_1hrs: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in the last 1 hour."""
    volume_1hrs_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in USD in the last 1 hour."""
    volume_1day: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in the last 1 day."""
    volume_1day_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in USD in the last 1 day."""
    volume_1mth: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in the last 1 month."""
    volume_1mth_usd: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The volume in USD in the last 1 month."""
    price: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The price."""
    symbol_id_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The symbol identifier in the exchange."""
    asset_id_base_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The base asset identifier in the exchange."""
    asset_id_quote_exchange: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The quote asset identifier in the exchange."""
    price_precision: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The price precision."""
    size_precision: OptionalFloatOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""The size precision."""
    raw_kvp: dict[str, str] | None | msgspec.UnsetType = msgspec.field(
        default=msgspec.UNSET,
    )
    r"""Not normalized raw kvp data."""

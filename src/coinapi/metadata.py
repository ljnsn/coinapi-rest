"""Metadata module."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class Metadata(Base):
    r"""Metadata controller."""

    def get_v1_assets(
        self,
        filter_asset_id: str | None = None,
        include_supply: bool | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1AssetsResponse:
        r"""List all assets.

        Retrieves all assets.

        :::info
        Our asset identifiers are aligned with the ISO 4217 currency codes standard only for fiat money (government or law regulated currency).
        :::

        :::info
        Properties of the output are providing aggregated information from across all symbols related to the specific asset. If you need to calculate your aggregation (e.g., limiting only the particular type of symbols), you should use /v1/symbols endpoint as a data source.
        :::
        """
        return self._make_request(
            "get_/v1/assets",
            operations.GetV1AssetsRequest(
                filter_asset_id=filter_asset_id,
                include_supply=include_supply,
            ),
            operations.GetV1AssetsResponse,
            accept_header_override,
        )

    def get_v1_assets_asset_id(
        self,
        asset_id: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1AssetsAssetIDResponse:
        r"""List all assets by asset ID."""
        return self._make_request(
            "get_/v1/assets/{asset_id}",
            operations.GetV1AssetsAssetIDRequest(asset_id=asset_id),
            operations.GetV1AssetsAssetIDResponse,
            accept_header_override,
        )

    def get_v1_assets_icons(
        self,
        size: int,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1AssetsIconsSizeResponse:
        r"""List all asset icons.

        Gets the list of icons (of the given size) for all the assets.
        """
        return self._make_request(
            "get_/v1/assets/icons/{size}",
            operations.GetV1AssetsIconsSizeRequest(size=size),
            operations.GetV1AssetsIconsSizeResponse,
            accept_header_override,
        )

    def get_v1_exchanges(
        self,
        filter_exchange_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1ExchangesResponse:
        r"""List all exchanges.

        Get a detailed list of exchanges provided by the system.

        :::info
        Properties of the output are providing aggregated information from across all symbols related to the specific exchange. If you need to calculate your aggregation (e.g., limiting only the particular type of symbols), you should use /v1/symbols endpoint as a data source.
        :::
        """
        return self._make_request(
            "get_/v1/exchanges",
            operations.GetV1ExchangesRequest(filter_exchange_id=filter_exchange_id),
            operations.GetV1ExchangesResponse,
            accept_header_override,
        )

    def get_v1_exchanges_exchange_id(
        self,
        exchange_id: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1ExchangesExchangeIDResponse:
        r"""List all exchanges by exchange_id."""
        return self._make_request(
            "get_/v1/exchanges/{exchange_id}",
            operations.GetV1ExchangesExchangeIDRequest(exchange_id=exchange_id),
            operations.GetV1ExchangesExchangeIDResponse,
            accept_header_override,
        )

    def get_v1_exchanges_icons(
        self,
        size: int,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1ExchangesIconsSizeResponse:
        r"""List of icons for the exchanges."""
        return self._make_request(
            "get_/v1/exchanges/icons/{size}",
            operations.GetV1ExchangesIconsSizeRequest(size=size),
            operations.GetV1ExchangesIconsSizeResponse,
            accept_header_override,
        )

    def get_v1_metadata(self) -> operations.GetV1MetadataResponse:
        r"""Base url of the API."""
        return self._make_request(
            "get_/v1/metadata",
            operations.GetV1MetadataRequest(),
            operations.GetV1MetadataResponse,
            accept_header_override=AcceptEnum.ANY,
        )

    def get_v1_symbols(
        self,
        filter_symbol_id: str | None = None,
        filter_exchange_id: str | None = None,
        filter_asset_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1SymbolsResponse:
        r"""List all symbols.

        Retrieves all symbols with optional filtering.

        :::info
        \"price_precision\" and \"size_precision\" are data precisions and are not always the same precisions used for trading eg. for the \"BINANCE\" exchanges.
        :::

        :::info
        You should not assume that the market data will be always within the resolution provided by the \"price_precision\" and \"size_precision\". The fact that the precision values can be derived from a posterior implies the fact that this data could be delayed, also it can be changed by the data source without notice and we will immediately deliver data with the new precision while could not update the precision values in this endpoint immediately.
        :::

        ### Symbol identifier

        Our symbol identifier is created using a pattern that depends on symbol type.

        Type | `symbol_id` pattern
        --------- | ---------
        SPOT | `{exchange_id}_SPOT_{asset_id_base}_{asset_id_quote}`
        FUTURES | `{exchange_id}_FTS_{asset_id_base}_{asset_id_quote}_{YYMMDD of future_delivery_time}`
        OPTION | `{exchange_id}_OPT_{asset_id_base}_{asset_id_quote}_{YYMMDD of option_expiration_time}_{option_strike_price}_{option_type_is_call as C/P}`
        PERPETUAL | `{exchange_id}_PERP_{asset_id_base}_{asset_id_quote}`
        INDEX | `{exchange_id}_IDX_{index_id}`
        CREDIT | `{exchange_id}_CRE_{asset_id_base}`
        CONTACT  | `{exchange_id}_COT_{contract_id}`

        :::info
        In the unlikely event when the \"symbol_id\" for more than one market is the same. We will append the additional term (prefixed with the \"_\") at the end of the duplicated identifiers to differentiate them.
        :::info

        ### Symbol types list (enumeration of `symbol_type` output variable)

        Type | Name | Description
        -------- | - | -----------
        SPOT | FX Spot | Agreement to exchange one asset for another one *(e.g. Buy BTC for USD)*
        FUTURES | Futures contract | FX Spot derivative contract where traders agree to trade fx spot at predetermined future time
        OPTION | Option contract | FX Spot derivative contract where traders agree to trade right to require buy or sell of fx spot at agreed price on exercise date
        PERPETUAL | Perpetual contract | FX Spot derivative contract where traders agree to trade fx spot continously without predetermined future delivery time
        INDEX | Index | Statistical composite that measures changes in the economy or markets.
        CREDIT | Credit/Funding | Margin funding contract. Order book displays lending offers and borrow bids. Price represents the daily rate.
        CONTRACT | Contract | Represents other types of financial instruments *(e.g. spreads, interest rate swap)*

        ### Additional output variables for `symbol_type = INDEX`

        Variable | Description
        --------- | -----------
        index_id | Index identifier
        index_display_name | Human readable name of the index *(optional)*
        index_display_description | Description of the index *(optional)*

        ### Additional output variables for `symbol_type = FUTURES`

        Variable | Description
        --------- | -----------
        future_delivery_time | Predetermined time of futures contract delivery date in ISO 8601
        future_contract_unit | Contact size *(eg. 10 BTC if `future_contract_unit` = `10` and `future_contract_unit_asset` = `BTC`)*
        future_contract_unit_asset | Identifier of the asset used to denominate the contract unit

        ### Additional output variables for `symbol_type = PERPETUAL`

        Variable | Description
        --------- | -----------
        future_contract_unit | Contact size *(eg. 10 BTC if `future_contract_unit` = `10` and `future_contract_unit_asset` = `BTC`)*
        future_contract_unit_asset | Identifier of the asset used to denominate the contract unit

        ### Additional output variables for `symbol_type = OPTION`

        Variable | Description
        --------- | -----------
        option_type_is_call | Boolean value representing option type. `true` for Call options, `false` for Put options
        option_strike_price | Price at which option contract can be exercised
        option_contract_unit | Base asset amount of underlying spot which single option represents
        option_exercise_style | Option exercise style. Can be `EUROPEAN` or `AMERICAN`
        option_expiration_time | Option contract expiration time in ISO 8601

        ### Additional output variables for `symbol_type = CONTRACT`

        Variable | Description
        --------- | -----------
        contract_delivery_time | Predetermined time of contract delivery date in ISO 8601
        contract_unit | Contact size *(eg. 10 BTC if `contract_unit` = `10` and `contract_unit_asset` = `BTC`)*
        contract_unit_asset | Identifier of the asset used to denominate the contract unit
        contract_id | Identifier of contract by the exchange
        """
        return self._make_request(
            "get_/v1/symbols",
            operations.GetV1SymbolsRequest(
                filter_symbol_id=filter_symbol_id,
                filter_exchange_id=filter_exchange_id,
                filter_asset_id=filter_asset_id,
            ),
            operations.GetV1SymbolsResponse,
            accept_header_override,
        )

    def get_v1_symbols_map_exchange_id(
        self,
        exchange_id: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1SymbolsMapExchangeIDResponse:
        r"""List symbol mapping for the exchange."""
        return self._make_request(
            "get_/v1/symbols/map/{exchange_id}",
            operations.GetV1SymbolsMapExchangeIDRequest(exchange_id=exchange_id),
            operations.GetV1SymbolsMapExchangeIDResponse,
            accept_header_override,
        )

    def get_v1_symbols_exchange_id(
        self,
        exchange_id: str,
        filter_symbol_id: str | None = None,
        filter_asset_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1SymbolsExchangeIDResponse:
        r"""List of symbols for the exchange."""
        return self._make_request(
            "get_/v1/symbols/{exchange_id}",
            operations.GetV1SymbolsExchangeIDRequest(
                exchange_id=exchange_id,
                filter_symbol_id=filter_symbol_id,
                filter_asset_id=filter_asset_id,
            ),
            operations.GetV1SymbolsExchangeIDResponse,
            accept_header_override,
        )

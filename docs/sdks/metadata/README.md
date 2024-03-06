# Metadata
(*metadata*)

## Overview

<span data-status-page="28923"></span>

### Available Operations

* [get_v1_assets](#get_v1_assets) - List all assets
* [get_v1_assets_asset_id](#get_v1_assets_asset_id) - List all assets by asset ID
* [get_v1_assets_icons](#get_v1_assets_icons) - List all asset icons
* [get_v1_exchanges](#get_v1_exchanges) - List all exchanges
* [get_v1_exchanges_exchange_id](#get_v1_exchanges_exchange_id) - List all exchanges by exchange_id
* [get_v1_exchanges_icons](#get_v1_exchanges_icons) - List of icons for the exchanges
* [get_v1_metadata](#get_v1_metadata) - Base url of the API.
* [get_v1_symbols](#get_v1_symbols) - List all symbols
* [get_v1_symbols_map_exchange_id](#get_v1_symbols_map_exchange_id) - List symbol mapping for the exchange
* [get_v1_symbols_exchange_id](#get_v1_symbols_exchange_id) - List of symbols for the exchange

## get_v1_assets

Retrieves all assets.
            
:::info
Our asset identifiers are aligned with the ISO 4217 currency codes standard only for fiat money (government or law regulated currency).
:::
            
:::info
Properties of the output are providing aggregated information from across all symbols related to the specific asset. If you need to calculate your aggregation (e.g., limiting only the particular type of symbols), you should use /v1/symbols endpoint as a data source.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `filter_asset_id`                                                                                  | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Comma or semicolon delimited asset identifiers used to filter response. (optional, eg. `BTC;ETH`). |
| `include_supply`                                                                                   | *Optional[bool]*                                                                                   | :heavy_minus_sign:                                                                                 | Flag indicating whether to include supply information.                                             |


### Response

**[operations.GetV1AssetsResponse](../../models/operations/getv1assetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_assets_asset_id

List all assets by asset ID

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_assets_asset_id(asset_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `asset_id`         | *str*              | :heavy_check_mark: | The asset ID.      |


### Response

**[operations.GetV1AssetsAssetIDResponse](../../models/operations/getv1assetsassetidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_assets_icons

Gets the list of icons (of the given size) for all the assets.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_assets_icons(size=202791)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `size`                 | *int*                  | :heavy_check_mark:     | The size of the icons. |


### Response

**[operations.GetV1AssetsIconsSizeResponse](../../models/operations/getv1assetsiconssizeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_exchanges

Get a detailed list of exchanges provided by the system.
            
:::info
Properties of the output are providing aggregated information from across all symbols related to the specific exchange. If you need to calculate your aggregation (e.g., limiting only the particular type of symbols), you should use /v1/symbols endpoint as a data source.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_exchanges(filter_exchange_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `filter_exchange_id`                                                                                         | *Optional[str]*                                                                                              | :heavy_minus_sign:                                                                                           | Comma or semicolon delimited exchange identifiers used to filter response. (optional, eg. `BITSTAMP;GEMINI`) |


### Response

**[operations.GetV1ExchangesResponse](../../models/operations/getv1exchangesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_exchanges_exchange_id

List all exchanges by exchange_id

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_exchanges_exchange_id(exchange_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `exchange_id`           | *str*                   | :heavy_check_mark:      | The ID of the exchange. |


### Response

**[operations.GetV1ExchangesExchangeIDResponse](../../models/operations/getv1exchangesexchangeidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_exchanges_icons

List of icons for the exchanges

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_exchanges_icons(size=6673)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `size`                 | *int*                  | :heavy_check_mark:     | The size of the icons. |


### Response

**[operations.GetV1ExchangesIconsSizeResponse](../../models/operations/getv1exchangesiconssizeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_metadata

Base url of the API.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_metadata()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetV1MetadataResponse](../../models/operations/getv1metadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_symbols

Retrieves all symbols with optional filtering.
            
:::info
"price_precision" and "size_precision" are data precisions and are not always the same precisions used for trading eg. for the "BINANCE" exchanges.
:::
            
:::info
You should not assume that the market data will be always within the resolution provided by the "price_precision" and "size_precision". The fact that the precision values can be derived from a posterior implies the fact that this data could be delayed, also it can be changed by the data source without notice and we will immediately deliver data with the new precision while could not update the precision values in this endpoint immediately.
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
In the unlikely event when the "symbol_id" for more than one market is the same. We will append the additional term (prefixed with the "_") at the end of the duplicated identifiers to differentiate them.
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

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_symbols(filter_symbol_id='<value>', filter_exchange_id='<value>', filter_asset_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `filter_symbol_id`                                                                                                              | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | Comma or semicolon delimited parts of symbol identifier used to filter response. (optional, eg. `BITSTAMP`_ or `BINANCE_SPOT_`) |
| `filter_exchange_id`                                                                                                            | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The filter for exchange ID.                                                                                                     |
| `filter_asset_id`                                                                                                               | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | The filter for asset ID.                                                                                                        |


### Response

**[operations.GetV1SymbolsResponse](../../models/operations/getv1symbolsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_symbols_map_exchange_id

List symbol mapping for the exchange

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_symbols_map_exchange_id(exchange_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `exchange_id`                                           | *str*                                                   | :heavy_check_mark:                                      | The ID of the exchange (from the Metadata -> Exchanges) |


### Response

**[operations.GetV1SymbolsMapExchangeIDResponse](../../models/operations/getv1symbolsmapexchangeidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_symbols_exchange_id

List of symbols for the exchange

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.metadata.get_v1_symbols_exchange_id(exchange_id='<value>', filter_symbol_id='<value>',
                                            filter_asset_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `exchange_id`                                           | *str*                                                   | :heavy_check_mark:                                      | The ID of the exchange (from the Metadata -> Exchanges) |
| `filter_symbol_id`                                      | *Optional[str]*                                         | :heavy_minus_sign:                                      | The filter for symbol ID.                               |
| `filter_asset_id`                                       | *Optional[str]*                                         | :heavy_minus_sign:                                      | The filter for asset ID.                                |


### Response

**[operations.GetV1SymbolsExchangeIDResponse](../../models/operations/getv1symbolsexchangeidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

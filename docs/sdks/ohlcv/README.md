# Ohlcv
(*ohlcv*)

## Overview


<span data-status-page="28926"></span>

API calls described in this section are related to downloading OHLCV *(Open, High, Low, Close, Volume)* timeseries data.
Each data point of this timeseries represents several indicators calculated from transactions activity inside a time range (period).

:::info
OHLCV data primary purpose is to present an overview of the market in human readable form. 
It's often used to visualize market data on charts, websites, and various kinds of reports.
:::

:::tip
CoinAPI expanded the standard OHLCV timeseries by including time of first and last trade and amount of trades executed inside period.
:::
    

### Available Operations

* [get_v1_ohlcv_periods](#get_v1_ohlcv_periods) - [ohlcv] List all periods
* [get_v1_ohlcv_symbol_id_history](#get_v1_ohlcv_symbol_id_history) - [ohlcv] Historical data
* [get_v1_ohlcv_exchanges_exchange_id_history](#get_v1_ohlcv_exchanges_exchange_id_history) - [ohlcv] Historical data by exchange
* [get_v1_ohlcv_symbol_id_latest](#get_v1_ohlcv_symbol_id_latest) - [ohlcv] Latest data

## get_v1_ohlcv_periods

Get full list of supported time periods available for requesting OHLCV timeseries data.
            
### Available periods
            
Time unit | Period identifiers
--------- | -----------
Second | 1SEC, 2SEC, 3SEC, 4SEC, 5SEC, 6SEC, 10SEC, 15SEC, 20SEC, 30SEC
Minute | 1MIN, 2MIN, 3MIN, 4MIN, 5MIN, 6MIN, 10MIN, 15MIN, 20MIN, 30MIN
Hour | 1HRS, 2HRS, 3HRS, 4HRS, 6HRS, 8HRS, 12HRS
Day | 1DAY, 2DAY, 3DAY, 5DAY, 7DAY, 10DAY
Month | 1MTH, 2MTH, 3MTH, 4MTH, 6MTH
Year | 1YRS, 2YRS, 3YRS, 4YRS, 5YRS
            
:::tip
You can assume that we will not remove any periods from this response, however, we may add new ones.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ohlcv.get_v1_ohlcv_periods()

if res.content is not None:
    # handle response
    pass
```


### Response

**[operations.GetV1OhlcvPeriodsResponse](../../models/operations/getv1ohlcvperiodsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_ohlcv_symbol_id_history

Get OHLCV timeseries data returned in time ascending order. Data can be requested by the period and for the specific symbol eg `BITSTAMP_SPOT_BTC_USD`, if you need to query timeseries by asset pairs eg. `BTC/USD`, then please reffer to the Exchange Rates Timeseries data
            
:::info
The OHLCV Historical endpoint data can be delayed a few seconds. Use OHLCV Latest endpoint to get real-time data without delay.
:::

### Example Usage

```python
import coinapi
from coinapi.models import operations

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetV1OhlcvSymbolIDHistoryRequest(
    symbol_id='<value>',
)

res = s.ohlcv.get_v1_ohlcv_symbol_id_history(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetV1OhlcvSymbolIDHistoryRequest](../../models/operations/getv1ohlcvsymbolidhistoryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetV1OhlcvSymbolIDHistoryResponse](../../models/operations/getv1ohlcvsymbolidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_ohlcv_exchanges_exchange_id_history

Get OHLCV timeseries data returned in time ascending order. Data can be requested by the period and for the specific exchange eg `BITSTAMP`
            
:::info
The OHLCV Historical endpoint data can be delayed a few seconds.
`time_start` and `time_end` must point to the same day
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ohlcv.get_v1_ohlcv_exchanges_exchange_id_history(exchange_id='<value>', period_id='<value>', time_start='<value>', time_end='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `exchange_id`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | Exchange identifier of requested timeseries (from the Metadata -> Exchanges) |
| `period_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | Identifier of requested timeseries period (e.g. `5SEC` or `2MTH`)            |
| `time_start`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Timeseries starting time in ISO 8601                                         |
| `time_end`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | Timeseries ending time in ISO 8601                                           |


### Response

**[operations.GetV1OhlcvExchangesExchangeIDHistoryResponse](../../models/operations/getv1ohlcvexchangesexchangeidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_ohlcv_symbol_id_latest

Get OHLCV latest timeseries data returned in time descending order. Data can be requested by the period and for the specific symbol eg `BITSTAMP_SPOT_BTC_USD`, if you need to query timeseries by asset pairs eg. `BTC/USD`, then please reffer to the Exchange Rates Timeseries data
            
:::info
OHLCV Latest endpoint is providing real-time data without delay. The OHLCV Historical endpoint data can be delayed a few seconds.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ohlcv.get_v1_ohlcv_symbol_id_latest(symbol_id='<value>', period_id='<value>', limit=100, include_empty_items=False)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol_id`                                                                                                                                                                  | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Symbol identifier of requested timeseries (from the Metadata -> Symbols)                                                                                                     |
| `period_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Identifier of requested timeseries period (required, e.g. `5SEC` or `2MTH`)                                                                                                  |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |
| `include_empty_items`                                                                                                                                                        | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Include items with no activity? (optional, default value is `false`, possible values are `true` or `false`)                                                                  |


### Response

**[operations.GetV1OhlcvSymbolIDLatestResponse](../../models/operations/getv1ohlcvsymbolidlatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

# ExchangeRates
(*exchange_rates*)

## Overview


<span data-status-page="28924"></span>
Exchange rate is defined as (VWAP-24H) last 24 hour (rolling window over time) Volume Weighted Average Price across multiple data sources listed on our platform. We are selecting and managing the data sources that are used in the calculation based on multiple factors to provide data of highest quality. 

Algorithm is described below:

  1. Exchange rates are produced from quotes, trades, and metadata datasets.
  1. Symbols that are not data_type = "SPOT" are excluded from the calculation.
  1. Symbols from the data sources that were marked by us as not legitimate are excluded from the calculation.
  1. Quotes data where the spread is outside the range of ```<0$; 67%>``` are discarded. `spreadPrc = (ask - bid) / ((ask + bid) / 2)`
  1. The midpoint from the quote data is used as a pricing reference and it's weighted by the passive cumulative volume resting on the best prices.
  1. Volume from the trades is used to weight the midpoint prices in the VWAP24 algorithm.
  1. Midpoint data that has not been updated in the last 5 minutes and 1 second is discarded.
  1. The last 24-hour volume for each symbol is updated every 4 hours when approximately 20% of the data in the sliding window changes (also, the list of eligible markets is updated at the same time).
  1. Everywhere in the algorithm below, we are using asset pairs only from exchanges that have the highest legitimacy rank, and the rest of the exchanges are discarded. As we establish the highest-ranking exchanges that have this data for each asset pair, we ensure that the highest quality data is used for each of them. The rank used for asset pairing is carried over to the following steps.
  1. Every 1 second, we update VWAP24 data for every asset pair across all data sources.
  1. For each asset pair, we also discard data that is outside the 3 sigma range if there are at least 3 exchanges for this asset pair.
  1. From the VWAP24 data, we are creating a tree structure where node/vertex = asset and edge = rate.
  1. By traversing the tree structure using the BFS algorithm and our secret sauce, we are able to establish the final exchange rates.
    

### Available Operations

* [get_v1_specific_rate](#get_v1_specific_rate) - [exchange rates] Get specific rate
* [get_v1_base_rates](#get_v1_base_rates) - [exchange rates] Get all current rates
* [get_v1_history_periods](#get_v1_history_periods) - [exchange rates] Timeseries periods
* [get_v1_pair_history](#get_v1_pair_history) - [exchange rates] Timeseries data

## get_v1_specific_rate

Retrieves the exchange rate for a specific base and quote asset at a given time or the current rate.
            
:::info
If you are using an exchange rate for mission-critical operations, then for best reliability, you should measure the difference between current time and the time returned from the response to ensure that value of the difference between those meets your internal requirements.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.exchange_rates.get_v1_specific_rate(asset_id_base='<value>', asset_id_quote='<value>', time='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `asset_id_base`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | Requested exchange rate base asset identifier (from the Metadata -> Assets)                         |
| `asset_id_quote`                                                                                    | *str*                                                                                               | :heavy_check_mark:                                                                                  | Requested exchange rate quote asset identifier (from the Metadata -> Assets)                        |
| `time`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Time at which exchange rate is calculated (optional, if not supplied then current rate is returned) |


### Response

**[operations.GetV1SpecificRateResponse](../../models/operations/getv1specificrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_base_rates

Get the current exchange rate between requested asset and all other assets.
            
:::info
If you are using an exchange rate for mission-critical operations, then for best reliability, you should measure the difference between current time and the time returned from the response to ensure that value of the difference between those meets your internal requirements.
:::
            
:::info
You can invert the rates by using Y = 1 / X equation, for example BTC/USD = 1 / (USD/BTC);
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.exchange_rates.get_v1_base_rates(asset_id_base='<value>', filter_asset_id='<value>', invert=False,
                                         time='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id_base`                                                                                                                         | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | Requested exchange rates base asset identifier (from the Metadata -> Assets)                                                            |
| `filter_asset_id`                                                                                                                       | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Comma or semicolon delimited asset identifiers used to filter response (optional)                                                       |
| `invert`                                                                                                                                | *Optional[bool]*                                                                                                                        | :heavy_minus_sign:                                                                                                                      | True will invert all the rates (optional, if true then rates will be calculated as `rate = 1 / actual_rate` eg. `USD/BTC` as `BTC/USD`) |
| `time`                                                                                                                                  | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Time for historical rates (optional)                                                                                                    |


### Response

**[operations.GetV1BaseRatesResponse](../../models/operations/getv1baseratesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_history_periods

You can also obtain historical exchange rates of any asset pair, grouped into time periods.
Get full list of supported time periods available for requesting exchange rates historical timeseries data.
            
## Timeseries periods
Time unit |	Period identifiers
--- | ---
Second | 1SEC, 2SEC, 3SEC, 4SEC, 5SEC, 6SEC, 10SEC, 15SEC, 20SEC, 30SEC
Minute | 1MIN, 2MIN, 3MIN, 4MIN, 5MIN, 6MIN, 10MIN, 15MIN, 20MIN, 30MIN
Hour | 1HRS, 2HRS, 3HRS, 4HRS, 6HRS, 8HRS, 12HRS
Day | 1DAY, 2DAY, 3DAY, 5DAY, 7DAY, 10DAY

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.exchange_rates.get_v1_history_periods()

if res.content is not None:
    # handle response
    pass
```


### Response

**[operations.GetV1HistoryPeriodsResponse](../../models/operations/getv1historyperiodsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_pair_history

Get the historical exchange rates between two assets in the form of the timeseries.

### Example Usage

```python
import coinapi
from coinapi.models import operations

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetV1PairHistoryRequest(
    asset_id_base='<value>',
    asset_id_quote='<value>',
)

res = s.exchange_rates.get_v1_pair_history(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetV1PairHistoryRequest](../../models/operations/getv1pairhistoryrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetV1PairHistoryResponse](../../models/operations/getv1pairhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

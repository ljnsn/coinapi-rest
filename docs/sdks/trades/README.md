# Trades
(*trades*)

## Overview

Controller for retrieving trade data related to executed transactions.

### Available Operations

* [get_v1_trades_symbol_id_history](#get_v1_trades_symbol_id_history) - [trades] Historical data
* [get_v1_trades_symbol_id_latest](#get_v1_trades_symbol_id_latest) - [trades] Latest data by symbol_id
* [get_v1_trades_latest](#get_v1_trades_latest) - [trades] Latest data

## get_v1_trades_symbol_id_history

Get history transactions from specific symbol, returned in time ascending order.

### Example Usage

```python
import coinapi
from coinapi.models import operations

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetV1TradesSymbolIDHistoryRequest(
    symbol_id='<value>',
)

res = s.trades.get_v1_trades_symbol_id_history(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetV1TradesSymbolIDHistoryRequest](../../models/operations/getv1tradessymbolidhistoryrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetV1TradesSymbolIDHistoryResponse](../../models/operations/getv1tradessymbolidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_trades_symbol_id_latest

Get latest trades executed up to 1 minute ago. Latest data is always returned in time descending order.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.trades.get_v1_trades_symbol_id_latest(symbol_id='<value>', limit=100, include_id=False)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol_id`                                                                                                                                                                  | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Symbol identifier for requested timeseries (from the Metadata -> Symbols)                                                                                                    |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |
| `include_id`                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Information that additional exchange trade identifier should be included in the `id_trade` parameter of the trade if exchange providing identifiers.                         |


### Response

**[operations.GetV1TradesSymbolIDLatestResponse](../../models/operations/getv1tradessymbolidlatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_trades_latest

Get latest trades executed up to 1 minute ago. Latest data is always returned in time descending order.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.trades.get_v1_trades_latest(filter_symbol_id='<value>', include_id=False, limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_symbol_id`                                                                                                                                                           | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Comma or semicolon delimited parts of symbol identifier used to filter response. (optional)                                                                                  |
| `include_id`                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Information that additional exchange trade identifier should be included in the `id_trade` parameter of the trade if exchange providing identifiers.                         |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |


### Response

**[operations.GetV1TradesLatestResponse](../../models/operations/getv1tradeslatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

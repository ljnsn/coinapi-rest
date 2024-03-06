# Quotes
(*quotes*)

## Overview

Controller for retrieving quotes data, also known as quotes or passive level 1 data.

### Available Operations

* [get_v1_quotes_symbol_id_history](#get_v1_quotes_symbol_id_history) - [quotes] Historical data
* [get_v1_quotes_current](#get_v1_quotes_current) - [quotes] Current data
* [get_v1_quotes_symbol_id_current](#get_v1_quotes_symbol_id_current) - [quotes] Current quotes for a specific symbol
* [get_v1_quotes_latest](#get_v1_quotes_latest) - [quotes] Latest data
* [get_v1_quotes_symbol_id_latest](#get_v1_quotes_symbol_id_latest) - [quotes] Latest quote updates for a specific symbol

## get_v1_quotes_symbol_id_history

Get historical quote updates within requested time range, returned in time ascending order.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.quotes.get_v1_quotes_symbol_id_history(symbol_id='<value>', time_start='<value>', time_end='<value>', limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol_id`                                                                                                                                                                  | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Symbol identifier for requested timeseries (from the Metadata -> Symbols)                                                                                                    |
| `time_start`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Starting time in ISO 8601 (required)                                                                                                                                         |
| `time_end`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Timeseries ending time in ISO 8601 (optional, if not supplied then the data is returned to the end or when result elements count reaches the limit)                          |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, minimum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |


### Response

**[operations.GetV1QuotesSymbolIDHistoryResponse](../../models/operations/getv1quotessymbolidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_quotes_current

Get current quotes for all symbols or for a specific symbol.
            
:::info
When requesting current data for a specific symbol, output is not encapsulated into JSON array as only one item is returned.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.quotes.get_v1_quotes_current(filter_symbol_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `filter_symbol_id`                                                                          | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Comma or semicolon delimited parts of symbol identifier used to filter response. (optional) |


### Response

**[operations.GetV1QuotesCurrentResponse](../../models/operations/getv1quotescurrentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_quotes_symbol_id_current

[quotes] Current quotes for a specific symbol

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.quotes.get_v1_quotes_symbol_id_current(symbol_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `symbol_id`                                          | *str*                                                | :heavy_check_mark:                                   | The symbol identifier (from the Metadata -> Symbols) |


### Response

**[operations.GetV1QuotesSymbolIDCurrentResponse](../../models/operations/getv1quotessymbolidcurrentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_quotes_latest

Get latest updates of the quotes up to 1 minute ago. Latest data is always returned in time descending order.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.quotes.get_v1_quotes_latest(filter_symbol_id='<value>', limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_symbol_id`                                                                                                                                                           | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Comma or semicolon delimited parts of symbol identifier used to filter response. (optional)                                                                                  |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |


### Response

**[operations.GetV1QuotesLatestResponse](../../models/operations/getv1quoteslatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_quotes_symbol_id_latest

[quotes] Latest quote updates for a specific symbol

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.quotes.get_v1_quotes_symbol_id_latest(symbol_id='<value>', limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol_id`                                                                                                                                                                  | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Symbol identifier of requested timeseries (from the Metadata -> Symbols)                                                                                                     |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |


### Response

**[operations.GetV1QuotesSymbolIDLatestResponse](../../models/operations/getv1quotessymbolidlatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

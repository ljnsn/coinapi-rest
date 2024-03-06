# OrderBook
(*order_book*)

## Overview


<span data-status-page="28929"></span>
This section describes calls related to order book data, also known as books or passive level 2 data.

:::info
When requesting current data for a specific symbol, output is not encapsulated into JSON array as only one item is returned.
:::

:::info
GET `/v1/orderbooks/current` endpoint is charged one request per 100 data points returned after applying a filter defined by filter_symbol_id parameter. If filter symbols target more than one exchange, error is returned.
:::

:::info
When requesting current order book data limited to a single level, then quotes are actually used. This information is important from the perspective that quotes data could be faster than order book data (behavior is dependent solely one the data source) and they can have the size equal to 0 when the size is unknown. Some data sources publish order books and separately quote data (without the sizes) at a higher frequency. In that case, we will merge the order book feed with quotes feed to make sure that our updates are as fast as possible. The quotes will have the size equal to 0 as the value is unknown and the customer can decide if these higher frequency updates without the sizes are valuable or if not then can discard them or ask for at least 2 order book levels (in case of a REST API call). For the data sources that publish order books only or order books and quotes with the sizes then this will not happen.
:::

### Available Operations

* [get_v1_orderbooks_symbol_id_depth_current](#get_v1_orderbooks_symbol_id_depth_current) - [order book] Current depth of the order book
* [get_v1_orderbooks_symbol_id_history](#get_v1_orderbooks_symbol_id_history) - [order book] Historical data
* [get_v1_orderbooks_symbol_id_current](#get_v1_orderbooks_symbol_id_current) - Get current order book
* [get_v1_orderbooks_symbol_id_latest](#get_v1_orderbooks_symbol_id_latest) - [order book] Latest data

## get_v1_orderbooks_symbol_id_depth_current

Retrieves the current depth of the order book for the specified symbol.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.order_book.get_v1_orderbooks_symbol_id_depth_current(symbol_id='<value>', limit_levels=550087)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `symbol_id`                                              | *str*                                                    | :heavy_check_mark:                                       | The symbol ID (from the Metadata -> Symbols)             |
| `limit_levels`                                           | *Optional[int]*                                          | :heavy_minus_sign:                                       | The maximum number of levels to include in the response. |


### Response

**[operations.GetV1OrderbooksSymbolIDDepthCurrentResponse](../../models/operations/getv1orderbookssymboliddepthcurrentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_orderbooks_symbol_id_history

Get historical order book snapshots for a specific symbol within time range, returned in time ascending order.
            
:::info
The historical order book data via the REST API is currently limited by a number of updates and to the maximum number of 20 levels.
:::

### Example Usage

```python
import coinapi
from coinapi.models import operations

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetV1OrderbooksSymbolIDHistoryRequest(
    symbol_id='<value>',
)

res = s.order_book.get_v1_orderbooks_symbol_id_history(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetV1OrderbooksSymbolIDHistoryRequest](../../models/operations/getv1orderbookssymbolidhistoryrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetV1OrderbooksSymbolIDHistoryResponse](../../models/operations/getv1orderbookssymbolidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_orderbooks_symbol_id_current

Retrieves the current order book for the specified symbol.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.order_book.get_v1_orderbooks_symbol_id_current(symbol_id='<value>', limit_levels=967320)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `symbol_id`                                              | *str*                                                    | :heavy_check_mark:                                       | The symbol ID (from the Metadata -> Symbols)             |
| `limit_levels`                                           | *Optional[int]*                                          | :heavy_minus_sign:                                       | The maximum number of levels to include in the response. |


### Response

**[operations.GetV1OrderbooksSymbolIDCurrentResponse](../../models/operations/getv1orderbookssymbolidcurrentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_orderbooks_symbol_id_latest

Get latest order book snapshots for a specific symbol, returned in time descending order.
            
:::info
The historical order book data via the REST API is currently limited by a number of updates and to the maximum number of 20 levels.
:::

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.order_book.get_v1_orderbooks_symbol_id_latest(symbol_id='<value>', limit=100, limit_levels=126677)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol_id`                                                                                                                                                                  | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Symbol identifier of requested timeseries (from the Metadata -> Symbols)                                                                                                     |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Amount of items to return (optional, mininum is 1, maximum is 100000, default value is 100, if the parameter is used then every 100 output items are counted as one request) |
| `limit_levels`                                                                                                                                                               | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Maximum amount of levels from each side of the book to include in response (optional)                                                                                        |


### Response

**[operations.GetV1OrderbooksSymbolIDLatestResponse](../../models/operations/getv1orderbookssymbolidlatestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

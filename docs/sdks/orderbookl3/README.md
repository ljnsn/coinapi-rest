# OrderBookL3
(*order_book_l3*)

## Overview


<span data-status-page="28929"></span>
This section describes calls related to order book data, also known as books or passive level 3 data.

### Available Operations

* [get_v1_orderbooks3_current](#get_v1_orderbooks3_current) - [order book l3] Current order books
* [get_v1_orderbooks3_symbol_id_current](#get_v1_orderbooks3_symbol_id_current) - [order book l3] Current order book by symbol_id

## get_v1_orderbooks3_current

[order book l3] Current order books

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.order_book_l3.get_v1_orderbooks3_current(filter_symbol_id='<value>', limit_levels=555267)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `filter_symbol_id`                                                                   | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Comma or semicolon delimited parts of symbol identifier used to filter the response. |
| `limit_levels`                                                                       | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | The maximum number of levels to include in the response.                             |


### Response

**[operations.GetV1Orderbooks3CurrentResponse](../../models/operations/getv1orderbooks3currentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_orderbooks3_symbol_id_current

Retrieves the current order book for the specified symbol.

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.order_book_l3.get_v1_orderbooks3_symbol_id_current(symbol_id='<value>', limit_levels=838831)

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

**[operations.GetV1Orderbooks3SymbolIDCurrentResponse](../../models/operations/getv1orderbooks3symbolidcurrentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

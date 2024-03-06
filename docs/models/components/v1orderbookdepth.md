# V1OrderBookDepth

Represents the depth of an order book.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `symbol_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The symbol identifier.                                               |
| `time_exchange`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The exchange time of the order book.                                 |
| `time_coinapi`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The CoinAPI time when the order book was received.                   |
| `ask_levels`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The number of ask levels in the order book.                          |
| `bid_levels`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The number of bid levels in the order book.                          |
| `ask_depth`                                                          | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The depth of the ask side of the order book.                         |
| `bid_depth`                                                          | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The depth of the bid side of the order book.                         |
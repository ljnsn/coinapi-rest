# V1LastTrade

Represents the last executed transaction.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `time_exchange`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The exchange time of the last trade.                                 |
| `time_coinapi`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The CoinAPI time when the last trade was received.                   |
| `uuid`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The UUID of the last trade.                                          |
| `price`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The price of the last trade.                                         |
| `size`                                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The size of the last trade.                                          |
| `taker_side`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The taker side of the last trade.                                    |
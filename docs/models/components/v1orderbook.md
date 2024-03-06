# V1OrderBook

Represents an order book with additional information and functionality.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `symbol_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The symbol identifier.                                               |
| `time_exchange`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The exchange time of the order book.                                 |
| `time_coinapi`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The CoinAPI time when the order book was received.                   |
| `asks`                                                               | *Optional[Any]*                                                      | :heavy_minus_sign:                                                   | The asks made by market makers.                                      |
| `bids`                                                               | *Optional[Any]*                                                      | :heavy_minus_sign:                                                   | The bids made by market makers.                                      |
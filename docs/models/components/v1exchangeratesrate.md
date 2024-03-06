# V1ExchangeRatesRate

Represents an exchange rate within a collection of exchange rates.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the time of the exchange rate.                          |
| `asset_id_quote`                                                     | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the quote asset ID of the exchange rate.                |
| `rate`                                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the exchange rate value.                                |
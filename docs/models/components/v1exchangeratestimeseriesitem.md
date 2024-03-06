# V1ExchangeRatesTimeseriesItem

Represents an item in the exchange rate timeseries.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `time_period_start`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the start time of the period.                           |
| `time_period_end`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the end time of the period.                             |
| `time_open`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the opening time of the period.                         |
| `time_close`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the closing time of the period.                         |
| `rate_open`                                                          | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the opening rate for the period.                        |
| `rate_high`                                                          | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the highest rate for the period.                        |
| `rate_low`                                                           | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the lowest rate for the period.                         |
| `rate_close`                                                         | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the closing rate for the period.                        |
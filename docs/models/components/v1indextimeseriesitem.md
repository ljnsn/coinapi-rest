# V1IndexTimeseriesItem

Represents a timeseries item with value information.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `time_period_start`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The start time of the time period.                                   |
| `time_period_end`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The end time of the time period.                                     |
| `time_open`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time when the value opened.                                      |
| `time_close`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time when the value closed.                                      |
| `value_open`                                                         | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The opening value.                                                   |
| `value_high`                                                         | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The highest value during the time period.                            |
| `value_low`                                                          | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The lowest value during the time period.                             |
| `value_close`                                                        | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | The closing value.                                                   |
| `value_count`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The number of values during the time period.                         |
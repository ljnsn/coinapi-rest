# V1GeneralData

Class representation of general metric data. This class is an XML type with name 'general_data' and inherits from the BaseCsvModel class.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `entry_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the entry time for the data point.                      |
| `recv_time`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the received time for the data point.                   |
| `exchange_id`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the identifier for the exchange.                        |
| `asset_id`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the identifier for the asset.                           |
| `symbol_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the identifier for the symbol.                          |
| `metric_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the identifier for the metric.                          |
| `value_decimal`                                                      | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the decimal value for the metric.                       |
| `value_text`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the textual representation of the value for the metric. |
| `value_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the timestamp value for the metric.                     |
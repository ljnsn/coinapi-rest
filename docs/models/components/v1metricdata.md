# V1MetricData

Represents a data model for metric data.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `symbol_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Gets or sets the symbol id.                                          |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Gets or sets the time at which the value is recorded.                |
| `value`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Gets or sets the value of the metric.                                |
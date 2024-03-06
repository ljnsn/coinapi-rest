# GetV1OhlcvExchangesExchangeIDHistoryRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `exchange_id`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | Exchange identifier of requested timeseries (from the Metadata -> Exchanges) |
| `period_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | Identifier of requested timeseries period (e.g. `5SEC` or `2MTH`)            |
| `time_start`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Timeseries starting time in ISO 8601                                         |
| `time_end`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | Timeseries ending time in ISO 8601                                           |
# GetV1BaseRatesRequest


## Fields

| Field                                                                                                                                   | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id_base`                                                                                                                         | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | Requested exchange rates base asset identifier (from the Metadata -> Assets)                                                            |
| `filter_asset_id`                                                                                                                       | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Comma or semicolon delimited asset identifiers used to filter response (optional)                                                       |
| `invert`                                                                                                                                | *Optional[bool]*                                                                                                                        | :heavy_minus_sign:                                                                                                                      | True will invert all the rates (optional, if true then rates will be calculated as `rate = 1 / actual_rate` eg. `USD/BTC` as `BTC/USD`) |
| `time`                                                                                                                                  | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Time for historical rates (optional)                                                                                                    |
# GetV1SymbolsExchangeIDRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `exchange_id`                                           | *str*                                                   | :heavy_check_mark:                                      | The ID of the exchange (from the Metadata -> Exchanges) |
| `filter_symbol_id`                                      | *Optional[str]*                                         | :heavy_minus_sign:                                      | The filter for symbol ID.                               |
| `filter_asset_id`                                       | *Optional[str]*                                         | :heavy_minus_sign:                                      | The filter for asset ID.                                |
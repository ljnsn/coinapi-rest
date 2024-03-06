# V1SymbolMapping

Represents symbol mapping information for exchange symbols.


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `symbol_id`                           | *Optional[str]*                       | :heavy_minus_sign:                    | The symbol ID.                        |
| `symbol_id_exchange`                  | *Optional[str]*                       | :heavy_minus_sign:                    | The exchange-specific symbol ID.      |
| `asset_id_base_exchange`              | *Optional[str]*                       | :heavy_minus_sign:                    | The exchange-specific base asset ID.  |
| `asset_id_quote_exchange`             | *Optional[str]*                       | :heavy_minus_sign:                    | The exchange-specific quote asset ID. |
| `asset_id_base`                       | *Optional[str]*                       | :heavy_minus_sign:                    | The base asset ID.                    |
| `asset_id_quote`                      | *Optional[str]*                       | :heavy_minus_sign:                    | The quote asset ID.                   |
| `price_precision`                     | *Optional[float]*                     | :heavy_minus_sign:                    | The price precision.                  |
| `size_precision`                      | *Optional[float]*                     | :heavy_minus_sign:                    | The size precision.                   |
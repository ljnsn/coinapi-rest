# GetV1MetricsAssetListingRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `metric_id`                                          | *Optional[str]*                                      | :heavy_minus_sign:                                   | Metric identifier (from the Metrics -> Listing)      |
| `exchange_id`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | Exchange identifier (from the Metadata -> Exchanges) |
| `chain_id`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Chain identifier                                     |
| `network_id`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | Network identifier                                   |
| `asset_id`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Asset identifier (from the Metadata -> Assets)       |
| `asset_id_external`                                  | *Optional[str]*                                      | :heavy_minus_sign:                                   | The asset external identifier                        |
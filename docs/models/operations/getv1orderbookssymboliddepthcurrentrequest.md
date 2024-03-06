# GetV1OrderbooksSymbolIDDepthCurrentRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `symbol_id`                                              | *str*                                                    | :heavy_check_mark:                                       | The symbol ID (from the Metadata -> Symbols)             |
| `limit_levels`                                           | *Optional[int]*                                          | :heavy_minus_sign:                                       | The maximum number of levels to include in the response. |
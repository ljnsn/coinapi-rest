# CoinAPI REST

[![Coverage Status](https://coveralls.io/repos/github/ljnsn/coinapi-rest/badge.svg?branch=ci/coveralls)](https://coveralls.io/github/ljnsn/coinapi-rest?branch=ci/coveralls)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/v/coinapi-rest)](https://pypi.python.org/pypi/coinapi-rest)
[![image](https://img.shields.io/pypi/pyversions/coinapi-rest.svg)](https://pypi.python.org/pypi/coinapi-rest)

## Installation

```bash
pip install coinapi-rest
```

## Example Usage

### Example

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```

## Available Resources and Operations

### [metadata](docs/sdks/metadata/README.md)

* [get_v1_assets](docs/sdks/metadata/README.md#get_v1_assets) - List all assets
* [get_v1_assets_asset_id](docs/sdks/metadata/README.md#get_v1_assets_asset_id) - List all assets by asset ID
* [get_v1_assets_icons](docs/sdks/metadata/README.md#get_v1_assets_icons) - List all asset icons
* [get_v1_exchanges](docs/sdks/metadata/README.md#get_v1_exchanges) - List all exchanges
* [get_v1_exchanges_exchange_id](docs/sdks/metadata/README.md#get_v1_exchanges_exchange_id) - List all exchanges by exchange_id
* [get_v1_exchanges_icons](docs/sdks/metadata/README.md#get_v1_exchanges_icons) - List of icons for the exchanges
* [get_v1_metadata](docs/sdks/metadata/README.md#get_v1_metadata) - Base url of the API.
* [get_v1_symbols](docs/sdks/metadata/README.md#get_v1_symbols) - List all symbols
* [get_v1_symbols_map_exchange_id](docs/sdks/metadata/README.md#get_v1_symbols_map_exchange_id) - List symbol mapping for the exchange
* [get_v1_symbols_exchange_id](docs/sdks/metadata/README.md#get_v1_symbols_exchange_id) - List of symbols for the exchange

### [exchange_rates](docs/sdks/exchangerates/README.md)

* [get_v1_specific_rate](docs/sdks/exchangerates/README.md#get_v1_specific_rate) - [exchange rates] Get specific rate
* [get_v1_base_rates](docs/sdks/exchangerates/README.md#get_v1_base_rates) - [exchange rates] Get all current rates
* [get_v1_history_periods](docs/sdks/exchangerates/README.md#get_v1_history_periods) - [exchange rates] Timeseries periods
* [get_v1_pair_history](docs/sdks/exchangerates/README.md#get_v1_pair_history) - [exchange rates] Timeseries data

### [indexes](docs/sdks/indexes/README.md)

* [get_v1_indexes](docs/sdks/indexes/README.md#get_v1_indexes) - List of available indexes
* [post_v1_indexes_json](docs/sdks/indexes/README.md#post_v1_indexes_json) - Create index
* [get_v1_indexes_index_id_](docs/sdks/indexes/README.md#get_v1_indexes_index_id_) - Get index data
* [put_v1_indexes_index_id_json](docs/sdks/indexes/README.md#put_v1_indexes_index_id_json) - Update index
* [get_v1_indexes_index_id_history](docs/sdks/indexes/README.md#get_v1_indexes_index_id_history) - Retrieve Historical Index Value and Composition
* [get_v1_indexes_index_id_timeseries](docs/sdks/indexes/README.md#get_v1_indexes_index_id_timeseries) - Retrieve Historical Index Value Timeseries
* [get_v1_indexes_index_id_timeseries_to_be_announced](docs/sdks/indexes/README.md#get_v1_indexes_index_id_timeseries_to_be_announced) - Retrieve Historical Composition Value Timeseries
Retrieves historical timeseries for the specific composition value for an index

### [metrics](docs/sdks/metrics/README.md)

* [get_v1_metrics_listing](docs/sdks/metrics/README.md#get_v1_metrics_listing) - Listing of all supported metrics by CoinAPI
* [get_v1_metrics_exchange_listing](docs/sdks/metrics/README.md#get_v1_metrics_exchange_listing) - Listing of all supported exchange metrics
* [get_v1_metrics_exchange_current](docs/sdks/metrics/README.md#get_v1_metrics_exchange_current) - Current metrics for given exchange
* [get_v1_metrics_exchange_history](docs/sdks/metrics/README.md#get_v1_metrics_exchange_history) - Historical metrics for the exchange
* [get_v1_metrics_symbol_listing](docs/sdks/metrics/README.md#get_v1_metrics_symbol_listing) - Listing of all supported metrics for symbol
* [get_v1_metrics_symbol_current](docs/sdks/metrics/README.md#get_v1_metrics_symbol_current) - Current metrics for given symbol
* [get_v1_metrics_symbol_history](docs/sdks/metrics/README.md#get_v1_metrics_symbol_history) - Historical metrics for symbol
* [get_v1_metrics_asset_listing](docs/sdks/metrics/README.md#get_v1_metrics_asset_listing) - Listing of all supported metrics for asset
* [get_v1_metrics_asset_current](docs/sdks/metrics/README.md#get_v1_metrics_asset_current) - Current metrics for given asset
* [get_v1_metrics_asset_history](docs/sdks/metrics/README.md#get_v1_metrics_asset_history) - Historical metrics for asset

### [order_book](docs/sdks/orderbook/README.md)

* [get_v1_orderbooks_symbol_id_depth_current](docs/sdks/orderbook/README.md#get_v1_orderbooks_symbol_id_depth_current) - [order book] Current depth of the order book
* [get_v1_orderbooks_symbol_id_history](docs/sdks/orderbook/README.md#get_v1_orderbooks_symbol_id_history) - [order book] Historical data
* [get_v1_orderbooks_symbol_id_current](docs/sdks/orderbook/README.md#get_v1_orderbooks_symbol_id_current) - Get current order book
* [get_v1_orderbooks_symbol_id_latest](docs/sdks/orderbook/README.md#get_v1_orderbooks_symbol_id_latest) - [order book] Latest data

### [order_book_l3](docs/sdks/orderbookl3/README.md)

* [get_v1_orderbooks3_current](docs/sdks/orderbookl3/README.md#get_v1_orderbooks3_current) - [order book l3] Current order books
* [get_v1_orderbooks3_symbol_id_current](docs/sdks/orderbookl3/README.md#get_v1_orderbooks3_symbol_id_current) - [order book l3] Current order book by symbol_id

### [quotes](docs/sdks/quotes/README.md)

* [get_v1_quotes_symbol_id_history](docs/sdks/quotes/README.md#get_v1_quotes_symbol_id_history) - [quotes] Historical data
* [get_v1_quotes_current](docs/sdks/quotes/README.md#get_v1_quotes_current) - [quotes] Current data
* [get_v1_quotes_symbol_id_current](docs/sdks/quotes/README.md#get_v1_quotes_symbol_id_current) - [quotes] Current quotes for a specific symbol
* [get_v1_quotes_latest](docs/sdks/quotes/README.md#get_v1_quotes_latest) - [quotes] Latest data
* [get_v1_quotes_symbol_id_latest](docs/sdks/quotes/README.md#get_v1_quotes_symbol_id_latest) - [quotes] Latest quote updates for a specific symbol

### [ohlcv](docs/sdks/ohlcv/README.md)

* [get_v1_ohlcv_periods](docs/sdks/ohlcv/README.md#get_v1_ohlcv_periods) - [ohlcv] List all periods
* [get_v1_ohlcv_symbol_id_history](docs/sdks/ohlcv/README.md#get_v1_ohlcv_symbol_id_history) - [ohlcv] Historical data
* [get_v1_ohlcv_exchanges_exchange_id_history](docs/sdks/ohlcv/README.md#get_v1_ohlcv_exchanges_exchange_id_history) - [ohlcv] Historical data by exchange
* [get_v1_ohlcv_symbol_id_latest](docs/sdks/ohlcv/README.md#get_v1_ohlcv_symbol_id_latest) - [ohlcv] Latest data

### [trades](docs/sdks/trades/README.md)

* [get_v1_trades_symbol_id_history](docs/sdks/trades/README.md#get_v1_trades_symbol_id_history) - [trades] Historical data
* [get_v1_trades_symbol_id_latest](docs/sdks/trades/README.md#get_v1_trades_symbol_id_latest) - [trades] Latest data by symbol_id
* [get_v1_trades_latest](docs/sdks/trades/README.md#get_v1_trades_latest) - [trades] Latest data

## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

### Example

```python
import coinapi
from coinapi.models import errors

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = None
try:
    res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)
except errors.CoinAPIError as e:
    # handle exception
    raise (e)

if res.content is not None:
    # handle response
    pass
```

## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://rest.coinapi.io` | None |

#### Example

```python
import coinapi

s = coinapi.CoinAPI(
    server_idx=0,
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import coinapi

s = coinapi.CoinAPI(
    server_url="https://rest.coinapi.io",
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```

## Custom HTTP Client

The CoinAPI SDK makes API calls using the [httpx](https://pypi.org/project/httpx/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `httpx.Client` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import coinapi
import httpx

http_client = httpx.Client(headers={'x-custom-header': 'someValue'})
s = coinapi.CoinAPI(api_key="<YOUR_API_KEY_HERE>", client=http_client)
```

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```

# Indexes
(*indexes*)

## Overview

Indexes section of the API is in the Alpha release cycle. Use only for testing, evaluaton and feedback.

### Available Operations

* [get_v1_indexes](#get_v1_indexes) - List of available indexes
* [post_v1_indexes_json](#post_v1_indexes_json) - Create index
* [get_v1_indexes_index_id](#get_v1_indexes_index_id) - Get index data
* [put_v1_indexes_index_id_json](#put_v1_indexes_index_id_json) - Update index
* [get_v1_indexes_index_id_history](#get_v1_indexes_index_id_history) - Retrieve Historical Index Value and Composition
* [get_v1_indexes_index_id_timeseries](#get_v1_indexes_index_id_timeseries) - Retrieve Historical Index Value Timeseries
* [get_v1_indexes_index_id_timeseries_to_be_announced](#get_v1_indexes_index_id_timeseries_to_be_announced) - Retrieve Historical Composition Value Timeseries
Retrieves historical timeseries for the specific composition value for an index

## get_v1_indexes

List of available indexes

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.indexes.get_v1_indexes()

if res.content is not None:
    # handle response
    pass
```


### Response

**[operations.GetV1IndexesResponse](../../models/operations/getv1indexesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## post_v1_indexes_json

Create index

### Example Usage

```python
import coinapi
from coinapi.models import components

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = components.V1IndexData()

res = s.indexes.post_v1_indexes_json(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.V1IndexData](../../models/components/v1indexdata.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.PostV1IndexesJSONResponse](../../models/operations/postv1indexesjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_indexes_index_id

Get index data

### Example Usage

```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.indexes.get_v1_indexes_index_id(index_id='<value>')

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `index_id`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetV1IndexesIndexIDResponse](../../models/operations/getv1indexesindexidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## put_v1_indexes_index_id_json

Update index

### Example Usage

```python
import coinapi
from coinapi.models import components

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.indexes.put_v1_indexes_index_id_json(index_id='<value>', v1_index_data=components.V1IndexData())

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `index_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `v1_index_data`                                                            | [Optional[components.V1IndexData]](../../models/components/v1indexdata.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.PutV1IndexesIndexIDJSONResponse](../../models/operations/putv1indexesindexidjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_indexes_index_id_history

Retrieve Historical Index Value and Composition

### Example Usage

```python
import coinapi
import dateutil.parser

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.indexes.get_v1_indexes_index_id_history(index_id='<value>', time_start=dateutil.parser.isoparse('2024-10-21T14:08:54.780Z'), time_end=dateutil.parser.isoparse('2022-08-14T15:13:35.032Z'), limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `index_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `time_start`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `time_end`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.GetV1IndexesIndexIDHistoryResponse](../../models/operations/getv1indexesindexidhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_indexes_index_id_timeseries

Retrieve Historical Index Value Timeseries

### Example Usage

```python
import coinapi
import dateutil.parser

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.indexes.get_v1_indexes_index_id_timeseries(index_id='<value>', time_start=dateutil.parser.isoparse('2022-09-29T06:10:23.640Z'), time_end=dateutil.parser.isoparse('2022-11-21T03:10:01.688Z'), limit=100)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `index_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `time_start`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `time_end`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.GetV1IndexesIndexIDTimeseriesResponse](../../models/operations/getv1indexesindexidtimeseriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

## get_v1_indexes_index_id_timeseries_to_be_announced

Retrieve Historical Composition Value Timeseries
Retrieves historical timeseries for the specific composition value for an index

### Example Usage

```python
import coinapi
from coinapi.models import operations

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)

req = operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDRequest(
    index_id='<value>',
)

res = s.indexes.get_v1_indexes_index_id_timeseries_to_be_announced(req)

if res.content is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDRequest](../../models/operations/getv1indexesindexidtimeseriestobeannouncedrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDResponse](../../models/operations/getv1indexesindexidtimeseriestobeannouncedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.CoinAPIError | 4x-5xx          | */*             |

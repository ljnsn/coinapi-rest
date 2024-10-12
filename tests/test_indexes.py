"""Tests for indexes requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import components, operations


@pytest.mark.vcr
def test_get_v1_indexes(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_indexes_listing."""
    response = coinapi.indexes.get_v1_indexes()

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.skip(reason="Alpha release..")
@pytest.mark.vcr(record_mode="once")
def test_post_v1_indexes(coinapi: CoinAPI) -> None:
    """Test posting an index."""
    request = operations.PostV1IndexesJSONRequest(
        body=components.V1IndexData(index_id="TEST", name="Test Index"),
    )
    response = coinapi.indexes.post_v1_indexes_json(request)

    assert response.status_code == 201


@pytest.mark.vcr
def test_get_v1_indexes_index_id(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_indexes_index_id."""
    response = coinapi.indexes.get_v1_indexes_index_id("TEST_IDX14_VWAP")

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.skip(reason="Alpha release..")
def test_put_v1_indexes(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test put_v1_indexes_index_id."""
    data = components.V1IndexData(
        index_id="TEST_IDX14_VWAP",
        name="Test Index",
        components=[
            components.V1IndexDataComponent(
                component_id="BTC",
                evaluation_method="Test evaluation method",
                evaluation_method_parameters={"test": "test"},
            ),
        ],
        description="Test index description",
        index_method="Test index method",
        index_method_parameters={"test": "test"},
        period_recalculation="Test period recalculation",
    )
    response = coinapi.indexes.put_v1_indexes_index_id_json("TEST_IDX14_VWAP", data)

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_indexes_history(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test retrieving historical index value and composition."""
    response = coinapi.indexes.get_v1_indexes_index_id_history("TEST_IDX14_VWAP")

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.skip(reason="Alpha release..")
@pytest.mark.vcr
def test_get_v1_indexes_index_id_timeseries(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test retrieving index timeseries."""
    response = coinapi.indexes.get_v1_indexes_index_id_timeseries("TEST_IDX14_VWAP")

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

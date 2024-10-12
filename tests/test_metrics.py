"""Tests for metrics requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import operations


@pytest.mark.vcr
def test_get_v1_metrics(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_metrics."""
    response = coinapi.metrics.get_v1_metrics_listing()

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_metrics_exchange(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_metrics_exchange_listing."""
    response = coinapi.metrics.get_v1_metrics_exchange_listing(exchange_id="KRAKEN")

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.skip(reason="Returns 500")
@pytest.mark.vcr
def test_get_v1_metrics_exchange_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_metrics_exchange_current."""
    response = coinapi.metrics.get_v1_metrics_exchange_current(
        exchange_id="BINANCE",
        metric_id="LIQUIDATION_IS_MATCH",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.skip(reason="What's a valid metric for an exchange?")
@pytest.mark.vcr
def test_get_v1_metrics_exchange_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_metrics_exchange_history."""
    request = operations.GetV1MetricsExchangeHistoryRequest(
        metric_id="LIQUIDATION_IS_MATCH",
        exchange_id="BINANCE",
    )
    response = coinapi.metrics.get_v1_metrics_exchange_history(request)

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_metrics_symbol_listing(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_metrics_symbol_listing."""
    response = coinapi.metrics.get_v1_metrics_symbol_listing(exchange_id="BINANCE")

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_metrics_asset_listing(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_metrics_asset_listing."""
    request = operations.GetV1MetricsAssetListingRequest(exchange_id="BINANCE")
    response = coinapi.metrics.get_v1_metrics_asset_listing(request)

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

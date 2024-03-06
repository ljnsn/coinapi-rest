"""Tests for exchange rates requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import operations


@pytest.mark.vcr()
def test_get_specific_rate(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_specific_rate."""
    response = coinapi.exchange_rates.get_specific_rate(
        asset_id_base="BTC",
        asset_id_quote="USD",
        time="2021-01-01",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr()
def test_get_v1_exchangerate_asset_id_base(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_exchangerate_asset_id_base."""
    response = coinapi.exchange_rates.get_v1_exchangerate_asset_id_base(
        asset_id_base="IOTA",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr()
def test_get_v1_exchangerate_history_periods(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_exchangerate_history_periods."""
    response = coinapi.exchange_rates.get_v1_exchangerate_history_periods()

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr()
def test_get_v1_exchangerate_asset_id_base_asset_id_quote_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting exchange rate history between two assets."""
    request = operations.GetV1ExchangerateAssetIDBaseAssetIDQuoteHistoryRequest(
        asset_id_base="BTC",
        asset_id_quote="USD",
        period_id="1DAY",
        limit=10,
    )
    response = (
        coinapi.exchange_rates.get_v1_exchangerate_asset_id_base_asset_id_quote_history(
            request,
        )
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

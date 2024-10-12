"""Tests for quote requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI


@pytest.mark.vcr
def test_get_v1_quotes_symbol_id_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_quotes_symbol_id_history."""
    response = coinapi.quotes.get_v1_quotes_symbol_id_history(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        time_start="2022-01-01T00:00:00",
        time_end="2022-01-02T00:00:00",
        limit=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_quotes_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_quotes_current."""
    response = coinapi.quotes.get_v1_quotes_current(
        filter_symbol_id="KRAKEN_SPOT_BTC_USD,COINBASE_SPOT_BTC_USD",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_quotes_symbol_id_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_quotes_symbol_id_current."""
    response = coinapi.quotes.get_v1_quotes_symbol_id_current(
        symbol_id="KRAKEN_SPOT_BTC_USD",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_quotes_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_quotes_latest."""
    response = coinapi.quotes.get_v1_quotes_latest(
        filter_symbol_id="KRAKEN_SPOT_BTC_USD,COINBASE_SPOT_BTC_USD",
        limit=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_quotes_symbol_id_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_quotes_symbol_id_latest."""
    response = coinapi.quotes.get_v1_quotes_symbol_id_latest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        limit=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

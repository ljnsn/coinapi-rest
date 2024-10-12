"""Tests for OHLCV requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import operations


@pytest.mark.vcr
def test_get_v1_ohlcv_periods(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test for get_v1_ohlcv_periods."""
    response = coinapi.ohlcv.get_v1_ohlcv_periods()

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_ohlcv_symbol_id_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_ohlcv_symbol_id_history."""
    request = operations.GetV1OhlcvSymbolIDHistoryRequest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        period_id="1DAY",
        time_start="2021-01-01T00:00:00",
        time_end="2021-01-05T00:00:00",
    )
    response = coinapi.ohlcv.get_v1_ohlcv_symbol_id_history(request)

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_ohlcv_exchanges_exchange_id_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_ohlcv_exchanges_exchange_id_history."""
    response = coinapi.ohlcv.get_v1_ohlcv_exchanges_exchange_id_history(
        exchange_id="KRAKEN",
        period_id="1DAY",
        time_start="2021-01-01T00:00:00",
        time_end="2021-01-01T04:00:00",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_ohlcv_symbol_id_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_ohlcv_symbol_id_latest."""
    response = coinapi.ohlcv.get_v1_ohlcv_symbol_id_latest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        period_id="1DAY",
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

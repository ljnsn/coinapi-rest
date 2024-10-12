"""Tests for trade requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import operations


@pytest.mark.vcr
def test_get_v1_trades_symbol_id_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_trades_symbol_id_history."""
    request = operations.GetV1TradesSymbolIDHistoryRequest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        time_start="2022-01-01T00:00:00",
        time_end="2022-01-02T00:00:00",
        limit=10,
    )
    response = coinapi.trades.get_v1_trades_symbol_id_history(
        request,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_trades_symbol_id_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_trades_symbol_id_latest."""
    response = coinapi.trades.get_v1_trades_symbol_id_latest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        limit=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_trades_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_trades_latest."""
    response = coinapi.trades.get_v1_trades_latest(
        filter_symbol_id="KRAKEN_SPOT_BTC_USD,KRAKEN_SPOT_ETH_USD",
        limit=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

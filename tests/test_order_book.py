"""Tests for order book requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI
from coinapi.models import operations


@pytest.mark.skip(reason="Can't find a symbol that has order book data..")
@pytest.mark.vcr
def test_get_v1_orderbooks_symbol_id_depth_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_orderbooks_symbol_id_depth_current."""
    response = coinapi.order_book.get_v1_orderbooks_symbol_id_depth_current(
        symbol_id="KRAKEN_SPOT_XMR_USDT",
        limit_levels=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_orderbooks_symbol_id_history(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_orderbooks_symbol_id_history."""
    request = operations.GetV1OrderbooksSymbolIDHistoryRequest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        time_start="2021-01-01T00:00:00",
        time_end="2021-01-02T00:00:00",
        limit=10,
    )
    response = coinapi.order_book.get_v1_orderbooks_symbol_id_history(
        request,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_orderbooks_symbol_id_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_orderbooks_symbol_id_current."""
    response = coinapi.order_book.get_v1_orderbooks_symbol_id_current(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        limit_levels=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_orderbooks_symbol_id_latest(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for get_v1_orderbooks_symbol_id_latest."""
    response = coinapi.order_book.get_v1_orderbooks_symbol_id_latest(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        limit=2,
        limit_levels=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

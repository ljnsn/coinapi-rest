"""Tests for order book L3 requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI


@pytest.mark.vcr
def test_get_v1_orderbooks3_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for OrderBookL3.get_v1_orderbooks3_current."""
    response = coinapi.order_book_l3.get_v1_orderbooks3_current(
        filter_symbol_id="KRAKEN_SPOT_BTC_USD,KRAKEN_SPOT_BTC_EUR",
        limit_levels=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot


@pytest.mark.vcr
def test_get_v1_orderbooks3_symbol_id_current(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test for OrderBookL3.get_v1_orderbooks3_symbol_id_current."""
    response = coinapi.order_book_l3.get_v1_orderbooks3_symbol_id_current(
        symbol_id="KRAKEN_SPOT_BTC_USD",
        limit_levels=10,
    )

    assert response.status_code == 200
    assert response.content is not None
    assert response.content == snapshot

"""Tests for metadata requests."""

import pytest
from syrupy.assertion import SnapshotAssertion

from coinapi import CoinAPI


@pytest.mark.vcr
def test_get_v1_assets(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_assets."""
    res = coinapi.metadata.get_v1_assets(filter_asset_id="BTC,XMR")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.vcr
def test_get_v1_asset_id(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_exchanges."""
    res = coinapi.metadata.get_v1_assets_asset_id("BTC")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.network
def test_get_v1_assets_icons(coinapi: CoinAPI) -> None:
    """Test get_v1_asset_icons."""
    # we don't want to store the whole response in the repo, so we don't use vcr here
    res = coinapi.metadata.get_v1_assets_icons(16)

    assert res.content is not None


@pytest.mark.vcr
def test_get_v1_exchanges(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_exchanges."""
    res = coinapi.metadata.get_v1_exchanges("KRAKEN,BINANCE")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.vcr
def test_get_v1_exchange_id(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_exchange_id."""
    res = coinapi.metadata.get_v1_exchanges_exchange_id("KRAKEN")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.network
def test_get_v1_exchange_icons(coinapi: CoinAPI) -> None:
    """Test get_v1_exchange_icons."""
    # we don't want to store the whole response in the repo, so we don't use vcr here
    res = coinapi.metadata.get_v1_exchanges_icons(16)

    assert res.content is not None


@pytest.mark.skip(reason="Returns an error")
def test_get_v1_metadata(coinapi: CoinAPI) -> None:
    """Test get_v1_metadata."""
    res = coinapi.metadata.get_v1_metadata()

    assert res.content is not None


@pytest.mark.vcr
def test_get_v1_symbols(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_symbols."""
    res = coinapi.metadata.get_v1_symbols(filter_asset_id="XMR")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.vcr
def test_get_v1_symbols_map(coinapi: CoinAPI, snapshot: SnapshotAssertion) -> None:
    """Test get_v1_symbols_map."""
    res = coinapi.metadata.get_v1_symbols_map_exchange_id("KRAKEN")

    assert res.content is not None
    assert res.content == snapshot


@pytest.mark.vcr
def test_get_v1_symbols_exchange_id(
    coinapi: CoinAPI,
    snapshot: SnapshotAssertion,
) -> None:
    """Test get_v1_symbols_exchange_id."""
    res = coinapi.metadata.get_v1_symbols_exchange_id("KRAKEN")

    assert res.content is not None
    assert res.content == snapshot

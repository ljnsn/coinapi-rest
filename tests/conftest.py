"""Pytest config."""

import logging
import os
from typing import Any

import pytest
from dotenv import load_dotenv
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from coinapi import CoinAPI

logger = logging.getLogger(__name__)

OBFUSCATED_DATA = "OBFUSCATED"
KEYS_TO_OBFUSCATE = {
    "username",
    "password",
    "secret",
    "api_key",
    "tokenvalue",
    "token",
    "access_token",
    "refresh_token",
}


@pytest.fixture(scope="session", autouse=True)
def _session_start() -> None:
    """Session start."""
    vcr_log = logging.getLogger("vcr")
    vcr_log.setLevel(logging.WARNING)


@pytest.fixture
def api_key() -> str:
    """Load the API key from the environment."""
    load_dotenv()
    return os.environ.get("COINAPI_KEY", "testing")


@pytest.fixture
def coinapi(api_key: str) -> CoinAPI:
    """Return a CoinAPI instance."""
    return CoinAPI(api_key)


@pytest.fixture(scope="package")
def vcr_config(record_mode: str) -> dict[str, Any]:
    """VCR configuration."""
    # Usage: add `@pytest.mark.vcr()` to record and replay all HTTP requests.

    # Record mode:
    # - Use "rewrite" in CI: rewrite all cassettes if they have changed.
    # - Use "none" in CI: only replay cassettes or throw an error if they are missing.
    # - Use "once" locally: record if there is no cassette, and if there is one replay it.

    return {
        "record_mode": record_mode or "none",
        "decode_compressed_response": True,
        # Remove sensitive information [1]. To make these secrets available when running tests, run
        # $ SECRET=swordfish invoke test
        # and access them in Python with `os.environ.get("SECRET")`.
        # [1] https://vcrpy.readthedocs.io/en/latest/advanced.html#filter-sensitive-data-from-the-request
        "filter_headers": [
            ("authorization", OBFUSCATED_DATA),
            ("X-CoinAPI-Key", OBFUSCATED_DATA),
        ],
        "filter_query_parameters": [
            ("apikey", OBFUSCATED_DATA),
            ("password", OBFUSCATED_DATA),
        ],
        "match_on": ["method", "scheme", "host", "port", "path", "query"],
    }


@pytest.fixture
def snapshot_json(snapshot: SnapshotAssertion) -> SnapshotAssertion:
    """Return a snapshot instance for JSON."""
    return snapshot.with_defaults(extension_class=JSONSnapshotExtension)

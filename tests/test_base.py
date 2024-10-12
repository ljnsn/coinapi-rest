"""Tests for the operations base."""

import httpx
import pytest

from coinapi._hooks import SDKHooks
from coinapi.base import Base
from coinapi.config import CoinAPIConfig
from coinapi.models.errors import CoinAPIError


@pytest.fixture(name="config")
def config_fixture() -> CoinAPIConfig:
    """Return a CoinAPIConfig instance."""
    config = CoinAPIConfig(None)
    config._hooks = SDKHooks()
    return config


def test_handle_request_error(config: CoinAPIConfig) -> None:
    """Test handle request error."""
    base = Base(config)
    hook_ctx = base._create_hook_context("test_operation")

    with pytest.raises(ValueError, match="Test error"):
        base._handle_request_error(hook_ctx, ValueError("Test error"))


def test_handle_error_response(config: CoinAPIConfig) -> None:
    """Test handle error response."""
    base = Base(config)

    response = httpx.Response(400, text="Bad Request")
    with pytest.raises(CoinAPIError):
        base._handle_error_response(response)


def test_set_response_content_text_plain(config: CoinAPIConfig) -> None:
    """Test set response content text plain."""
    base = Base(config)

    class MockResponse:
        content_plain = None

    res = MockResponse()
    http_res = httpx.Response(
        200,
        text="Test content",
        headers={"Content-Type": "text/plain"},
    )
    base._set_response_content(res, http_res, "text/plain", type(res))  # type: ignore[type-var]

    assert res.content_plain == "Test content"

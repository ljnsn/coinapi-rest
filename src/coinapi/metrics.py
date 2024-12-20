"""Metrics module."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class Metrics(Base):
    r"""Metrics are quantitative measurements used to evaluate the performance and activity of cryptocurrency exchanges.

    These metrics include:

    1. Trading Volume: The total amount of cryptocurrency traded on an exchange within a specific time period, indicating liquidity and activity.
    1. Market Depth: The level of buy and sell orders at different price levels, providing insights into liquidity and potential price impact.
    1. Order Book: A record of outstanding buy and sell orders for a cryptocurrency, reflecting supply and demand dynamics.
    1. Spread: The difference between the highest bid and lowest ask prices, indicating liquidity and trading costs.
    1. Price Charts: Visual representations of cryptocurrency price movements over time, helping identify trends and inform trading decisions.
    1. Market Cap: The total value of a cryptocurrency calculated by its price multiplied by circulating supply, reflecting relative size and value.
    1. Trading Pairs: Combinations of cryptocurrencies available for trading, including volume, price, and spread for each pair.
    1. User Metrics: Data on active users, new registrations, user retention, and engagement, indicating platform popularity and growth.
    1. Trading Fees: Fees charged for executing trades, including fee structure, discounts, and revenue generated by the exchange.
    1. Security Metrics: Measures assessing the security of an exchange, such as past incidents, user fund protection, and security audits.

    These metrics assist traders and investors in evaluating market activity, liquidity, and the reliability of crypto exchanges for informed decision-making.
    """

    def get_v1_metrics_listing(
        self,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsListingResponse:
        r"""Listing of all supported metrics by CoinAPI.

        Get all data metrics.
        """
        return self._make_request(
            "get_/v1/metrics/listing",
            operations.GetV1MetricsListingRequest(),
            operations.GetV1MetricsListingResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_exchange_listing(
        self,
        exchange_id: str,
        metric_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsExchangeListingResponse:
        r"""Listing of all supported exchange metrics.

        Get data metrics for exchange.
        """
        return self._make_request(
            "get_/v1/metrics/exchange/listing",
            operations.GetV1MetricsExchangeListingRequest(
                exchange_id=exchange_id,
                metric_id=metric_id,
            ),
            operations.GetV1MetricsExchangeListingResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_exchange_current(
        self,
        exchange_id: str,
        metric_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsExchangeCurrentResponse:
        r"""Current metrics for given exchange.

        Get current exchange metrics values.
        """
        return self._make_request(
            "get_/v1/metrics/exchange/current",
            operations.GetV1MetricsExchangeCurrentRequest(
                exchange_id=exchange_id,
                metric_id=metric_id,
            ),
            operations.GetV1MetricsExchangeCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_exchange_history(
        self,
        request: operations.GetV1MetricsExchangeHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsExchangeHistoryResponse:
        r"""Historical metrics for the exchange.

        Get exchange metrics history.
        """
        return self._make_request(
            "get_/v1/metrics/exchange/history",
            request,
            operations.GetV1MetricsExchangeHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_symbol_listing(
        self,
        metric_id: str | None = None,
        exchange_id: str | None = None,
        symbol_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsSymbolListingResponse:
        r"""Listing of all supported metrics for symbol.

        Get data metrics for symbol.
        """
        return self._make_request(
            "get_/v1/metrics/symbol/listing",
            operations.GetV1MetricsSymbolListingRequest(
                metric_id=metric_id,
                exchange_id=exchange_id,
                symbol_id=symbol_id,
            ),
            operations.GetV1MetricsSymbolListingResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_symbol_current(
        self,
        metric_id: str | None = None,
        symbol_id: str | None = None,
        exchange_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsSymbolCurrentResponse:
        r"""Current metrics for given symbol.

        Get current symbol metrics.
        """
        return self._make_request(
            "get_/v1/metrics/symbol/current",
            operations.GetV1MetricsSymbolCurrentRequest(
                metric_id=metric_id,
                symbol_id=symbol_id,
                exchange_id=exchange_id,
            ),
            operations.GetV1MetricsSymbolCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_symbol_history(
        self,
        request: operations.GetV1MetricsSymbolHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsSymbolHistoryResponse:
        r"""Historical metrics for symbol.

        Get symbol metrics history.
        """
        return self._make_request(
            "get_/v1/metrics/symbol/history",
            request,
            operations.GetV1MetricsSymbolHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_asset_listing(
        self,
        request: operations.GetV1MetricsAssetListingRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsAssetListingResponse:
        r"""Listing of all supported metrics for asset.

        Get data metrics for asset.
        """
        return self._make_request(
            "get_/v1/metrics/asset/listing",
            request,
            operations.GetV1MetricsAssetListingResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_asset_current(
        self,
        metric_id: str | None = None,
        asset_id: str | None = None,
        asset_id_external: str | None = None,
        exchange_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsAssetCurrentResponse:
        r"""Current metrics for given asset.

        Get current asset metrics.
        """
        return self._make_request(
            "get_/v1/metrics/asset/current",
            operations.GetV1MetricsAssetCurrentRequest(
                metric_id=metric_id,
                asset_id=asset_id,
                asset_id_external=asset_id_external,
                exchange_id=exchange_id,
            ),
            operations.GetV1MetricsAssetCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_metrics_asset_history(
        self,
        request: operations.GetV1MetricsAssetHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1MetricsAssetHistoryResponse:
        r"""Historical metrics for asset.

        Get asset metrics history.
        """
        return self._make_request(
            "get_/v1/metrics/asset/history",
            request,
            operations.GetV1MetricsAssetHistoryResponse,
            accept_header_override=accept_header_override,
        )

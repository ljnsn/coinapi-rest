"""OHLCV operations."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class Ohlcv(Base):
    r"""API calls described in this section are related to downloading OHLCV *(Open, High, Low, Close, Volume)* timeseries data.

    Each data point of this timeseries represents several indicators calculated from
    transactions activity inside a time range (period).

    :::info
    OHLCV data primary purpose is to present an overview of the market in human-readable form.
    It's often used to visualize market data on charts, websites, and various kinds of reports.
    :::

    :::tip
    CoinAPI expanded the standard OHLCV timeseries by including time of first
    and last trade and amount of trades executed inside period.
    :::
    """

    def get_v1_ohlcv_periods(
        self,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OhlcvPeriodsResponse:
        r"""[ohlcv] List all periods.

        Get full list of supported time periods available for requesting OHLCV timeseries data.

        ### Available periods

        Time unit | Period identifiers
        --------- | -----------
        Second | 1SEC, 2SEC, 3SEC, 4SEC, 5SEC, 6SEC, 10SEC, 15SEC, 20SEC, 30SEC
        Minute | 1MIN, 2MIN, 3MIN, 4MIN, 5MIN, 6MIN, 10MIN, 15MIN, 20MIN, 30MIN
        Hour | 1HRS, 2HRS, 3HRS, 4HRS, 6HRS, 8HRS, 12HRS
        Day | 1DAY, 2DAY, 3DAY, 5DAY, 7DAY, 10DAY
        Month | 1MTH, 2MTH, 3MTH, 4MTH, 6MTH
        Year | 1YRS, 2YRS, 3YRS, 4YRS, 5YRS

        :::tip
        You can assume that we will not remove any periods from this response, however, we may add new ones.
        :::
        """
        return self._make_request(
            "get_/v1/ohlcv/periods",
            operations.GetV1OhlcvPeriodsRequest(),
            operations.GetV1OhlcvPeriodsResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_ohlcv_symbol_id_history(
        self,
        request: operations.GetV1OhlcvSymbolIDHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OhlcvSymbolIDHistoryResponse:
        r"""[ohlcv] Historical data.

        Get OHLCV timeseries data returned in time ascending order. Data can
        be requested by the period and for the specific symbol eg
        `BITSTAMP_SPOT_BTC_USD`, if you need to query timeseries by asset
        pairs eg. `BTC/USD`, then please reffer to the Exchange Rates Timeseries data.

        :::info
        The OHLCV Historical endpoint data can be delayed a few seconds. Use OHLCV Latest endpoint to get real-time data without delay.
        :::
        """
        return self._make_request(
            "get_/v1/ohlcv/{symbol_id}/history",
            request,
            operations.GetV1OhlcvSymbolIDHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_ohlcv_exchanges_exchange_id_history(
        self,
        exchange_id: str,
        period_id: str,
        time_start: str,
        time_end: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OhlcvExchangesExchangeIDHistoryResponse:
        r"""[ohlcv] Historical data by exchange.

        Get OHLCV timeseries data returned in time ascending order. Data can
        be requested by the period and for the specific exchange eg `BITSTAMP`

        :::info
        The OHLCV Historical endpoint data can be delayed a few seconds.
        `time_start` and `time_end` must point to the same day
        :::
        """
        return self._make_request(
            "get_/v1/ohlcv/exchanges/{exchange_id}/history",
            operations.GetV1OhlcvExchangesExchangeIDHistoryRequest(
                exchange_id=exchange_id,
                period_id=period_id,
                time_start=time_start,
                time_end=time_end,
            ),
            operations.GetV1OhlcvExchangesExchangeIDHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_ohlcv_symbol_id_latest(
        self,
        symbol_id: str,
        period_id: str | None = None,
        limit: int | None = None,
        include_empty_items: bool | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OhlcvSymbolIDLatestResponse:
        r"""[ohlcv] Latest data.

        Get OHLCV latest timeseries data returned in time descending order.
        Data can be requested by the period and for the specific symbol
        eg `BITSTAMP_SPOT_BTC_USD`, if you need to query timeseries by asset pairs
        eg. `BTC/USD`, then please reffer to the Exchange Rates Timeseries data.

        :::info
        OHLCV Latest endpoint is providing real-time data without delay.
        The OHLCV Historical endpoint data can be delayed a few seconds.
        :::
        """
        return self._make_request(
            "get_/v1/ohlcv/{symbol_id}/latest",
            operations.GetV1OhlcvSymbolIDLatestRequest(
                symbol_id=symbol_id,
                period_id=period_id,
                limit=limit,
                include_empty_items=include_empty_items,
            ),
            operations.GetV1OhlcvSymbolIDLatestResponse,
            accept_header_override=accept_header_override,
        )

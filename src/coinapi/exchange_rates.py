"""Exchange rates module."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class ExchangeRates(Base):
    r"""Exchange rate is defined as (VWAP-24H) last 24 hour (rolling window over time) Volume Weighted Average Price across multiple data sources listed on our platform. We are selecting and managing the data sources that are used in the calculation based on multiple factors to provide data of highest quality.

    Algorithm is described below:

      1. Exchange rates are produced from quotes, trades, and metadata datasets.
      1. Symbols that are not data_type = \"SPOT\" are excluded from the calculation.
      1. Symbols from the data sources that were marked by us as not legitimate are excluded from the calculation.
      1. Quotes data where the spread is outside the range of ```<0$; 67%>``` are discarded. `spreadPrc = (ask - bid) / ((ask + bid) / 2)`
      1. The midpoint from the quote data is used as a pricing reference and it's weighted by the passive cumulative volume resting on the best prices.
      1. Volume from the trades is used to weight the midpoint prices in the VWAP24 algorithm.
      1. Midpoint data that has not been updated in the last 5 minutes and 1 second is discarded.
      1. The last 24-hour volume for each symbol is updated every 4 hours when approximately 20% of the data in the sliding window changes (also, the list of eligible markets is updated at the same time).
      1. Everywhere in the algorithm below, we are using asset pairs only from exchanges that have the highest legitimacy rank, and the rest of the exchanges are discarded. As we establish the highest-ranking exchanges that have this data for each asset pair, we ensure that the highest quality data is used for each of them. The rank used for asset pairing is carried over to the following steps.
      1. Every 1 second, we update VWAP24 data for every asset pair across all data sources.
      1. For each asset pair, we also discard data that is outside the 3 sigma range if there are at least 3 exchanges for this asset pair.
      1. From the VWAP24 data, we are creating a tree structure where node/vertex = asset and edge = rate.
      1. By traversing the tree structure using the BFS algorithm and our secret sauce, we are able to establish the final exchange rates.
    """

    def get_v1_specific_rate(
        self,
        asset_id_base: str,
        asset_id_quote: str,
        time: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1SpecificRateResponse:
        r"""[exchange rates] Get specific rate.

        Retrieves the exchange rate for a specific base and quote asset at a given time or the current rate.

        :::info
        If you are using an exchange rate for mission-critical operations, then for best reliability, you should measure the difference between current time and the time returned from the response to ensure that value of the difference between those meets your internal requirements.
        :::
        """
        return self._make_request(
            "Get specific rate",
            operations.GetV1SpecificRateRequest(
                asset_id_base=asset_id_base,
                asset_id_quote=asset_id_quote,
                time=time,
            ),
            operations.GetV1SpecificRateResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_base_rates(
        self,
        asset_id_base: str,
        filter_asset_id: str | None = None,
        invert: bool | None = None,
        time: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1BaseRatesResponse:
        r"""[exchange rates] Get all current rates.

        Get the current exchange rate between requested asset and all other assets.

        :::info
        If you are using an exchange rate for mission-critical operations, then for best reliability, you should measure the difference between current time and the time returned from the response to ensure that value of the difference between those meets your internal requirements.
        :::

        :::info
        You can invert the rates by using Y = 1 / X equation, for example BTC/USD = 1 / (USD/BTC);
        :::
        """
        return self._make_request(
            "get_/v1/exchangerate/{asset_id_base}",
            operations.GetV1BaseRatesRequest(
                asset_id_base=asset_id_base,
                filter_asset_id=filter_asset_id,
                invert=invert,
                time=time,
            ),
            operations.GetV1BaseRatesResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_history_periods(
        self,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1HistoryPeriodsResponse:
        r"""[exchange rates] Timeseries periods.

        You can also obtain historical exchange rates of any asset pair, grouped into time periods.
        Get full list of supported time periods available for requesting exchange rates historical timeseries data.

        ## Timeseries periods
        Time unit |	Period identifiers
        --- | ---
        Second | 1SEC, 2SEC, 3SEC, 4SEC, 5SEC, 6SEC, 10SEC, 15SEC, 20SEC, 30SEC
        Minute | 1MIN, 2MIN, 3MIN, 4MIN, 5MIN, 6MIN, 10MIN, 15MIN, 20MIN, 30MIN
        Hour | 1HRS, 2HRS, 3HRS, 4HRS, 6HRS, 8HRS, 12HRS
        Day | 1DAY, 2DAY, 3DAY, 5DAY, 7DAY, 10DAY
        """
        return self._make_request(
            "get_/v1/exchangerate/history/periods",
            operations.GetV1HistoryPeriodsRequest(),
            operations.GetV1HistoryPeriodsResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_pair_history(
        self,
        request: operations.GetV1PairHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1PairHistoryResponse:
        r"""[exchange rates] Timeseries data.

        Get the historical exchange rates between two assets in the form of the timeseries.
        """
        return self._make_request(
            "get_/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history",
            request,
            operations.GetV1PairHistoryResponse,
            accept_header_override=accept_header_override,
        )

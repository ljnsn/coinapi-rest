"""Operations."""

__all__ = (
    "CoinAPIRequest",
    "CoinAPIResponse",
    "GetV1AssetsAssetIDRequest",
    "GetV1AssetsAssetIDResponse",
    "GetV1AssetsIconsSizeRequest",
    "GetV1AssetsIconsSizeResponse",
    "GetV1AssetsRequest",
    "GetV1AssetsResponse",
    "GetV1BaseRatesRequest",
    "GetV1BaseRatesResponse",
    "GetV1ExchangesExchangeIDRequest",
    "GetV1ExchangesExchangeIDResponse",
    "GetV1ExchangesIconsSizeRequest",
    "GetV1ExchangesIconsSizeResponse",
    "GetV1ExchangesRequest",
    "GetV1ExchangesResponse",
    "GetV1HistoryPeriodsResponse",
    "GetV1IndexesIndexIDHistoryRequest",
    "GetV1IndexesIndexIDHistoryResponse",
    "GetV1IndexesIndexIDRequest",
    "GetV1IndexesIndexIDResponse",
    "GetV1IndexesIndexIDTimeseriesRequest",
    "GetV1IndexesIndexIDTimeseriesResponse",
    "GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDRequest",
    "GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDResponse",
    "GetV1IndexesResponse",
    "GetV1MetadataResponse",
    "GetV1MetricsAssetCurrentRequest",
    "GetV1MetricsAssetCurrentResponse",
    "GetV1MetricsAssetHistoryRequest",
    "GetV1MetricsAssetHistoryResponse",
    "GetV1MetricsAssetListingRequest",
    "GetV1MetricsAssetListingResponse",
    "GetV1MetricsExchangeCurrentRequest",
    "GetV1MetricsExchangeCurrentResponse",
    "GetV1MetricsExchangeHistoryRequest",
    "GetV1MetricsExchangeHistoryResponse",
    "GetV1MetricsExchangeListingRequest",
    "GetV1MetricsExchangeListingResponse",
    "GetV1MetricsListingResponse",
    "GetV1MetricsSymbolCurrentRequest",
    "GetV1MetricsSymbolCurrentResponse",
    "GetV1MetricsSymbolHistoryRequest",
    "GetV1MetricsSymbolHistoryResponse",
    "GetV1MetricsSymbolListingRequest",
    "GetV1MetricsSymbolListingResponse",
    "GetV1OhlcvExchangesExchangeIDHistoryRequest",
    "GetV1OhlcvExchangesExchangeIDHistoryResponse",
    "GetV1OhlcvPeriodsResponse",
    "GetV1OhlcvSymbolIDHistoryRequest",
    "GetV1OhlcvSymbolIDHistoryResponse",
    "GetV1OhlcvSymbolIDLatestRequest",
    "GetV1OhlcvSymbolIDLatestResponse",
    "GetV1Orderbooks3CurrentRequest",
    "GetV1Orderbooks3CurrentResponse",
    "GetV1Orderbooks3SymbolIDCurrentRequest",
    "GetV1Orderbooks3SymbolIDCurrentResponse",
    "GetV1OrderbooksSymbolIDCurrentRequest",
    "GetV1OrderbooksSymbolIDCurrentResponse",
    "GetV1OrderbooksSymbolIDDepthCurrentRequest",
    "GetV1OrderbooksSymbolIDDepthCurrentResponse",
    "GetV1OrderbooksSymbolIDHistoryRequest",
    "GetV1OrderbooksSymbolIDHistoryResponse",
    "GetV1OrderbooksSymbolIDLatestRequest",
    "GetV1OrderbooksSymbolIDLatestResponse",
    "GetV1PairHistoryRequest",
    "GetV1PairHistoryResponse",
    "GetV1QuotesCurrentRequest",
    "GetV1QuotesCurrentResponse",
    "GetV1QuotesLatestRequest",
    "GetV1QuotesLatestResponse",
    "GetV1QuotesSymbolIDCurrentRequest",
    "GetV1QuotesSymbolIDCurrentResponse",
    "GetV1QuotesSymbolIDHistoryRequest",
    "GetV1QuotesSymbolIDHistoryResponse",
    "GetV1QuotesSymbolIDLatestRequest",
    "GetV1QuotesSymbolIDLatestResponse",
    "GetV1SpecificRateRequest",
    "GetV1SpecificRateResponse",
    "GetV1SymbolsExchangeIDRequest",
    "GetV1SymbolsExchangeIDResponse",
    "GetV1SymbolsMapExchangeIDRequest",
    "GetV1SymbolsMapExchangeIDResponse",
    "GetV1SymbolsRequest",
    "GetV1SymbolsResponse",
    "GetV1TradesLatestRequest",
    "GetV1TradesLatestResponse",
    "GetV1TradesSymbolIDHistoryRequest",
    "GetV1TradesSymbolIDHistoryResponse",
    "GetV1TradesSymbolIDLatestRequest",
    "GetV1TradesSymbolIDLatestResponse",
    "PostV1IndexesJSONResponse",
    "PutV1IndexesIndexIDJSONRequest",
    "PutV1IndexesIndexIDJSONResponse",
)

from coinapi.models.operations.base import CoinAPIRequest, CoinAPIResponse
from coinapi.models.operations.get_v1_assets import *
from coinapi.models.operations.get_v1_assets_asset_id_ import *
from coinapi.models.operations.get_v1_assets_icons_size_ import *
from coinapi.models.operations.get_v1_base_rates import *
from coinapi.models.operations.get_v1_exchanges import *
from coinapi.models.operations.get_v1_exchanges_exchange_id_ import *
from coinapi.models.operations.get_v1_exchanges_icons_size_ import *
from coinapi.models.operations.get_v1_history_periods import *
from coinapi.models.operations.get_v1_indexes import *
from coinapi.models.operations.get_v1_indexes_index_id_ import *
from coinapi.models.operations.get_v1_indexes_index_id_history import *
from coinapi.models.operations.get_v1_indexes_index_id_timeseries import *
from coinapi.models.operations.get_v1_indexes_index_id_timeseries_to_be_announced import *
from coinapi.models.operations.get_v1_metadata import *
from coinapi.models.operations.get_v1_metrics_asset_current import *
from coinapi.models.operations.get_v1_metrics_asset_history import *
from coinapi.models.operations.get_v1_metrics_asset_listing import *
from coinapi.models.operations.get_v1_metrics_exchange_current import *
from coinapi.models.operations.get_v1_metrics_exchange_history import *
from coinapi.models.operations.get_v1_metrics_exchange_listing import *
from coinapi.models.operations.get_v1_metrics_listing import *
from coinapi.models.operations.get_v1_metrics_symbol_current import *
from coinapi.models.operations.get_v1_metrics_symbol_history import *
from coinapi.models.operations.get_v1_metrics_symbol_listing import *
from coinapi.models.operations.get_v1_ohlcv_exchanges_exchange_id_history import *
from coinapi.models.operations.get_v1_ohlcv_periods import *
from coinapi.models.operations.get_v1_ohlcv_symbol_id_history import *
from coinapi.models.operations.get_v1_ohlcv_symbol_id_latest import *
from coinapi.models.operations.get_v1_orderbooks3_current import *
from coinapi.models.operations.get_v1_orderbooks3_symbol_id_current import *
from coinapi.models.operations.get_v1_orderbooks_symbol_id_current import *
from coinapi.models.operations.get_v1_orderbooks_symbol_id_depth_current import *
from coinapi.models.operations.get_v1_orderbooks_symbol_id_history import *
from coinapi.models.operations.get_v1_orderbooks_symbol_id_latest import *
from coinapi.models.operations.get_v1_pair_history import (
    GetV1PairHistoryRequest,
    GetV1PairHistoryResponse,
)
from coinapi.models.operations.get_v1_quotes_current import *
from coinapi.models.operations.get_v1_quotes_latest import *
from coinapi.models.operations.get_v1_quotes_symbol_id_current import *
from coinapi.models.operations.get_v1_quotes_symbol_id_history import *
from coinapi.models.operations.get_v1_quotes_symbol_id_latest import *
from coinapi.models.operations.get_v1_specific_rate import *
from coinapi.models.operations.get_v1_symbols import *
from coinapi.models.operations.get_v1_symbols_exchange_id_ import *
from coinapi.models.operations.get_v1_symbols_map_exchange_id_ import *
from coinapi.models.operations.get_v1_trades_latest import *
from coinapi.models.operations.get_v1_trades_symbol_id_history import *
from coinapi.models.operations.get_v1_trades_symbol_id_latest import *
from coinapi.models.operations.post_v1_indexes_json import *
from coinapi.models.operations.put_v1_indexes_index_id_json import *

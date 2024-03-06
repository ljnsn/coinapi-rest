"""Order book module."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class OrderBook(Base):
    r"""This section describes calls related to order book data, also known as books or passive level 2 data.

    :::info
    When requesting current data for a specific symbol, output is not encapsulated into JSON array as only one item is returned.
    :::

    :::info
    GET `/v1/orderbooks/current` endpoint is charged one request per 100 data points returned after applying a filter defined by filter_symbol_id parameter. If filter symbols target more than one exchange, error is returned.
    :::

    :::info
    When requesting current order book data limited to a single level, then quotes are actually used. This information is important from the perspective that quotes data could be faster than order book data (behavior is dependent solely one the data source) and they can have the size equal to 0 when the size is unknown. Some data sources publish order books and separately quote data (without the sizes) at a higher frequency. In that case, we will merge the order book feed with quotes feed to make sure that our updates are as fast as possible. The quotes will have the size equal to 0 as the value is unknown and the customer can decide if these higher frequency updates without the sizes are valuable or if not then can discard them or ask for at least 2 order book levels (in case of a REST API call). For the data sources that publish order books only or order books and quotes with the sizes then this will not happen.
    :::
    """

    def get_v1_orderbooks_symbol_id_depth_current(
        self,
        symbol_id: str,
        limit_levels: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OrderbooksSymbolIDDepthCurrentResponse:
        r"""[order book] Current depth of the order book.

        Retrieves the current depth of the order book for the specified symbol.
        """
        return self._make_request(
            "get_/v1/orderbooks/{symbol_id}/depth/current",
            operations.GetV1OrderbooksSymbolIDDepthCurrentRequest(
                symbol_id=symbol_id,
                limit_levels=limit_levels,
            ),
            operations.GetV1OrderbooksSymbolIDDepthCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_orderbooks_symbol_id_history(
        self,
        request: operations.GetV1OrderbooksSymbolIDHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OrderbooksSymbolIDHistoryResponse:
        r"""[order book] Historical data.

        Get historical order book snapshots for a specific symbol within time range, returned in time ascending order.

        :::info
        The historical order book data via the REST API is currently limited by a number of updates and to the maximum number of 20 levels.
        :::
        """
        return self._make_request(
            "get_/v1/orderbooks/{symbol_id}/history",
            request,
            operations.GetV1OrderbooksSymbolIDHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_orderbooks_symbol_id_current(
        self,
        symbol_id: str,
        limit_levels: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OrderbooksSymbolIDCurrentResponse:
        r"""Get current order book.

        Retrieves the current order book for the specified symbol.
        """
        return self._make_request(
            "get_/v1/orderbooks/{symbol_id}/current",
            operations.GetV1OrderbooksSymbolIDCurrentRequest(
                symbol_id=symbol_id,
                limit_levels=limit_levels,
            ),
            operations.GetV1OrderbooksSymbolIDCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_orderbooks_symbol_id_latest(
        self,
        symbol_id: str,
        limit: int | None = None,
        limit_levels: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1OrderbooksSymbolIDLatestResponse:
        r"""[order book] Latest data.

        Get latest order book snapshots for a specific symbol, returned in time descending order.

        :::info
        The historical order book data via the REST API is currently limited by a number of updates and to the maximum number of 20 levels.
        :::
        """
        return self._make_request(
            "get_/v1/orderbooks/{symbol_id}/latest",
            operations.GetV1OrderbooksSymbolIDLatestRequest(
                symbol_id=symbol_id,
                limit=limit,
                limit_levels=limit_levels,
            ),
            operations.GetV1OrderbooksSymbolIDLatestResponse,
            accept_header_override=accept_header_override,
        )

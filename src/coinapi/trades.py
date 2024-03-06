"""Trades operations."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class Trades(Base):
    r"""Controller for retrieving trade data related to executed transactions."""

    def get_v1_trades_symbol_id_history(
        self,
        request: operations.GetV1TradesSymbolIDHistoryRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1TradesSymbolIDHistoryResponse:
        r"""[trades] Historical data.

        Get history transactions from specific symbol, returned in time ascending order.
        """
        return self._make_request(
            "get_/v1/trades/{symbol_id}/history",
            request,
            operations.GetV1TradesSymbolIDHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_trades_symbol_id_latest(
        self,
        symbol_id: str,
        limit: int | None = None,
        include_id: bool | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1TradesSymbolIDLatestResponse:
        r"""[trades] Latest data by symbol_id.

        Get latest trades executed up to 1 minute ago. Latest data is always returned in time descending order.
        """
        return self._make_request(
            "get_/v1/trades/{symbol_id}/latest",
            operations.GetV1TradesSymbolIDLatestRequest(
                symbol_id=symbol_id,
                limit=limit,
                include_id=include_id,
            ),
            operations.GetV1TradesSymbolIDLatestResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_trades_latest(
        self,
        filter_symbol_id: str | None = None,
        include_id: bool | None = None,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1TradesLatestResponse:
        r"""[trades] Latest data.

        Get latest trades executed up to 1 minute ago. Latest data is always returned in time descending order.
        """
        return self._make_request(
            "get_/v1/trades/latest",
            operations.GetV1TradesLatestRequest(
                filter_symbol_id=filter_symbol_id,
                include_id=include_id,
                limit=limit,
            ),
            operations.GetV1TradesLatestResponse,
            accept_header_override=accept_header_override,
        )

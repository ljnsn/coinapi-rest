"""Quote operations."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class Quotes(Base):
    r"""Controller for retrieving quotes data, also known as quotes or passive level 1 data."""

    def get_v1_quotes_symbol_id_history(
        self,
        symbol_id: str,
        time_start: str | None = None,
        time_end: str | None = None,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1QuotesSymbolIDHistoryResponse:
        r"""[quotes] Historical data.

        Get historical quote updates within requested time range, returned in time ascending order.
        """
        return self._make_request(
            "get_/v1/quotes/{symbol_id}/history",
            operations.GetV1QuotesSymbolIDHistoryRequest(
                symbol_id=symbol_id,
                time_start=time_start,
                time_end=time_end,
                limit=limit,
            ),
            operations.GetV1QuotesSymbolIDHistoryResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_quotes_current(
        self,
        filter_symbol_id: str | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1QuotesCurrentResponse:
        r"""[quotes] Current data.

        Get current quotes for all symbols or for a specific symbol.

        :::info
        When requesting current data for a specific symbol, output is not encapsulated
        into JSON array as only one item is returned.
        :::
        """
        return self._make_request(
            "get_/v1/quotes/current",
            operations.GetV1QuotesCurrentRequest(filter_symbol_id=filter_symbol_id),
            operations.GetV1QuotesCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_quotes_symbol_id_current(
        self,
        symbol_id: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1QuotesSymbolIDCurrentResponse:
        r"""[quotes] Current quotes for a specific symbol."""
        return self._make_request(
            "get_/v1/quotes/{symbol_id}/current",
            operations.GetV1QuotesSymbolIDCurrentRequest(symbol_id=symbol_id),
            operations.GetV1QuotesSymbolIDCurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_quotes_latest(
        self,
        filter_symbol_id: str | None = None,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1QuotesLatestResponse:
        r"""[quotes] Latest data.

        Get latest updates of the quotes up to 1 minute ago. Latest data is always returned in time descending order.
        """
        return self._make_request(
            "get_/v1/quotes/latest",
            operations.GetV1QuotesLatestRequest(
                filter_symbol_id=filter_symbol_id,
                limit=limit,
            ),
            operations.GetV1QuotesLatestResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_quotes_symbol_id_latest(
        self,
        symbol_id: str,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1QuotesSymbolIDLatestResponse:
        r"""[quotes] Latest quote updates for a specific symbol."""
        return self._make_request(
            "get_/v1/quotes/{symbol_id}/latest",
            operations.GetV1QuotesSymbolIDLatestRequest(
                symbol_id=symbol_id,
                limit=limit,
            ),
            operations.GetV1QuotesSymbolIDLatestResponse,
            accept_header_override=accept_header_override,
        )

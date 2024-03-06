"""Order book L3 operations."""

from coinapi.base import AcceptEnum, Base
from coinapi.models import operations


class OrderBookL3(Base):
    r"""This section describes calls related to order book data, also known as books or passive level 3 data."""

    def get_v1_orderbooks3_current(
        self,
        filter_symbol_id: str | None = None,
        limit_levels: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1Orderbooks3CurrentResponse:
        r"""[order book l3] Current order books."""
        return self._make_request(
            "get_/v1/orderbooks3/current",
            operations.GetV1Orderbooks3CurrentRequest(
                filter_symbol_id=filter_symbol_id,
                limit_levels=limit_levels,
            ),
            operations.GetV1Orderbooks3CurrentResponse,
            accept_header_override=accept_header_override,
        )

    def get_v1_orderbooks3_symbol_id_current(
        self,
        symbol_id: str,
        limit_levels: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1Orderbooks3SymbolIDCurrentResponse:
        r"""[order book l3] Current order book by symbol_id.

        Retrieves the current order book for the specified symbol.
        """
        return self._make_request(
            "get_/v1/orderbooks3/{symbol_id}/current",
            operations.GetV1Orderbooks3SymbolIDCurrentRequest(
                symbol_id=symbol_id,
                limit_levels=limit_levels,
            ),
            operations.GetV1Orderbooks3SymbolIDCurrentResponse,
            accept_header_override=accept_header_override,
        )

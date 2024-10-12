"""Indexes module."""

from datetime import datetime

from coinapi.base import AcceptEnum, Base
from coinapi.models import components, operations


class Indexes(Base):
    r"""Indexes section of the API is in the Alpha release cycle. Use only for testing, evaluaton and feedback."""

    def get_v1_indexes(
        self,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1IndexesResponse:
        r"""List of available indexes."""
        return self._make_request(
            "get_/v1/indexes",
            operations.GetV1IndexesRequest(),
            operations.GetV1IndexesResponse,
            accept_header_override,
        )

    def post_v1_indexes_json(
        self,
        request: operations.PostV1IndexesJSONRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.PostV1IndexesJSONResponse:
        r"""Create index."""
        return self._make_request(
            "post_/v1/indexes_json",
            request,
            operations.PostV1IndexesJSONResponse,
            accept_header_override,
        )

    def get_v1_indexes_index_id(
        self,
        index_id: str,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1IndexesIndexIDResponse:
        r"""Get index data."""
        return self._make_request(
            "get_/v1/indexes/{index_id}",
            operations.GetV1IndexesIndexIDRequest(index_id=index_id),
            operations.GetV1IndexesIndexIDResponse,
            accept_header_override,
        )

    def put_v1_indexes_index_id_json(
        self,
        index_id: str,
        v1_index_data: components.V1IndexData | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.PutV1IndexesIndexIDJSONResponse:
        r"""Update index."""
        return self._make_request(
            "put_/v1/indexes/{index_id}_json",
            operations.PutV1IndexesIndexIDJSONRequest(
                index_id=index_id,
                body=v1_index_data,
            ),
            operations.PutV1IndexesIndexIDJSONResponse,
            accept_header_override,
        )

    def get_v1_indexes_index_id_history(
        self,
        index_id: str,
        time_start: datetime | None = None,
        time_end: datetime | None = None,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1IndexesIndexIDHistoryResponse:
        r"""Retrieve Historical Index Value and Composition."""
        return self._make_request(
            "get_/v1/indexes/{index_id}/history",
            operations.GetV1IndexesIndexIDHistoryRequest(
                index_id=index_id,
                time_start=time_start,
                time_end=time_end,
                limit=limit,
            ),
            operations.GetV1IndexesIndexIDHistoryResponse,
            accept_header_override,
        )

    def get_v1_indexes_index_id_timeseries(
        self,
        index_id: str,
        time_start: datetime | None = None,
        time_end: datetime | None = None,
        limit: int | None = None,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1IndexesIndexIDTimeseriesResponse:
        r"""Retrieve Historical Index Value Timeseries."""
        return self._make_request(
            "get_/v1/indexes/{index_id}/timeseries",
            operations.GetV1IndexesIndexIDTimeseriesRequest(
                index_id=index_id,
                time_start=time_start,
                time_end=time_end,
                limit=limit,
            ),
            operations.GetV1IndexesIndexIDTimeseriesResponse,
            accept_header_override,
        )

    def get_v1_indexes_index_id_timeseries_to_be_announced(
        self,
        request: operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDRequest,
        accept_header_override: AcceptEnum | None = None,
    ) -> operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDResponse:
        r"""Retrieve Historical Composition Value Timeseries.

        Retrieves historical timeseries for the specific composition value for an index
        """
        return self._make_request(
            "get_/v1/indexes/{index_id}/timeseries/TO_BE_ANNOUNCED",
            request,
            operations.GetV1IndexesIndexIDTimeseriesTOBEANNOUNCEDResponse,
            accept_header_override,
        )

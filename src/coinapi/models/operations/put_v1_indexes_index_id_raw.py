"""Update an index."""

from __future__ import annotations

import dataclasses

import httpx

from coinapi.models.components import v1_indexdataresponse


@dataclasses.dataclass
class PutV1IndexesIndexIDRawRequest:
    """Request to update an index."""

    index_id: str = dataclasses.field(
        metadata={
            "path_param": {
                "field_name": "index_id",
                "style": "simple",
                "explode": False,
            },
        },
    )
    request_body: bytes | None = dataclasses.field(
        default=None,
        metadata={"request": {"media_type": "application/x-msgpack"}},
    )


@dataclasses.dataclass
class PutV1IndexesIndexIDRawResponse:
    """Successful operation."""

    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    v1_index_data_response: str | None = dataclasses.field(default=None)
    r"""successful operation"""
    v1_index_data_response1: v1_indexdataresponse.V1IndexDataResponse | None = (
        dataclasses.field(default=None)
    )
    r"""successful operation"""
    body: bytes | None = dataclasses.field(default=None)

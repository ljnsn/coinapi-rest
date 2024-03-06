"""Security module."""

from __future__ import annotations

from typing import Annotated

import msgspec


class Security(msgspec.Struct):
    """Security."""

    api_key: Annotated[
        str,
        msgspec.Meta(
            extra={
                "security": {
                    "scheme": True,
                    "type": "apiKey",
                    "sub_type": "header",
                    "field_name": "X-CoinAPI-Key",
                },
            },
        ),
    ]

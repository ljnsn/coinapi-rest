"""Metric."""

from __future__ import annotations

import msgspec

from coinapi.utils.aliases import OptionalStrOrUnset


class V1Metric(msgspec.Struct, kw_only=True, frozen=True, omit_defaults=True):
    r"""Represents a metric."""

    metric_id: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the metric ID."""
    description: OptionalStrOrUnset = msgspec.field(default=msgspec.UNSET)
    r"""Gets or sets the metric description."""

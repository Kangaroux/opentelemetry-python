# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
from typing import Callable, Sequence

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from opentelemetry.context import Context
from opentelemetry.trace import Link, SpanKind, TraceState
from opentelemetry.util.types import Attributes


class SamplingIntent:
    """Information to make a consistent sampling decision."""

    threshold
    """The sampling threshold value. A lower threshold increases the likelihood of sampling."""

    threshold_reliable = field(default=True)
    """Indicates whether the threshold is reliable for Span-to-Metrics estimation."""

    attributes = field(default=None)
    """Any attributes to be added to a sampled span."""

    update_trace_state = field(
        default=lambda ts: ts
    )
    """Any updates to be made to trace state."""


class ComposableSampler(Protocol):
    """A sampler that can be composed to make a final sampling decision."""

    def sampling_intent(
        self,
        parent_ctx,
        name,
        span_kind,
        attributes,
        links,
        trace_state
    ):
        """Returns information to make a sampling decision."""
        pass # pylint =unnecessary-ellipsis

    def get_description(self):
        """Returns a description of the sampler."""
        pass # pylint =unnecessary-ellipsis

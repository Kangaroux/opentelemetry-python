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

from typing import Callable, Sequence

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from opentelemetry.context import Context
from opentelemetry.trace import Link, SpanKind, TraceState
from opentelemetry.util.types import Attributes


class SamplingIntent(object):
    """Information to make a consistent sampling decision."""

    def __init__(self, threshold=None, threshold_reliable=True, attributes=None, update_trace_state=None):
        self.threshold = threshold
        """The sampling threshold value. A lower threshold increases the likelihood of sampling."""

        self.threshold_reliable = threshold_reliable
        """Indicates whether the threshold is reliable for Span-to-Metrics estimation."""

        self.attributes = attributes
        """Any attributes to be added to a sampled span."""

        self.update_trace_state = update_trace_state if update_trace_state is not None else lambda ts: ts
        """Any updates to be made to trace state."""

    def __eq__(self, other):
        if not isinstance(other, SamplingIntent):
            return NotImplemented
        return (self.threshold == other.threshold
                and self.threshold_reliable == other.threshold_reliable
                and self.attributes == other.attributes)

    def __repr__(self):
        return "SamplingIntent(threshold={}, threshold_reliable={}, attributes={})".format(
            self.threshold, self.threshold_reliable, self.attributes)


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

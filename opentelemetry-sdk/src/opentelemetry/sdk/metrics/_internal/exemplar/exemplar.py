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

from opentelemetry.util.types import Attributes


class Exemplar(object):
    """A representation of an exemplar, which is a sample input measurement.

    Exemplars also hold information about the environment when the measurement
    was recorded, for example the span and trace ID of the active span when the
    exemplar was recorded.

    Attributes:
        trace_id: (optional) The trace associated with a recording
        span_id: (optional) The span associated with a recording
        time_unix_nano: The time of the observation
        value: The recorded value
        filtered_attributes: A set of filtered attributes which provide additional insight into the Context when the observation was made.

    References:
        https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/data-model.md#exemplars
        https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk.md#exemplar
    """

    def __init__(self, filtered_attributes=None, value=None, time_unix_nano=None, span_id=None, trace_id=None):
        self.filtered_attributes = filtered_attributes
        self.value = value
        self.time_unix_nano = time_unix_nano
        self.span_id = span_id
        self.trace_id = trace_id

    def __eq__(self, other):
        if not isinstance(other, Exemplar):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Exemplar(filtered_attributes={}, value={}, time_unix_nano={}, span_id={}, trace_id={})".format(
            self.filtered_attributes, self.value, self.time_unix_nano, self.span_id, self.trace_id)

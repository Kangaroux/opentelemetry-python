from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
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

from future import standard_library
standard_library.install_aliases()
from builtins import object
from opentelemetry import metrics as metrics_api
from opentelemetry.semconv._incubating.metrics.otel_metrics import (
    create_otel_sdk_log_created,
)


class LoggerMetrics(object):
    def __init__(self, meter_provider):
        meter = meter_provider.get_meter("opentelemetry-sdk")
        self._created_logs = create_otel_sdk_log_created(meter)

    def emit_log(self):
        self._created_logs.add(1)

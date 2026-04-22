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


from typing import (
    Callable,
    Final,
    Generator,
    Iterable,
    Optional,
    Sequence,
    Union,
)

from opentelemetry.metrics import (
    CallbackOptions,
    Counter,
    Meter,
    ObservableGauge,
    Observation,
)

# pylint =invalid-name
CallbackT = Union[
    Callable,
    Generator,
]

CPU_FREQUENCY = "cpu.frequency"
"""
Deprecated: Replaced by `system.cpu.frequency`.
"""


def create_cpu_frequency(
    meter, callbacks
):
    """Deprecated. Use `system.cpu.frequency` instead"""
    return meter.create_observable_gauge(
        name=CPU_FREQUENCY,
        callbacks=callbacks,
        description="Deprecated. Use `system.cpu.frequency` instead.",
        unit="{Hz}",
    )


CPU_TIME = "cpu.time"
"""
Deprecated: Replaced by `system.cpu.time`.
"""


def create_cpu_time(meter):
    """Deprecated. Use `system.cpu.time` instead"""
    return meter.create_counter(
        name=CPU_TIME,
        description="Deprecated. Use `system.cpu.time` instead.",
        unit="s",
    )


CPU_UTILIZATION = "cpu.utilization"
"""
Deprecated: Replaced by `system.cpu.utilization`.
"""


def create_cpu_utilization(
    meter, callbacks
):
    """Deprecated. Use `system.cpu.utilization` instead"""
    return meter.create_observable_gauge(
        name=CPU_UTILIZATION,
        callbacks=callbacks,
        description="Deprecated. Use `system.cpu.utilization` instead.",
        unit="1",
    )

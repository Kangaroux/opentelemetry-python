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
    UpDownCounter,
)

# pylint =invalid-name
CallbackT = Union[
    Callable,
    Generator,
]

PROCESS_CONTEXT_SWITCHES = "process.context_switches"
"""
Number of times the process has been context switched
Instrument
Unit: {context_switch}
"""


def create_process_context_switches(meter):
    """Number of times the process has been context switched"""
    return meter.create_counter(
        name=PROCESS_CONTEXT_SWITCHES,
        description="Number of times the process has been context switched.",
        unit="{context_switch}",
    )


PROCESS_CPU_TIME = "process.cpu.time"
"""
Total CPU seconds broken down by different states
Instrument
Unit
"""


def create_process_cpu_time(meter):
    """Total CPU seconds broken down by different states"""
    return meter.create_counter(
        name=PROCESS_CPU_TIME,
        description="Total CPU seconds broken down by different states.",
        unit="s",
    )


PROCESS_CPU_UTILIZATION = "process.cpu.utilization"
"""
Difference in process.cpu.time since the last measurement, divided by the elapsed time and number of CPUs available to the process
Instrument
Unit
"""


def create_process_cpu_utilization(
    meter, callbacks
):
    """Difference in process.cpu.time since the last measurement, divided by the elapsed time and number of CPUs available to the process"""
    return meter.create_observable_gauge(
        name=PROCESS_CPU_UTILIZATION,
        callbacks=callbacks,
        description="Difference in process.cpu.time since the last measurement, divided by the elapsed time and number of CPUs available to the process.",
        unit="1",
    )


PROCESS_DISK_IO = "process.disk.io"
"""
Disk bytes transferred
Instrument
Unit
"""


def create_process_disk_io(meter):
    """Disk bytes transferred"""
    return meter.create_counter(
        name=PROCESS_DISK_IO,
        description="Disk bytes transferred.",
        unit="By",
    )


PROCESS_MEMORY_USAGE = "process.memory.usage"
"""
The amount of physical memory in use
Instrument
Unit
"""


def create_process_memory_usage(meter):
    """The amount of physical memory in use"""
    return meter.create_up_down_counter(
        name=PROCESS_MEMORY_USAGE,
        description="The amount of physical memory in use.",
        unit="By",
    )


PROCESS_MEMORY_VIRTUAL = "process.memory.virtual"
"""
The amount of committed virtual memory
Instrument
Unit
"""


def create_process_memory_virtual(meter):
    """The amount of committed virtual memory"""
    return meter.create_up_down_counter(
        name=PROCESS_MEMORY_VIRTUAL,
        description="The amount of committed virtual memory.",
        unit="By",
    )


PROCESS_NETWORK_IO = "process.network.io"
"""
Network bytes transferred
Instrument
Unit
"""


def create_process_network_io(meter):
    """Network bytes transferred"""
    return meter.create_counter(
        name=PROCESS_NETWORK_IO,
        description="Network bytes transferred.",
        unit="By",
    )


PROCESS_OPEN_FILE_DESCRIPTOR_COUNT = (
    "process.open_file_descriptor.count"
)
"""
Deprecated: Replaced by `process.unix.file_descriptor.count`.
"""


def create_process_open_file_descriptor_count(meter):
    """Deprecated, use `process.unix.file_descriptor.count` instead"""
    return meter.create_up_down_counter(
        name=PROCESS_OPEN_FILE_DESCRIPTOR_COUNT,
        description="Deprecated, use `process.unix.file_descriptor.count` instead.",
        unit="{file_descriptor}",
    )


PROCESS_PAGING_FAULTS = "process.paging.faults"
"""
Number of page faults the process has made
Instrument
Unit: {fault}
"""


def create_process_paging_faults(meter):
    """Number of page faults the process has made"""
    return meter.create_counter(
        name=PROCESS_PAGING_FAULTS,
        description="Number of page faults the process has made.",
        unit="{fault}",
    )


PROCESS_THREAD_COUNT = "process.thread.count"
"""
Process threads count
Instrument
Unit: {thread}
"""


def create_process_thread_count(meter):
    """Process threads count"""
    return meter.create_up_down_counter(
        name=PROCESS_THREAD_COUNT,
        description="Process threads count.",
        unit="{thread}",
    )


PROCESS_UNIX_FILE_DESCRIPTOR_COUNT = (
    "process.unix.file_descriptor.count"
)
"""
Number of unix file descriptors in use by the process
Instrument
Unit: {file_descriptor}
"""


def create_process_unix_file_descriptor_count(meter):
    """Number of unix file descriptors in use by the process"""
    return meter.create_up_down_counter(
        name=PROCESS_UNIX_FILE_DESCRIPTOR_COUNT,
        description="Number of unix file descriptors in use by the process.",
        unit="{file_descriptor}",
    )


PROCESS_UPTIME = "process.uptime"
"""
The time the process has been running
Instrument
Unit
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_process_uptime(
    meter, callbacks
):
    """The time the process has been running"""
    return meter.create_observable_gauge(
        name=PROCESS_UPTIME,
        callbacks=callbacks,
        description="The time the process has been running.",
        unit="s",
    )


PROCESS_WINDOWS_HANDLE_COUNT = "process.windows.handle.count"
"""
Number of handles held by the process
Instrument
Unit: {handle}
"""


def create_process_windows_handle_count(meter):
    """Number of handles held by the process"""
    return meter.create_up_down_counter(
        name=PROCESS_WINDOWS_HANDLE_COUNT,
        description="Number of handles held by the process.",
        unit="{handle}",
    )

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

SYSTEM_CPU_FREQUENCY = "system.cpu.frequency"
"""
Operating frequency of the logical CPU in Hertz
Instrument
Unit
"""


def create_system_cpu_frequency(
    meter, callbacks
):
    """Operating frequency of the logical CPU in Hertz"""
    return meter.create_observable_gauge(
        name=SYSTEM_CPU_FREQUENCY,
        callbacks=callbacks,
        description="Operating frequency of the logical CPU in Hertz.",
        unit="Hz",
    )


SYSTEM_CPU_LOGICAL_COUNT = "system.cpu.logical.count"
"""
Reports the number of logical (virtual) processor cores created by the operating system to manage multitasking
Instrument
Unit: {cpu}
Note: Calculated by multiplying the number of sockets by the number of cores per socket, and then by the number of threads per core.
"""


def create_system_cpu_logical_count(meter):
    """Reports the number of logical (virtual) processor cores created by the operating system to manage multitasking"""
    return meter.create_up_down_counter(
        name=SYSTEM_CPU_LOGICAL_COUNT,
        description="Reports the number of logical (virtual) processor cores created by the operating system to manage multitasking.",
        unit="{cpu}",
    )


SYSTEM_CPU_PHYSICAL_COUNT = "system.cpu.physical.count"
"""
Reports the number of actual physical processor cores on the hardware
Instrument
Unit: {cpu}
Note: Calculated by multiplying the number of sockets by the number of cores per socket.
"""


def create_system_cpu_physical_count(meter):
    """Reports the number of actual physical processor cores on the hardware"""
    return meter.create_up_down_counter(
        name=SYSTEM_CPU_PHYSICAL_COUNT,
        description="Reports the number of actual physical processor cores on the hardware.",
        unit="{cpu}",
    )


SYSTEM_CPU_TIME = "system.cpu.time"
"""
Seconds each logical CPU spent on each mode
Instrument
Unit
"""


def create_system_cpu_time(meter):
    """Seconds each logical CPU spent on each mode"""
    return meter.create_counter(
        name=SYSTEM_CPU_TIME,
        description="Seconds each logical CPU spent on each mode.",
        unit="s",
    )


SYSTEM_CPU_UTILIZATION = "system.cpu.utilization"
"""
For each logical CPU, the utilization is calculated as the change in cumulative CPU time (cpu.time) over a measurement interval, divided by the elapsed time
Instrument
Unit
"""


def create_system_cpu_utilization(
    meter, callbacks
):
    """For each logical CPU, the utilization is calculated as the change in cumulative CPU time (cpu.time) over a measurement interval, divided by the elapsed time"""
    return meter.create_observable_gauge(
        name=SYSTEM_CPU_UTILIZATION,
        callbacks=callbacks,
        description="For each logical CPU, the utilization is calculated as the change in cumulative CPU time (cpu.time) over a measurement interval, divided by the elapsed time.",
        unit="1",
    )


SYSTEM_DISK_IO = "system.disk.io"
"""
Disk bytes transferred
Instrument
Unit
"""


def create_system_disk_io(meter):
    """Disk bytes transferred"""
    return meter.create_counter(
        name=SYSTEM_DISK_IO,
        description="Disk bytes transferred.",
        unit="By",
    )


SYSTEM_DISK_IO_TIME = "system.disk.io_time"
"""
Time disk spent activated
Instrument
Unit
Note: The real elapsed time ("wall clock") used in the I/O path (time from operations running in parallel are not counted). Measured as:

- Linux: Field 13 from [procfs-diskstats](https://www.kernel.org/doc/Documentation/ABI/testing/procfs-diskstats)
- Windows: The complement of
  ["Disk\\% Idle Time"](https://learn.microsoft.com/archive/blogs/askcore/windows-performance-monitor-disk-counters-explained#windows-performance-monitor-disk-counters-explained)
  performance counter: `uptime * (100 - "Disk\\% Idle Time") / 100`.
"""


def create_system_disk_io_time(meter):
    """Time disk spent activated"""
    return meter.create_counter(
        name=SYSTEM_DISK_IO_TIME,
        description="Time disk spent activated.",
        unit="s",
    )


SYSTEM_DISK_LIMIT = "system.disk.limit"
"""
The total storage capacity of the disk
Instrument
Unit
"""


def create_system_disk_limit(meter):
    """The total storage capacity of the disk"""
    return meter.create_up_down_counter(
        name=SYSTEM_DISK_LIMIT,
        description="The total storage capacity of the disk.",
        unit="By",
    )


SYSTEM_DISK_MERGED = "system.disk.merged"
"""
The number of disk reads/writes merged into single physical disk access operations
Instrument
Unit: {operation}
"""


def create_system_disk_merged(meter):
    """The number of disk reads/writes merged into single physical disk access operations"""
    return meter.create_counter(
        name=SYSTEM_DISK_MERGED,
        description="The number of disk reads/writes merged into single physical disk access operations.",
        unit="{operation}",
    )


SYSTEM_DISK_OPERATION_TIME = "system.disk.operation_time"
"""
Sum of the time each operation took to complete
Instrument
Unit
Note: Because it is the sum of time each request took, parallel-issued requests each contribute to make the count grow. Measured as:

- Linux: Fields 7 & 11 from [procfs-diskstats](https://www.kernel.org/doc/Documentation/ABI/testing/procfs-diskstats)
- Windows: "Avg. Disk sec/Read" perf counter multiplied by "Disk Reads/sec" perf counter (similar for Writes).
"""


def create_system_disk_operation_time(meter):
    """Sum of the time each operation took to complete"""
    return meter.create_counter(
        name=SYSTEM_DISK_OPERATION_TIME,
        description="Sum of the time each operation took to complete.",
        unit="s",
    )


SYSTEM_DISK_OPERATIONS = "system.disk.operations"
"""
Disk operations count
Instrument
Unit: {operation}
"""


def create_system_disk_operations(meter):
    """Disk operations count"""
    return meter.create_counter(
        name=SYSTEM_DISK_OPERATIONS,
        description="Disk operations count.",
        unit="{operation}",
    )


SYSTEM_FILESYSTEM_LIMIT = "system.filesystem.limit"
"""
The total storage capacity of the filesystem
Instrument
Unit
"""


def create_system_filesystem_limit(meter):
    """The total storage capacity of the filesystem"""
    return meter.create_up_down_counter(
        name=SYSTEM_FILESYSTEM_LIMIT,
        description="The total storage capacity of the filesystem.",
        unit="By",
    )


SYSTEM_FILESYSTEM_USAGE = "system.filesystem.usage"
"""
Reports a filesystem's space usage across different states
Instrument
Unit
Note: The sum of all `system.filesystem.usage` values over the different `system.filesystem.state` attributes
SHOULD equal the total storage capacity of the filesystem, that is `system.filesystem.limit`.
"""


def create_system_filesystem_usage(meter):
    """Reports a filesystem's space usage across different states"""
    return meter.create_up_down_counter(
        name=SYSTEM_FILESYSTEM_USAGE,
        description="Reports a filesystem's space usage across different states.",
        unit="By",
    )


SYSTEM_FILESYSTEM_UTILIZATION = "system.filesystem.utilization"
"""
Fraction of filesystem bytes used
Instrument
Unit
"""


def create_system_filesystem_utilization(
    meter, callbacks
):
    """Fraction of filesystem bytes used"""
    return meter.create_observable_gauge(
        name=SYSTEM_FILESYSTEM_UTILIZATION,
        callbacks=callbacks,
        description="Fraction of filesystem bytes used.",
        unit="1",
    )


SYSTEM_LINUX_MEMORY_AVAILABLE = "system.linux.memory.available"
"""
Deprecated: Replaced by `system.memory.linux.available`.
"""


def create_system_linux_memory_available(meter):
    """The number of packets transferred"""
    return meter.create_counter(
        name=SYSTEM_LINUX_MEMORY_AVAILABLE,
        description="The number of packets transferred.",
        unit="{packet}",
    )


SYSTEM_LINUX_MEMORY_SLAB_USAGE = "system.linux.memory.slab.usage"
"""
Deprecated: Replaced by `system.memory.linux.slab.usage`.
"""


def create_system_linux_memory_slab_usage(meter):
    """The number of packets transferred"""
    return meter.create_counter(
        name=SYSTEM_LINUX_MEMORY_SLAB_USAGE,
        description="The number of packets transferred.",
        unit="{packet}",
    )


SYSTEM_MEMORY_LIMIT = "system.memory.limit"
"""
Total virtual memory available in the system
Instrument
Unit
"""


def create_system_memory_limit(meter):
    """Total virtual memory available in the system"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_LIMIT,
        description="Total virtual memory available in the system.",
        unit="By",
    )


SYSTEM_MEMORY_LINUX_AVAILABLE = "system.memory.linux.available"
"""
An estimate of how much memory is available for starting new applications, without causing swapping
Instrument
Unit
Note: This is an alternative to `system.memory.usage` metric with `state=free`.
Linux starting from 3.14 exports "available" memory. It takes "free" memory as a baseline, and then factors in kernel-specific values.
This is supposed to be more accurate than just "free" memory.
For reference, see the calculations [here](https://superuser.com/a/980821).
See also `MemAvailable` in [/proc/meminfo](https://man7.org/linux/man-pages/man5/proc.5.html).
"""


def create_system_memory_linux_available(meter):
    """An estimate of how much memory is available for starting new applications, without causing swapping"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_LINUX_AVAILABLE,
        description="An estimate of how much memory is available for starting new applications, without causing swapping.",
        unit="By",
    )


SYSTEM_MEMORY_LINUX_SHARED = "system.memory.linux.shared"
"""
Shared memory used (mostly by tmpfs)
Instrument
Unit
Note: Equivalent of `shared` from [`free` command](https://man7.org/linux/man-pages/man1/free.1.html) or
`Shmem` from [`/proc/meminfo`](https://man7.org/linux/man-pages/man5/proc.5.html)".
"""


def create_system_memory_linux_shared(meter):
    """Shared memory used (mostly by tmpfs)"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_LINUX_SHARED,
        description="Shared memory used (mostly by tmpfs).",
        unit="By",
    )


SYSTEM_MEMORY_LINUX_SLAB_USAGE = "system.memory.linux.slab.usage"
"""
Reports the memory used by the Linux kernel for managing caches of frequently used objects
Instrument
Unit
Note: The sum over the `reclaimable` and `unreclaimable` state values in `memory.linux.slab.usage` SHOULD be equal to the total slab memory available on the system.
Note that the total slab memory is not constant and may vary over time.
See also the [Slab allocator](https://blogs.oracle.com/linux/post/understanding-linux-kernel-memory-statistics) and `Slab` in [/proc/meminfo](https://man7.org/linux/man-pages/man5/proc.5.html).
"""


def create_system_memory_linux_slab_usage(meter):
    """Reports the memory used by the Linux kernel for managing caches of frequently used objects"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_LINUX_SLAB_USAGE,
        description="Reports the memory used by the Linux kernel for managing caches of frequently used objects.",
        unit="By",
    )


SYSTEM_MEMORY_SHARED = "system.memory.shared"
"""
Deprecated: Replaced by `system.memory.linux.shared`.
"""


def create_system_memory_shared(meter):
    """Deprecated, use `system.memory.linux.shared` instead"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_SHARED,
        description="Deprecated, use `system.memory.linux.shared` instead.",
        unit="By",
    )


SYSTEM_MEMORY_USAGE = "system.memory.usage"
"""
Reports memory in use by state
Instrument
Unit
"""


def create_system_memory_usage(meter):
    """Reports memory in use by state"""
    return meter.create_up_down_counter(
        name=SYSTEM_MEMORY_USAGE,
        description="Reports memory in use by state.",
        unit="By",
    )


SYSTEM_MEMORY_UTILIZATION = "system.memory.utilization"
"""
Percentage of memory bytes in use
Instrument
Unit
"""


def create_system_memory_utilization(
    meter, callbacks
):
    """Percentage of memory bytes in use"""
    return meter.create_observable_gauge(
        name=SYSTEM_MEMORY_UTILIZATION,
        callbacks=callbacks,
        description="Percentage of memory bytes in use.",
        unit="1",
    )


SYSTEM_NETWORK_CONNECTION_COUNT = "system.network.connection.count"
"""
The number of connections
Instrument
Unit: {connection}
"""


def create_system_network_connection_count(meter):
    """The number of connections"""
    return meter.create_up_down_counter(
        name=SYSTEM_NETWORK_CONNECTION_COUNT,
        description="The number of connections.",
        unit="{connection}",
    )


SYSTEM_NETWORK_CONNECTIONS = "system.network.connections"
"""
Deprecated: Replaced by `system.network.connection.count`.
"""


def create_system_network_connections(meter):
    """Deprecated, use `system.network.connection.count` instead"""
    return meter.create_up_down_counter(
        name=SYSTEM_NETWORK_CONNECTIONS,
        description="Deprecated, use `system.network.connection.count` instead.",
        unit="{connection}",
    )


SYSTEM_NETWORK_DROPPED = "system.network.dropped"
"""
Deprecated: Replaced by `system.network.packet.dropped`.
"""


def create_system_network_dropped(meter):
    """Count of packets that are dropped or discarded even though there was no error"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_DROPPED,
        description="Count of packets that are dropped or discarded even though there was no error.",
        unit="{packet}",
    )


SYSTEM_NETWORK_ERRORS = "system.network.errors"
"""
Count of network errors detected
Instrument
Unit: {error}
Note: Measured as:

- Linux: the `errs` column in `/proc/net/dev` ([source](https://web.archive.org/web/20180321091318/http://www.onlamp.com/pub/a/linux/2000/11/16/LinuxAdmin.html)).
- Windows: [`InErrors`/`OutErrors`](https://docs.microsoft.com/windows/win32/api/netioapi/ns-netioapi-mib_if_row2)
  from [`GetIfEntry2`](https://docs.microsoft.com/windows/win32/api/netioapi/nf-netioapi-getifentry2).
"""


def create_system_network_errors(meter):
    """Count of network errors detected"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_ERRORS,
        description="Count of network errors detected.",
        unit="{error}",
    )


SYSTEM_NETWORK_IO = "system.network.io"
"""
The number of bytes transmitted and received
Instrument
Unit
"""


def create_system_network_io(meter):
    """The number of bytes transmitted and received"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_IO,
        description="The number of bytes transmitted and received.",
        unit="By",
    )


SYSTEM_NETWORK_PACKET_COUNT = "system.network.packet.count"
"""
The number of packets transferred
Instrument
Unit: {packet}
"""


def create_system_network_packet_count(meter):
    """The number of packets transferred"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_PACKET_COUNT,
        description="The number of packets transferred.",
        unit="{packet}",
    )


SYSTEM_NETWORK_PACKET_DROPPED = "system.network.packet.dropped"
"""
Count of packets that are dropped or discarded even though there was no error
Instrument
Unit: {packet}
Note: Measured as:

- Linux: the `drop` column in `/proc/net/dev` ([source](https://web.archive.org/web/20180321091318/http://www.onlamp.com/pub/a/linux/2000/11/16/LinuxAdmin.html))
- Windows: [`InDiscards`/`OutDiscards`](https://docs.microsoft.com/windows/win32/api/netioapi/ns-netioapi-mib_if_row2)
  from [`GetIfEntry2`](https://docs.microsoft.com/windows/win32/api/netioapi/nf-netioapi-getifentry2).
"""


def create_system_network_packet_dropped(meter):
    """Count of packets that are dropped or discarded even though there was no error"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_PACKET_DROPPED,
        description="Count of packets that are dropped or discarded even though there was no error.",
        unit="{packet}",
    )


SYSTEM_NETWORK_PACKETS = "system.network.packets"
"""
Deprecated: Replaced by `system.network.packet.count`.
"""


def create_system_network_packets(meter):
    """The number of packets transferred"""
    return meter.create_counter(
        name=SYSTEM_NETWORK_PACKETS,
        description="The number of packets transferred.",
        unit="{packet}",
    )


SYSTEM_PAGING_FAULTS = "system.paging.faults"
"""
The number of page faults
Instrument
Unit: {fault}
"""


def create_system_paging_faults(meter):
    """The number of page faults"""
    return meter.create_counter(
        name=SYSTEM_PAGING_FAULTS,
        description="The number of page faults.",
        unit="{fault}",
    )


SYSTEM_PAGING_OPERATIONS = "system.paging.operations"
"""
The number of paging operations
Instrument
Unit: {operation}
"""


def create_system_paging_operations(meter):
    """The number of paging operations"""
    return meter.create_counter(
        name=SYSTEM_PAGING_OPERATIONS,
        description="The number of paging operations.",
        unit="{operation}",
    )


SYSTEM_PAGING_USAGE = "system.paging.usage"
"""
Unix swap or windows pagefile usage
Instrument
Unit
"""


def create_system_paging_usage(meter):
    """Unix swap or windows pagefile usage"""
    return meter.create_up_down_counter(
        name=SYSTEM_PAGING_USAGE,
        description="Unix swap or windows pagefile usage.",
        unit="By",
    )


SYSTEM_PAGING_UTILIZATION = "system.paging.utilization"
"""
Swap (unix) or pagefile (windows) utilization
Instrument
Unit
"""


def create_system_paging_utilization(
    meter, callbacks
):
    """Swap (unix) or pagefile (windows) utilization"""
    return meter.create_observable_gauge(
        name=SYSTEM_PAGING_UTILIZATION,
        callbacks=callbacks,
        description="Swap (unix) or pagefile (windows) utilization.",
        unit="1",
    )


SYSTEM_PROCESS_COUNT = "system.process.count"
"""
Total number of processes in each state
Instrument
Unit: {process}
"""


def create_system_process_count(meter):
    """Total number of processes in each state"""
    return meter.create_up_down_counter(
        name=SYSTEM_PROCESS_COUNT,
        description="Total number of processes in each state.",
        unit="{process}",
    )


SYSTEM_PROCESS_CREATED = "system.process.created"
"""
Total number of processes created over uptime of the host
Instrument
Unit: {process}
"""


def create_system_process_created(meter):
    """Total number of processes created over uptime of the host"""
    return meter.create_counter(
        name=SYSTEM_PROCESS_CREATED,
        description="Total number of processes created over uptime of the host.",
        unit="{process}",
    )


SYSTEM_UPTIME = "system.uptime"
"""
The time the system has been running
Instrument
Unit
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_system_uptime(
    meter, callbacks
):
    """The time the system has been running"""
    return meter.create_observable_gauge(
        name=SYSTEM_UPTIME,
        callbacks=callbacks,
        description="The time the system has been running.",
        unit="s",
    )

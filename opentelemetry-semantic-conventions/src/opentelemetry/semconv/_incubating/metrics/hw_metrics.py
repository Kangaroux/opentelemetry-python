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

HW_BATTERY_CHARGE = "hw.battery.charge"
"""
Remaining fraction of battery charge
Instrument
Unit
"""


def create_hw_battery_charge(
    meter, callbacks
):
    """Remaining fraction of battery charge"""
    return meter.create_observable_gauge(
        name=HW_BATTERY_CHARGE,
        callbacks=callbacks,
        description="Remaining fraction of battery charge.",
        unit="1",
    )


HW_BATTERY_CHARGE_LIMIT = "hw.battery.charge.limit"
"""
Lower limit of battery charge fraction to ensure proper operation
Instrument
Unit
"""


def create_hw_battery_charge_limit(
    meter, callbacks
):
    """Lower limit of battery charge fraction to ensure proper operation"""
    return meter.create_observable_gauge(
        name=HW_BATTERY_CHARGE_LIMIT,
        callbacks=callbacks,
        description="Lower limit of battery charge fraction to ensure proper operation.",
        unit="1",
    )


HW_BATTERY_TIME_LEFT = "hw.battery.time_left"
"""
Time left before battery is completely charged or discharged
Instrument
Unit
"""


def create_hw_battery_time_left(
    meter, callbacks
):
    """Time left before battery is completely charged or discharged"""
    return meter.create_observable_gauge(
        name=HW_BATTERY_TIME_LEFT,
        callbacks=callbacks,
        description="Time left before battery is completely charged or discharged.",
        unit="s",
    )


HW_CPU_SPEED = "hw.cpu.speed"
"""
CPU current frequency
Instrument
Unit
"""


def create_hw_cpu_speed(
    meter, callbacks
):
    """CPU current frequency"""
    return meter.create_observable_gauge(
        name=HW_CPU_SPEED,
        callbacks=callbacks,
        description="CPU current frequency.",
        unit="Hz",
    )


HW_CPU_SPEED_LIMIT = "hw.cpu.speed.limit"
"""
CPU maximum frequency
Instrument
Unit
"""


def create_hw_cpu_speed_limit(
    meter, callbacks
):
    """CPU maximum frequency"""
    return meter.create_observable_gauge(
        name=HW_CPU_SPEED_LIMIT,
        callbacks=callbacks,
        description="CPU maximum frequency.",
        unit="Hz",
    )


HW_ENERGY = "hw.energy"
"""
Energy consumed by the component
Instrument
Unit
"""


def create_hw_energy(meter):
    """Energy consumed by the component"""
    return meter.create_counter(
        name=HW_ENERGY,
        description="Energy consumed by the component.",
        unit="J",
    )


HW_ERRORS = "hw.errors"
"""
Number of errors encountered by the component
Instrument
Unit: {error}
"""


def create_hw_errors(meter):
    """Number of errors encountered by the component"""
    return meter.create_counter(
        name=HW_ERRORS,
        description="Number of errors encountered by the component.",
        unit="{error}",
    )


HW_FAN_SPEED = "hw.fan.speed"
"""
Fan speed in revolutions per minute
Instrument
Unit
"""


def create_hw_fan_speed(
    meter, callbacks
):
    """Fan speed in revolutions per minute"""
    return meter.create_observable_gauge(
        name=HW_FAN_SPEED,
        callbacks=callbacks,
        description="Fan speed in revolutions per minute.",
        unit="rpm",
    )


HW_FAN_SPEED_LIMIT = "hw.fan.speed.limit"
"""
Speed limit in rpm
Instrument
Unit
"""


def create_hw_fan_speed_limit(
    meter, callbacks
):
    """Speed limit in rpm"""
    return meter.create_observable_gauge(
        name=HW_FAN_SPEED_LIMIT,
        callbacks=callbacks,
        description="Speed limit in rpm.",
        unit="rpm",
    )


HW_FAN_SPEED_RATIO = "hw.fan.speed_ratio"
"""
Fan speed expressed as a fraction of its maximum speed
Instrument
Unit
"""


def create_hw_fan_speed_ratio(
    meter, callbacks
):
    """Fan speed expressed as a fraction of its maximum speed"""
    return meter.create_observable_gauge(
        name=HW_FAN_SPEED_RATIO,
        callbacks=callbacks,
        description="Fan speed expressed as a fraction of its maximum speed.",
        unit="1",
    )


HW_GPU_IO = "hw.gpu.io"
"""
Received and transmitted bytes by the GPU
Instrument
Unit
"""


def create_hw_gpu_io(meter):
    """Received and transmitted bytes by the GPU"""
    return meter.create_counter(
        name=HW_GPU_IO,
        description="Received and transmitted bytes by the GPU.",
        unit="By",
    )


HW_GPU_MEMORY_LIMIT = "hw.gpu.memory.limit"
"""
Size of the GPU memory
Instrument
Unit
"""


def create_hw_gpu_memory_limit(meter):
    """Size of the GPU memory"""
    return meter.create_up_down_counter(
        name=HW_GPU_MEMORY_LIMIT,
        description="Size of the GPU memory.",
        unit="By",
    )


HW_GPU_MEMORY_USAGE = "hw.gpu.memory.usage"
"""
GPU memory used
Instrument
Unit
"""


def create_hw_gpu_memory_usage(meter):
    """GPU memory used"""
    return meter.create_up_down_counter(
        name=HW_GPU_MEMORY_USAGE,
        description="GPU memory used.",
        unit="By",
    )


HW_GPU_MEMORY_UTILIZATION = "hw.gpu.memory.utilization"
"""
Fraction of GPU memory used
Instrument
Unit
"""


def create_hw_gpu_memory_utilization(
    meter, callbacks
):
    """Fraction of GPU memory used"""
    return meter.create_observable_gauge(
        name=HW_GPU_MEMORY_UTILIZATION,
        callbacks=callbacks,
        description="Fraction of GPU memory used.",
        unit="1",
    )


HW_GPU_UTILIZATION = "hw.gpu.utilization"
"""
Fraction of time spent in a specific task
Instrument
Unit
"""


def create_hw_gpu_utilization(
    meter, callbacks
):
    """Fraction of time spent in a specific task"""
    return meter.create_observable_gauge(
        name=HW_GPU_UTILIZATION,
        callbacks=callbacks,
        description="Fraction of time spent in a specific task.",
        unit="1",
    )


HW_HOST_AMBIENT_TEMPERATURE = "hw.host.ambient_temperature"
"""
Ambient (external) temperature of the physical host
Instrument
Unit
"""


def create_hw_host_ambient_temperature(
    meter, callbacks
):
    """Ambient (external) temperature of the physical host"""
    return meter.create_observable_gauge(
        name=HW_HOST_AMBIENT_TEMPERATURE,
        callbacks=callbacks,
        description="Ambient (external) temperature of the physical host.",
        unit="Cel",
    )


HW_HOST_ENERGY = "hw.host.energy"
"""
Total energy consumed by the entire physical host, in joules
Instrument
Unit
Note: The overall energy usage of a host MUST be reported using the specific `hw.host.energy` and `hw.host.power` metrics **only**, instead of the generic `hw.energy` and `hw.power` described in the previous section, to prevent summing up overlapping values.
"""


def create_hw_host_energy(meter):
    """Total energy consumed by the entire physical host, in joules"""
    return meter.create_counter(
        name=HW_HOST_ENERGY,
        description="Total energy consumed by the entire physical host, in joules.",
        unit="J",
    )


HW_HOST_HEATING_MARGIN = "hw.host.heating_margin"
"""
By how many degrees Celsius the temperature of the physical host can be increased, before reaching a warning threshold on one of the internal sensors
Instrument
Unit
"""


def create_hw_host_heating_margin(
    meter, callbacks
):
    """By how many degrees Celsius the temperature of the physical host can be increased, before reaching a warning threshold on one of the internal sensors"""
    return meter.create_observable_gauge(
        name=HW_HOST_HEATING_MARGIN,
        callbacks=callbacks,
        description="By how many degrees Celsius the temperature of the physical host can be increased, before reaching a warning threshold on one of the internal sensors.",
        unit="Cel",
    )


HW_HOST_POWER = "hw.host.power"
"""
Instantaneous power consumed by the entire physical host in Watts (`hw.host.energy` is preferred)
Instrument
Unit
Note: The overall energy usage of a host MUST be reported using the specific `hw.host.energy` and `hw.host.power` metrics **only**, instead of the generic `hw.energy` and `hw.power` described in the previous section, to prevent summing up overlapping values.
"""


def create_hw_host_power(
    meter, callbacks
):
    """Instantaneous power consumed by the entire physical host in Watts (`hw.host.energy` is preferred)"""
    return meter.create_observable_gauge(
        name=HW_HOST_POWER,
        callbacks=callbacks,
        description="Instantaneous power consumed by the entire physical host in Watts (`hw.host.energy` is preferred).",
        unit="W",
    )


HW_LOGICAL_DISK_LIMIT = "hw.logical_disk.limit"
"""
Size of the logical disk
Instrument
Unit
"""


def create_hw_logical_disk_limit(meter):
    """Size of the logical disk"""
    return meter.create_up_down_counter(
        name=HW_LOGICAL_DISK_LIMIT,
        description="Size of the logical disk.",
        unit="By",
    )


HW_LOGICAL_DISK_USAGE = "hw.logical_disk.usage"
"""
Logical disk space usage
Instrument
Unit
"""


def create_hw_logical_disk_usage(meter):
    """Logical disk space usage"""
    return meter.create_up_down_counter(
        name=HW_LOGICAL_DISK_USAGE,
        description="Logical disk space usage.",
        unit="By",
    )


HW_LOGICAL_DISK_UTILIZATION = "hw.logical_disk.utilization"
"""
Logical disk space utilization as a fraction
Instrument
Unit
"""


def create_hw_logical_disk_utilization(
    meter, callbacks
):
    """Logical disk space utilization as a fraction"""
    return meter.create_observable_gauge(
        name=HW_LOGICAL_DISK_UTILIZATION,
        callbacks=callbacks,
        description="Logical disk space utilization as a fraction.",
        unit="1",
    )


HW_MEMORY_SIZE = "hw.memory.size"
"""
Size of the memory module
Instrument
Unit
"""


def create_hw_memory_size(meter):
    """Size of the memory module"""
    return meter.create_up_down_counter(
        name=HW_MEMORY_SIZE,
        description="Size of the memory module.",
        unit="By",
    )


HW_NETWORK_BANDWIDTH_LIMIT = "hw.network.bandwidth.limit"
"""
Link speed
Instrument
Unit: By/s
"""


def create_hw_network_bandwidth_limit(meter):
    """Link speed"""
    return meter.create_up_down_counter(
        name=HW_NETWORK_BANDWIDTH_LIMIT,
        description="Link speed.",
        unit="By/s",
    )


HW_NETWORK_BANDWIDTH_UTILIZATION = "hw.network.bandwidth.utilization"
"""
Utilization of the network bandwidth as a fraction
Instrument
Unit
"""


def create_hw_network_bandwidth_utilization(
    meter, callbacks
):
    """Utilization of the network bandwidth as a fraction"""
    return meter.create_observable_gauge(
        name=HW_NETWORK_BANDWIDTH_UTILIZATION,
        callbacks=callbacks,
        description="Utilization of the network bandwidth as a fraction.",
        unit="1",
    )


HW_NETWORK_IO = "hw.network.io"
"""
Received and transmitted network traffic in bytes
Instrument
Unit
"""


def create_hw_network_io(meter):
    """Received and transmitted network traffic in bytes"""
    return meter.create_counter(
        name=HW_NETWORK_IO,
        description="Received and transmitted network traffic in bytes.",
        unit="By",
    )


HW_NETWORK_PACKETS = "hw.network.packets"
"""
Received and transmitted network traffic in packets (or frames)
Instrument
Unit: {packet}
"""


def create_hw_network_packets(meter):
    """Received and transmitted network traffic in packets (or frames)"""
    return meter.create_counter(
        name=HW_NETWORK_PACKETS,
        description="Received and transmitted network traffic in packets (or frames).",
        unit="{packet}",
    )


HW_NETWORK_UP = "hw.network.up"
"""
Link status: `1` (up) or `0` (down)
Instrument
Unit
"""


def create_hw_network_up(meter):
    """Link status: `1` (up) or `0` (down)"""
    return meter.create_up_down_counter(
        name=HW_NETWORK_UP,
        description="Link status: `1` (up) or `0` (down).",
        unit="1",
    )


HW_PHYSICAL_DISK_ENDURANCE_UTILIZATION = (
    "hw.physical_disk.endurance_utilization"
)
"""
Endurance remaining for this SSD disk
Instrument
Unit
"""


def create_hw_physical_disk_endurance_utilization(
    meter, callbacks
):
    """Endurance remaining for this SSD disk"""
    return meter.create_observable_gauge(
        name=HW_PHYSICAL_DISK_ENDURANCE_UTILIZATION,
        callbacks=callbacks,
        description="Endurance remaining for this SSD disk.",
        unit="1",
    )


HW_PHYSICAL_DISK_SIZE = "hw.physical_disk.size"
"""
Size of the disk
Instrument
Unit
"""


def create_hw_physical_disk_size(meter):
    """Size of the disk"""
    return meter.create_up_down_counter(
        name=HW_PHYSICAL_DISK_SIZE,
        description="Size of the disk.",
        unit="By",
    )


HW_PHYSICAL_DISK_SMART = "hw.physical_disk.smart"
"""
Value of the corresponding [S.M.A.R.T.](https://wikipedia.org/wiki/S.M.A.R.T.) (Self-Monitoring, Analysis, and Reporting Technology) attribute
Instrument
Unit
"""


def create_hw_physical_disk_smart(
    meter, callbacks
):
    """Value of the corresponding [S.M.A.R.T.](https://wikipedia.org/wiki/S.M.A.R.T.) (Self-Monitoring, Analysis, and Reporting Technology) attribute"""
    return meter.create_observable_gauge(
        name=HW_PHYSICAL_DISK_SMART,
        callbacks=callbacks,
        description="Value of the corresponding [S.M.A.R.T.](https://wikipedia.org/wiki/S.M.A.R.T.) (Self-Monitoring, Analysis, and Reporting Technology) attribute.",
        unit="1",
    )


HW_POWER = "hw.power"
"""
Instantaneous power consumed by the component
Instrument
Unit
Note: It is recommended to report `hw.energy` instead of `hw.power` when possible.
"""


def create_hw_power(
    meter, callbacks
):
    """Instantaneous power consumed by the component"""
    return meter.create_observable_gauge(
        name=HW_POWER,
        callbacks=callbacks,
        description="Instantaneous power consumed by the component.",
        unit="W",
    )


HW_POWER_SUPPLY_LIMIT = "hw.power_supply.limit"
"""
Maximum power output of the power supply
Instrument
Unit
"""


def create_hw_power_supply_limit(meter):
    """Maximum power output of the power supply"""
    return meter.create_up_down_counter(
        name=HW_POWER_SUPPLY_LIMIT,
        description="Maximum power output of the power supply.",
        unit="W",
    )


HW_POWER_SUPPLY_USAGE = "hw.power_supply.usage"
"""
Current power output of the power supply
Instrument
Unit
"""


def create_hw_power_supply_usage(meter):
    """Current power output of the power supply"""
    return meter.create_up_down_counter(
        name=HW_POWER_SUPPLY_USAGE,
        description="Current power output of the power supply.",
        unit="W",
    )


HW_POWER_SUPPLY_UTILIZATION = "hw.power_supply.utilization"
"""
Utilization of the power supply as a fraction of its maximum output
Instrument
Unit
"""


def create_hw_power_supply_utilization(
    meter, callbacks
):
    """Utilization of the power supply as a fraction of its maximum output"""
    return meter.create_observable_gauge(
        name=HW_POWER_SUPPLY_UTILIZATION,
        callbacks=callbacks,
        description="Utilization of the power supply as a fraction of its maximum output.",
        unit="1",
    )


HW_STATUS = "hw.status"
"""
Operational status: `1` (true) or `0` (false) for each of the possible states
Instrument
Unit
Note: `hw.status` is currently specified as an *UpDownCounter* but would ideally be represented using a [*StateSet* as defined in OpenMetrics](https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#stateset). This semantic convention will be updated once *StateSet* is specified in OpenTelemetry. This planned change is not expected to have any consequence on the way users query their timeseries backend to retrieve the values of `hw.status` over time.
"""


def create_hw_status(meter):
    """Operational status: `1` (true) or `0` (false) for each of the possible states"""
    return meter.create_up_down_counter(
        name=HW_STATUS,
        description="Operational status: `1` (true) or `0` (false) for each of the possible states.",
        unit="1",
    )


HW_TAPE_DRIVE_OPERATIONS = "hw.tape_drive.operations"
"""
Operations performed by the tape drive
Instrument
Unit: {operation}
"""


def create_hw_tape_drive_operations(meter):
    """Operations performed by the tape drive"""
    return meter.create_counter(
        name=HW_TAPE_DRIVE_OPERATIONS,
        description="Operations performed by the tape drive.",
        unit="{operation}",
    )


HW_TEMPERATURE = "hw.temperature"
"""
Temperature in degrees Celsius
Instrument
Unit
"""


def create_hw_temperature(
    meter, callbacks
):
    """Temperature in degrees Celsius"""
    return meter.create_observable_gauge(
        name=HW_TEMPERATURE,
        callbacks=callbacks,
        description="Temperature in degrees Celsius.",
        unit="Cel",
    )


HW_TEMPERATURE_LIMIT = "hw.temperature.limit"
"""
Temperature limit in degrees Celsius
Instrument
Unit
"""


def create_hw_temperature_limit(
    meter, callbacks
):
    """Temperature limit in degrees Celsius"""
    return meter.create_observable_gauge(
        name=HW_TEMPERATURE_LIMIT,
        callbacks=callbacks,
        description="Temperature limit in degrees Celsius.",
        unit="Cel",
    )


HW_VOLTAGE = "hw.voltage"
"""
Voltage measured by the sensor
Instrument
Unit
"""


def create_hw_voltage(
    meter, callbacks
):
    """Voltage measured by the sensor"""
    return meter.create_observable_gauge(
        name=HW_VOLTAGE,
        callbacks=callbacks,
        description="Voltage measured by the sensor.",
        unit="V",
    )


HW_VOLTAGE_LIMIT = "hw.voltage.limit"
"""
Voltage limit in Volts
Instrument
Unit
"""


def create_hw_voltage_limit(
    meter, callbacks
):
    """Voltage limit in Volts"""
    return meter.create_observable_gauge(
        name=HW_VOLTAGE_LIMIT,
        callbacks=callbacks,
        description="Voltage limit in Volts.",
        unit="V",
    )


HW_VOLTAGE_NOMINAL = "hw.voltage.nominal"
"""
Nominal (expected) voltage
Instrument
Unit
"""


def create_hw_voltage_nominal(
    meter, callbacks
):
    """Nominal (expected) voltage"""
    return meter.create_observable_gauge(
        name=HW_VOLTAGE_NOMINAL,
        callbacks=callbacks,
        description="Nominal (expected) voltage.",
        unit="V",
    )

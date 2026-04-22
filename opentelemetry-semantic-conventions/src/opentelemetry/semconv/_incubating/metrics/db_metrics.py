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


from typing_extensions import Final

from opentelemetry.metrics import Counter, Histogram, Meter, UpDownCounter

DB_CLIENT_CONNECTION_COUNT = "db.client.connection.count"
"""
The number of connections that are currently in state described by the `state` attribute
Instrument
Unit: {connection}
"""


def create_db_client_connection_count(meter):
    """The number of connections that are currently in state described by the `state` attribute"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTION_COUNT,
        description="The number of connections that are currently in state described by the `state` attribute.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTION_CREATE_TIME = "db.client.connection.create_time"
"""
The time it took to create a new connection
Instrument
Unit
"""


def create_db_client_connection_create_time(meter):
    """The time it took to create a new connection"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTION_CREATE_TIME,
        description="The time it took to create a new connection.",
        unit="s",
    )


DB_CLIENT_CONNECTION_IDLE_MAX = "db.client.connection.idle.max"
"""
The maximum number of idle open connections allowed
Instrument
Unit: {connection}
"""


def create_db_client_connection_idle_max(meter):
    """The maximum number of idle open connections allowed"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTION_IDLE_MAX,
        description="The maximum number of idle open connections allowed.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTION_IDLE_MIN = "db.client.connection.idle.min"
"""
The minimum number of idle open connections allowed
Instrument
Unit: {connection}
"""


def create_db_client_connection_idle_min(meter):
    """The minimum number of idle open connections allowed"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTION_IDLE_MIN,
        description="The minimum number of idle open connections allowed.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTION_MAX = "db.client.connection.max"
"""
The maximum number of open connections allowed
Instrument
Unit: {connection}
"""


def create_db_client_connection_max(meter):
    """The maximum number of open connections allowed"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTION_MAX,
        description="The maximum number of open connections allowed.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTION_PENDING_REQUESTS = (
    "db.client.connection.pending_requests"
)
"""
The number of current pending requests for an open connection
Instrument
Unit: {request}
"""


def create_db_client_connection_pending_requests(
    meter
):
    """The number of current pending requests for an open connection"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTION_PENDING_REQUESTS,
        description="The number of current pending requests for an open connection.",
        unit="{request}",
    )


DB_CLIENT_CONNECTION_TIMEOUTS = "db.client.connection.timeouts"
"""
The number of connection timeouts that have occurred trying to obtain a connection from the pool
Instrument
Unit: {timeout}
"""


def create_db_client_connection_timeouts(meter):
    """The number of connection timeouts that have occurred trying to obtain a connection from the pool"""
    return meter.create_counter(
        name=DB_CLIENT_CONNECTION_TIMEOUTS,
        description="The number of connection timeouts that have occurred trying to obtain a connection from the pool.",
        unit="{timeout}",
    )


DB_CLIENT_CONNECTION_USE_TIME = "db.client.connection.use_time"
"""
The time between borrowing a connection and returning it to the pool
Instrument
Unit
"""


def create_db_client_connection_use_time(meter):
    """The time between borrowing a connection and returning it to the pool"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTION_USE_TIME,
        description="The time between borrowing a connection and returning it to the pool.",
        unit="s",
    )


DB_CLIENT_CONNECTION_WAIT_TIME = "db.client.connection.wait_time"
"""
The time it took to obtain an open connection from the pool
Instrument
Unit
"""


def create_db_client_connection_wait_time(meter):
    """The time it took to obtain an open connection from the pool"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTION_WAIT_TIME,
        description="The time it took to obtain an open connection from the pool.",
        unit="s",
    )


DB_CLIENT_CONNECTIONS_CREATE_TIME = "db.client.connections.create_time"
"""
Deprecated: Replaced by `db.client.connection.create_time` with unit `s`.
"""


def create_db_client_connections_create_time(meter):
    """Deprecated, use `db.client.connection.create_time` instead. Note: the unit also changed from `ms` to `s`"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTIONS_CREATE_TIME,
        description="Deprecated, use `db.client.connection.create_time` instead. Note: the unit also changed from `ms` to `s`.",
        unit="ms",
    )


DB_CLIENT_CONNECTIONS_IDLE_MAX = "db.client.connections.idle.max"
"""
Deprecated: Replaced by `db.client.connection.idle.max`.
"""


def create_db_client_connections_idle_max(meter):
    """Deprecated, use `db.client.connection.idle.max` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTIONS_IDLE_MAX,
        description="Deprecated, use `db.client.connection.idle.max` instead.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTIONS_IDLE_MIN = "db.client.connections.idle.min"
"""
Deprecated: Replaced by `db.client.connection.idle.min`.
"""


def create_db_client_connections_idle_min(meter):
    """Deprecated, use `db.client.connection.idle.min` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTIONS_IDLE_MIN,
        description="Deprecated, use `db.client.connection.idle.min` instead.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTIONS_MAX = "db.client.connections.max"
"""
Deprecated: Replaced by `db.client.connection.max`.
"""


def create_db_client_connections_max(meter):
    """Deprecated, use `db.client.connection.max` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTIONS_MAX,
        description="Deprecated, use `db.client.connection.max` instead.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTIONS_PENDING_REQUESTS = (
    "db.client.connections.pending_requests"
)
"""
Deprecated: Replaced by `db.client.connection.pending_requests`.
"""


def create_db_client_connections_pending_requests(
    meter
):
    """Deprecated, use `db.client.connection.pending_requests` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTIONS_PENDING_REQUESTS,
        description="Deprecated, use `db.client.connection.pending_requests` instead.",
        unit="{request}",
    )


DB_CLIENT_CONNECTIONS_TIMEOUTS = "db.client.connections.timeouts"
"""
Deprecated: Replaced by `db.client.connection.timeouts`.
"""


def create_db_client_connections_timeouts(meter):
    """Deprecated, use `db.client.connection.timeouts` instead"""
    return meter.create_counter(
        name=DB_CLIENT_CONNECTIONS_TIMEOUTS,
        description="Deprecated, use `db.client.connection.timeouts` instead.",
        unit="{timeout}",
    )


DB_CLIENT_CONNECTIONS_USAGE = "db.client.connections.usage"
"""
Deprecated: Replaced by `db.client.connection.count`.
"""


def create_db_client_connections_usage(meter):
    """Deprecated, use `db.client.connection.count` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_CONNECTIONS_USAGE,
        description="Deprecated, use `db.client.connection.count` instead.",
        unit="{connection}",
    )


DB_CLIENT_CONNECTIONS_USE_TIME = "db.client.connections.use_time"
"""
Deprecated: Replaced by `db.client.connection.use_time` with unit `s`.
"""


def create_db_client_connections_use_time(meter):
    """Deprecated, use `db.client.connection.use_time` instead. Note: the unit also changed from `ms` to `s`"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTIONS_USE_TIME,
        description="Deprecated, use `db.client.connection.use_time` instead. Note: the unit also changed from `ms` to `s`.",
        unit="ms",
    )


DB_CLIENT_CONNECTIONS_WAIT_TIME = "db.client.connections.wait_time"
"""
Deprecated: Replaced by `db.client.connection.wait_time` with unit `s`.
"""


def create_db_client_connections_wait_time(meter):
    """Deprecated, use `db.client.connection.wait_time` instead. Note: the unit also changed from `ms` to `s`"""
    return meter.create_histogram(
        name=DB_CLIENT_CONNECTIONS_WAIT_TIME,
        description="Deprecated, use `db.client.connection.wait_time` instead. Note: the unit also changed from `ms` to `s`.",
        unit="ms",
    )


DB_CLIENT_COSMOSDB_ACTIVE_INSTANCE_COUNT = (
    "db.client.cosmosdb.active_instance.count"
)
"""
Deprecated: Replaced by `azure.cosmosdb.client.active_instance.count`.
"""


def create_db_client_cosmosdb_active_instance_count(
    meter
):
    """Deprecated, use `azure.cosmosdb.client.active_instance.count` instead"""
    return meter.create_up_down_counter(
        name=DB_CLIENT_COSMOSDB_ACTIVE_INSTANCE_COUNT,
        description="Deprecated, use `azure.cosmosdb.client.active_instance.count` instead.",
        unit="{instance}",
    )


DB_CLIENT_COSMOSDB_OPERATION_REQUEST_CHARGE = (
    "db.client.cosmosdb.operation.request_charge"
)
"""
Deprecated: Replaced by `azure.cosmosdb.client.operation.request_charge`.
"""


def create_db_client_cosmosdb_operation_request_charge(
    meter
):
    """Deprecated, use `azure.cosmosdb.client.operation.request_charge` instead"""
    return meter.create_histogram(
        name=DB_CLIENT_COSMOSDB_OPERATION_REQUEST_CHARGE,
        description="Deprecated, use `azure.cosmosdb.client.operation.request_charge` instead.",
        unit="{request_unit}",
    )


DB_CLIENT_OPERATION_DURATION = "db.client.operation.duration"
"""
Deprecated in favor of stable :py:const:`opentelemetry.semconv.metrics.db_metrics.DB_CLIENT_OPERATION_DURATION`.
"""


def create_db_client_operation_duration(meter):
    """Duration of database client operations"""
    return meter.create_histogram(
        name=DB_CLIENT_OPERATION_DURATION,
        description="Duration of database client operations.",
        unit="s",
    )


DB_CLIENT_RESPONSE_RETURNED_ROWS = "db.client.response.returned_rows"
"""
The actual number of records returned by the database operation
Instrument
Unit: {row}
"""


def create_db_client_response_returned_rows(meter):
    """The actual number of records returned by the database operation"""
    return meter.create_histogram(
        name=DB_CLIENT_RESPONSE_RETURNED_ROWS,
        description="The actual number of records returned by the database operation.",
        unit="{row}",
    )

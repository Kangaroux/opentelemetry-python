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

from opentelemetry.metrics import Histogram, Meter, UpDownCounter

AZURE_COSMOSDB_CLIENT_ACTIVE_INSTANCE_COUNT = (
    "azure.cosmosdb.client.active_instance.count"
)
"""
Number of active client instances
Instrument
Unit: {instance}
"""


def create_azure_cosmosdb_client_active_instance_count(
    meter
):
    """Number of active client instances"""
    return meter.create_up_down_counter(
        name=AZURE_COSMOSDB_CLIENT_ACTIVE_INSTANCE_COUNT,
        description="Number of active client instances.",
        unit="{instance}",
    )


AZURE_COSMOSDB_CLIENT_OPERATION_REQUEST_CHARGE = (
    "azure.cosmosdb.client.operation.request_charge"
)
"""
[Request units](https://learn.microsoft.com/azure/cosmos-db/request-units) consumed by the operation
Instrument
Unit: {request_unit}
"""


def create_azure_cosmosdb_client_operation_request_charge(
    meter
):
    """[Request units](https://learn.microsoft.com/azure/cosmos-db/request-units) consumed by the operation"""
    return meter.create_histogram(
        name=AZURE_COSMOSDB_CLIENT_OPERATION_REQUEST_CHARGE,
        description="[Request units](https://learn.microsoft.com/azure/cosmos-db/request-units) consumed by the operation.",
        unit="{request_unit}",
    )

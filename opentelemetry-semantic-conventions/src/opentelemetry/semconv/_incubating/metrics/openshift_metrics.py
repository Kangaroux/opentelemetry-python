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

from opentelemetry.metrics import Meter, UpDownCounter

OPENSHIFT_CLUSTERQUOTA_CPU_LIMIT_HARD = (
    "openshift.clusterquota.cpu.limit.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_cpu_limit_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_CPU_LIMIT_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="{cpu}",
    )


OPENSHIFT_CLUSTERQUOTA_CPU_LIMIT_USED = (
    "openshift.clusterquota.cpu.limit.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_cpu_limit_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_CPU_LIMIT_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="{cpu}",
    )


OPENSHIFT_CLUSTERQUOTA_CPU_REQUEST_HARD = (
    "openshift.clusterquota.cpu.request.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_cpu_request_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_CPU_REQUEST_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="{cpu}",
    )


OPENSHIFT_CLUSTERQUOTA_CPU_REQUEST_USED = (
    "openshift.clusterquota.cpu.request.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_cpu_request_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_CPU_REQUEST_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="{cpu}",
    )


OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_LIMIT_HARD = (
    "openshift.clusterquota.ephemeral_storage.limit.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_ephemeral_storage_limit_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_LIMIT_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_LIMIT_USED = (
    "openshift.clusterquota.ephemeral_storage.limit.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_ephemeral_storage_limit_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_LIMIT_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_REQUEST_HARD = (
    "openshift.clusterquota.ephemeral_storage.request.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_ephemeral_storage_request_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_REQUEST_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_REQUEST_USED = (
    "openshift.clusterquota.ephemeral_storage.request.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_ephemeral_storage_request_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_EPHEMERAL_STORAGE_REQUEST_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_HUGEPAGE_COUNT_REQUEST_HARD = (
    "openshift.clusterquota.hugepage_count.request.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit: {hugepage}
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_hugepage_count_request_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_HUGEPAGE_COUNT_REQUEST_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="{hugepage}",
    )


OPENSHIFT_CLUSTERQUOTA_HUGEPAGE_COUNT_REQUEST_USED = (
    "openshift.clusterquota.hugepage_count.request.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit: {hugepage}
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_hugepage_count_request_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_HUGEPAGE_COUNT_REQUEST_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="{hugepage}",
    )


OPENSHIFT_CLUSTERQUOTA_MEMORY_LIMIT_HARD = (
    "openshift.clusterquota.memory.limit.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_memory_limit_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_MEMORY_LIMIT_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_MEMORY_LIMIT_USED = (
    "openshift.clusterquota.memory.limit.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_memory_limit_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_MEMORY_LIMIT_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_MEMORY_REQUEST_HARD = (
    "openshift.clusterquota.memory.request.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_memory_request_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_MEMORY_REQUEST_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_MEMORY_REQUEST_USED = (
    "openshift.clusterquota.memory.request.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_memory_request_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_MEMORY_REQUEST_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_OBJECT_COUNT_HARD = (
    "openshift.clusterquota.object_count.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit: {object}
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_object_count_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_OBJECT_COUNT_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="{object}",
    )


OPENSHIFT_CLUSTERQUOTA_OBJECT_COUNT_USED = (
    "openshift.clusterquota.object_count.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit: {object}
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).
"""


def create_openshift_clusterquota_object_count_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_OBJECT_COUNT_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="{object}",
    )


OPENSHIFT_CLUSTERQUOTA_PERSISTENTVOLUMECLAIM_COUNT_HARD = (
    "openshift.clusterquota.persistentvolumeclaim_count.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit: {persistentvolumeclaim}
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_openshift_clusterquota_persistentvolumeclaim_count_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_PERSISTENTVOLUMECLAIM_COUNT_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="{persistentvolumeclaim}",
    )


OPENSHIFT_CLUSTERQUOTA_PERSISTENTVOLUMECLAIM_COUNT_USED = (
    "openshift.clusterquota.persistentvolumeclaim_count.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit: {persistentvolumeclaim}
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_openshift_clusterquota_persistentvolumeclaim_count_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_PERSISTENTVOLUMECLAIM_COUNT_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="{persistentvolumeclaim}",
    )


OPENSHIFT_CLUSTERQUOTA_STORAGE_REQUEST_HARD = (
    "openshift.clusterquota.storage.request.hard"
)
"""
The enforced hard limit of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_openshift_clusterquota_storage_request_hard(
    meter
):
    """The enforced hard limit of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_STORAGE_REQUEST_HARD,
        description="The enforced hard limit of the resource across all projects.",
        unit="By",
    )


OPENSHIFT_CLUSTERQUOTA_STORAGE_REQUEST_USED = (
    "openshift.clusterquota.storage.request.used"
)
"""
The current observed total usage of the resource across all projects
Instrument
Unit
Note: This metric is retrieved from the `Status.Total.Used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core)
of the
[ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1#status-total).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_openshift_clusterquota_storage_request_used(
    meter
):
    """The current observed total usage of the resource across all projects"""
    return meter.create_up_down_counter(
        name=OPENSHIFT_CLUSTERQUOTA_STORAGE_REQUEST_USED,
        description="The current observed total usage of the resource across all projects.",
        unit="By",
    )

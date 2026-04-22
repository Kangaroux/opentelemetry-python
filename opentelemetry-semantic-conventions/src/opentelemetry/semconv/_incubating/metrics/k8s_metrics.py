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

K8S_CONTAINER_CPU_LIMIT = "k8s.container.cpu.limit"
"""
Maximum CPU resource limit set for the container
Instrument
Unit: {cpu}
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_cpu_limit(meter):
    """Maximum CPU resource limit set for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_CPU_LIMIT,
        description="Maximum CPU resource limit set for the container.",
        unit="{cpu}",
    )


K8S_CONTAINER_CPU_LIMIT_UTILIZATION = (
    "k8s.container.cpu.limit_utilization"
)
"""
The ratio of container CPU usage to its CPU limit
Instrument
Unit
Note: The value range is [0.0,1.0]. A value of 1.0 means the container is using 100% of its CPU limit. If the CPU limit is not set, this metric SHOULD NOT be emitted for that container.
"""


def create_k8s_container_cpu_limit_utilization(
    meter, callbacks
):
    """The ratio of container CPU usage to its CPU limit"""
    return meter.create_observable_gauge(
        name=K8S_CONTAINER_CPU_LIMIT_UTILIZATION,
        callbacks=callbacks,
        description="The ratio of container CPU usage to its CPU limit.",
        unit="1",
    )


K8S_CONTAINER_CPU_REQUEST = "k8s.container.cpu.request"
"""
CPU resource requested for the container
Instrument
Unit: {cpu}
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_cpu_request(meter):
    """CPU resource requested for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_CPU_REQUEST,
        description="CPU resource requested for the container.",
        unit="{cpu}",
    )


K8S_CONTAINER_CPU_REQUEST_UTILIZATION = (
    "k8s.container.cpu.request_utilization"
)
"""
The ratio of container CPU usage to its CPU request
Instrument
Unit
"""


def create_k8s_container_cpu_request_utilization(
    meter, callbacks
):
    """The ratio of container CPU usage to its CPU request"""
    return meter.create_observable_gauge(
        name=K8S_CONTAINER_CPU_REQUEST_UTILIZATION,
        callbacks=callbacks,
        description="The ratio of container CPU usage to its CPU request.",
        unit="1",
    )


K8S_CONTAINER_EPHEMERAL_STORAGE_LIMIT = (
    "k8s.container.ephemeral_storage.limit"
)
"""
Maximum ephemeral storage resource limit set for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_ephemeral_storage_limit(
    meter
):
    """Maximum ephemeral storage resource limit set for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_EPHEMERAL_STORAGE_LIMIT,
        description="Maximum ephemeral storage resource limit set for the container.",
        unit="By",
    )


K8S_CONTAINER_EPHEMERAL_STORAGE_REQUEST = (
    "k8s.container.ephemeral_storage.request"
)
"""
Ephemeral storage resource requested for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_ephemeral_storage_request(
    meter
):
    """Ephemeral storage resource requested for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_EPHEMERAL_STORAGE_REQUEST,
        description="Ephemeral storage resource requested for the container.",
        unit="By",
    )


K8S_CONTAINER_MEMORY_LIMIT = "k8s.container.memory.limit"
"""
Maximum memory resource limit set for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_memory_limit(meter):
    """Maximum memory resource limit set for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_MEMORY_LIMIT,
        description="Maximum memory resource limit set for the container.",
        unit="By",
    )


K8S_CONTAINER_MEMORY_REQUEST = "k8s.container.memory.request"
"""
Memory resource requested for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_memory_request(meter):
    """Memory resource requested for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_MEMORY_REQUEST,
        description="Memory resource requested for the container.",
        unit="By",
    )


K8S_CONTAINER_READY = "k8s.container.ready"
"""
Indicates whether the container is currently marked as ready to accept traffic, based on its readiness probe (1 = ready, 0 = not ready)
Instrument
Unit: {container}
Note: This metric SHOULD reflect the value of the `ready` field in the
[K8s ContainerStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#containerstatus-v1-core).
"""


def create_k8s_container_ready(meter):
    """Indicates whether the container is currently marked as ready to accept traffic, based on its readiness probe (1 = ready, 0 = not ready)"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_READY,
        description="Indicates whether the container is currently marked as ready to accept traffic, based on its readiness probe (1 = ready, 0 = not ready).",
        unit="{container}",
    )


K8S_CONTAINER_RESTART_COUNT = "k8s.container.restart.count"
"""
Describes how many times the container has restarted (since the last counter reset)
Instrument
Unit: {restart}
Note: This value is pulled directly from the K8s API and the value can go indefinitely high and be reset to 0
at any time depending on how your kubelet is configured to prune dead containers.
It is best to not depend too much on the exact value but rather look at it as
either == 0, in which case you can conclude there were no restarts in the recent past, or > 0, in which case
you can conclude there were restarts in the recent past, and not try and analyze the value beyond that.
"""


def create_k8s_container_restart_count(meter):
    """Describes how many times the container has restarted (since the last counter reset)"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_RESTART_COUNT,
        description="Describes how many times the container has restarted (since the last counter reset).",
        unit="{restart}",
    )


K8S_CONTAINER_STATUS_REASON = "k8s.container.status.reason"
"""
Describes the number of K8s containers that are currently in a state for a given reason
Instrument
Unit: {container}
Note: All possible container state reasons will be reported at each time interval to avoid missing metrics.
Only the value corresponding to the current state reason will be non-zero.
"""


def create_k8s_container_status_reason(meter):
    """Describes the number of K8s containers that are currently in a state for a given reason"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_STATUS_REASON,
        description="Describes the number of K8s containers that are currently in a state for a given reason.",
        unit="{container}",
    )


K8S_CONTAINER_STATUS_STATE = "k8s.container.status.state"
"""
Describes the number of K8s containers that are currently in a given state
Instrument
Unit: {container}
Note: All possible container states will be reported at each time interval to avoid missing metrics.
Only the value corresponding to the current state will be non-zero.
"""


def create_k8s_container_status_state(meter):
    """Describes the number of K8s containers that are currently in a given state"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_STATUS_STATE,
        description="Describes the number of K8s containers that are currently in a given state.",
        unit="{container}",
    )


K8S_CONTAINER_STORAGE_LIMIT = "k8s.container.storage.limit"
"""
Maximum storage resource limit set for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_storage_limit(meter):
    """Maximum storage resource limit set for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_STORAGE_LIMIT,
        description="Maximum storage resource limit set for the container.",
        unit="By",
    )


K8S_CONTAINER_STORAGE_REQUEST = "k8s.container.storage.request"
"""
Storage resource requested for the container
Instrument
Unit
Note: See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#resourcerequirements-v1-core for details.
"""


def create_k8s_container_storage_request(meter):
    """Storage resource requested for the container"""
    return meter.create_up_down_counter(
        name=K8S_CONTAINER_STORAGE_REQUEST,
        description="Storage resource requested for the container.",
        unit="By",
    )


K8S_CRONJOB_ACTIVE_JOBS = "k8s.cronjob.active_jobs"
"""
Deprecated: Replaced by `k8s.cronjob.job.active`.
"""


def create_k8s_cronjob_active_jobs(meter):
    """Deprecated, use `k8s.cronjob.job.active` instead"""
    return meter.create_up_down_counter(
        name=K8S_CRONJOB_ACTIVE_JOBS,
        description="Deprecated, use `k8s.cronjob.job.active` instead.",
        unit="{job}",
    )


K8S_CRONJOB_JOB_ACTIVE = "k8s.cronjob.job.active"
"""
The number of actively running jobs for a cronjob
Instrument
Unit: {job}
Note: This metric aligns with the `active` field of the
[K8s CronJobStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#cronjobstatus-v1-batch).
"""


def create_k8s_cronjob_job_active(meter):
    """The number of actively running jobs for a cronjob"""
    return meter.create_up_down_counter(
        name=K8S_CRONJOB_JOB_ACTIVE,
        description="The number of actively running jobs for a cronjob.",
        unit="{job}",
    )


K8S_DAEMONSET_CURRENT_SCHEDULED_NODES = (
    "k8s.daemonset.current_scheduled_nodes"
)
"""
Deprecated: Replaced by `k8s.daemonset.node.current_scheduled`.
"""


def create_k8s_daemonset_current_scheduled_nodes(
    meter
):
    """Deprecated, use `k8s.daemonset.node.current_scheduled` instead"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_CURRENT_SCHEDULED_NODES,
        description="Deprecated, use `k8s.daemonset.node.current_scheduled` instead.",
        unit="{node}",
    )


K8S_DAEMONSET_DESIRED_SCHEDULED_NODES = (
    "k8s.daemonset.desired_scheduled_nodes"
)
"""
Deprecated: Replaced by `k8s.daemonset.node.desired_scheduled`.
"""


def create_k8s_daemonset_desired_scheduled_nodes(
    meter
):
    """Deprecated, use `k8s.daemonset.node.desired_scheduled` instead"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_DESIRED_SCHEDULED_NODES,
        description="Deprecated, use `k8s.daemonset.node.desired_scheduled` instead.",
        unit="{node}",
    )


K8S_DAEMONSET_MISSCHEDULED_NODES = "k8s.daemonset.misscheduled_nodes"
"""
Deprecated: Replaced by `k8s.daemonset.node.misscheduled`.
"""


def create_k8s_daemonset_misscheduled_nodes(meter):
    """Deprecated, use `k8s.daemonset.node.misscheduled` instead"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_MISSCHEDULED_NODES,
        description="Deprecated, use `k8s.daemonset.node.misscheduled` instead.",
        unit="{node}",
    )


K8S_DAEMONSET_NODE_CURRENT_SCHEDULED = (
    "k8s.daemonset.node.current_scheduled"
)
"""
Number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod
Instrument
Unit: {node}
Note: This metric aligns with the `currentNumberScheduled` field of the
[K8s DaemonSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#daemonsetstatus-v1-apps).
"""


def create_k8s_daemonset_node_current_scheduled(meter):
    """Number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_NODE_CURRENT_SCHEDULED,
        description="Number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod.",
        unit="{node}",
    )


K8S_DAEMONSET_NODE_DESIRED_SCHEDULED = (
    "k8s.daemonset.node.desired_scheduled"
)
"""
Number of nodes that should be running the daemon pod (including nodes currently running the daemon pod)
Instrument
Unit: {node}
Note: This metric aligns with the `desiredNumberScheduled` field of the
[K8s DaemonSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#daemonsetstatus-v1-apps).
"""


def create_k8s_daemonset_node_desired_scheduled(meter):
    """Number of nodes that should be running the daemon pod (including nodes currently running the daemon pod)"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_NODE_DESIRED_SCHEDULED,
        description="Number of nodes that should be running the daemon pod (including nodes currently running the daemon pod).",
        unit="{node}",
    )


K8S_DAEMONSET_NODE_MISSCHEDULED = "k8s.daemonset.node.misscheduled"
"""
Number of nodes that are running the daemon pod, but are not supposed to run the daemon pod
Instrument
Unit: {node}
Note: This metric aligns with the `numberMisscheduled` field of the
[K8s DaemonSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#daemonsetstatus-v1-apps).
"""


def create_k8s_daemonset_node_misscheduled(meter):
    """Number of nodes that are running the daemon pod, but are not supposed to run the daemon pod"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_NODE_MISSCHEDULED,
        description="Number of nodes that are running the daemon pod, but are not supposed to run the daemon pod.",
        unit="{node}",
    )


K8S_DAEMONSET_NODE_READY = "k8s.daemonset.node.ready"
"""
Number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready
Instrument
Unit: {node}
Note: This metric aligns with the `numberReady` field of the
[K8s DaemonSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#daemonsetstatus-v1-apps).
"""


def create_k8s_daemonset_node_ready(meter):
    """Number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_NODE_READY,
        description="Number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.",
        unit="{node}",
    )


K8S_DAEMONSET_READY_NODES = "k8s.daemonset.ready_nodes"
"""
Deprecated: Replaced by `k8s.daemonset.node.ready`.
"""


def create_k8s_daemonset_ready_nodes(meter):
    """Deprecated, use `k8s.daemonset.node.ready` instead"""
    return meter.create_up_down_counter(
        name=K8S_DAEMONSET_READY_NODES,
        description="Deprecated, use `k8s.daemonset.node.ready` instead.",
        unit="{node}",
    )


K8S_DEPLOYMENT_AVAILABLE_PODS = "k8s.deployment.available_pods"
"""
Deprecated: Replaced by `k8s.deployment.pod.available`.
"""


def create_k8s_deployment_available_pods(meter):
    """Deprecated, use `k8s.deployment.pod.available` instead"""
    return meter.create_up_down_counter(
        name=K8S_DEPLOYMENT_AVAILABLE_PODS,
        description="Deprecated, use `k8s.deployment.pod.available` instead.",
        unit="{pod}",
    )


K8S_DEPLOYMENT_DESIRED_PODS = "k8s.deployment.desired_pods"
"""
Deprecated: Replaced by `k8s.deployment.pod.desired`.
"""


def create_k8s_deployment_desired_pods(meter):
    """Deprecated, use `k8s.deployment.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_DEPLOYMENT_DESIRED_PODS,
        description="Deprecated, use `k8s.deployment.pod.desired` instead.",
        unit="{pod}",
    )


K8S_DEPLOYMENT_POD_AVAILABLE = "k8s.deployment.pod.available"
"""
Total number of available replica pods (ready for at least minReadySeconds) targeted by this deployment
Instrument
Unit: {pod}
Note: This metric aligns with the `availableReplicas` field of the
[K8s DeploymentStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#deploymentstatus-v1-apps).
"""


def create_k8s_deployment_pod_available(meter):
    """Total number of available replica pods (ready for at least minReadySeconds) targeted by this deployment"""
    return meter.create_up_down_counter(
        name=K8S_DEPLOYMENT_POD_AVAILABLE,
        description="Total number of available replica pods (ready for at least minReadySeconds) targeted by this deployment.",
        unit="{pod}",
    )


K8S_DEPLOYMENT_POD_DESIRED = "k8s.deployment.pod.desired"
"""
Number of desired replica pods in this deployment
Instrument
Unit: {pod}
Note: This metric aligns with the `replicas` field of the
[K8s DeploymentSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#deploymentspec-v1-apps).
"""


def create_k8s_deployment_pod_desired(meter):
    """Number of desired replica pods in this deployment"""
    return meter.create_up_down_counter(
        name=K8S_DEPLOYMENT_POD_DESIRED,
        description="Number of desired replica pods in this deployment.",
        unit="{pod}",
    )


K8S_HPA_CURRENT_PODS = "k8s.hpa.current_pods"
"""
Deprecated: Replaced by `k8s.hpa.pod.current`.
"""


def create_k8s_hpa_current_pods(meter):
    """Deprecated, use `k8s.hpa.pod.current` instead"""
    return meter.create_up_down_counter(
        name=K8S_HPA_CURRENT_PODS,
        description="Deprecated, use `k8s.hpa.pod.current` instead.",
        unit="{pod}",
    )


K8S_HPA_DESIRED_PODS = "k8s.hpa.desired_pods"
"""
Deprecated: Replaced by `k8s.hpa.pod.desired`.
"""


def create_k8s_hpa_desired_pods(meter):
    """Deprecated, use `k8s.hpa.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_HPA_DESIRED_PODS,
        description="Deprecated, use `k8s.hpa.pod.desired` instead.",
        unit="{pod}",
    )


K8S_HPA_MAX_PODS = "k8s.hpa.max_pods"
"""
Deprecated: Replaced by `k8s.hpa.pod.max`.
"""


def create_k8s_hpa_max_pods(meter):
    """Deprecated, use `k8s.hpa.pod.max` instead"""
    return meter.create_up_down_counter(
        name=K8S_HPA_MAX_PODS,
        description="Deprecated, use `k8s.hpa.pod.max` instead.",
        unit="{pod}",
    )


K8S_HPA_METRIC_TARGET_CPU_AVERAGE_UTILIZATION = (
    "k8s.hpa.metric.target.cpu.average_utilization"
)
"""
Target average utilization, in percentage, for CPU resource in HPA config
Instrument
Unit
Note: This metric aligns with the `averageUtilization` field of the
[K8s HPA MetricTarget](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#metrictarget-v2-autoscaling).
If the type of the metric is [`ContainerResource`](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis),
the `k8s.container.name` attribute MUST be set to identify the specific container within the pod to which the metric applies.
"""


def create_k8s_hpa_metric_target_cpu_average_utilization(
    meter, callbacks
):
    """Target average utilization, in percentage, for CPU resource in HPA config"""
    return meter.create_observable_gauge(
        name=K8S_HPA_METRIC_TARGET_CPU_AVERAGE_UTILIZATION,
        callbacks=callbacks,
        description="Target average utilization, in percentage, for CPU resource in HPA config.",
        unit="1",
    )


K8S_HPA_METRIC_TARGET_CPU_AVERAGE_VALUE = (
    "k8s.hpa.metric.target.cpu.average_value"
)
"""
Target average value for CPU resource in HPA config
Instrument
Unit: {cpu}
Note: This metric aligns with the `averageValue` field of the
[K8s HPA MetricTarget](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#metrictarget-v2-autoscaling).
If the type of the metric is [`ContainerResource`](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis),
the `k8s.container.name` attribute MUST be set to identify the specific container within the pod to which the metric applies.
"""


def create_k8s_hpa_metric_target_cpu_average_value(
    meter, callbacks
):
    """Target average value for CPU resource in HPA config"""
    return meter.create_observable_gauge(
        name=K8S_HPA_METRIC_TARGET_CPU_AVERAGE_VALUE,
        callbacks=callbacks,
        description="Target average value for CPU resource in HPA config.",
        unit="{cpu}",
    )


K8S_HPA_METRIC_TARGET_CPU_VALUE = "k8s.hpa.metric.target.cpu.value"
"""
Target value for CPU resource in HPA config
Instrument
Unit: {cpu}
Note: This metric aligns with the `value` field of the
[K8s HPA MetricTarget](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#metrictarget-v2-autoscaling).
If the type of the metric is [`ContainerResource`](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis),
the `k8s.container.name` attribute MUST be set to identify the specific container within the pod to which the metric applies.
"""


def create_k8s_hpa_metric_target_cpu_value(
    meter, callbacks
):
    """Target value for CPU resource in HPA config"""
    return meter.create_observable_gauge(
        name=K8S_HPA_METRIC_TARGET_CPU_VALUE,
        callbacks=callbacks,
        description="Target value for CPU resource in HPA config.",
        unit="{cpu}",
    )


K8S_HPA_MIN_PODS = "k8s.hpa.min_pods"
"""
Deprecated: Replaced by `k8s.hpa.pod.min`.
"""


def create_k8s_hpa_min_pods(meter):
    """Deprecated, use `k8s.hpa.pod.min` instead"""
    return meter.create_up_down_counter(
        name=K8S_HPA_MIN_PODS,
        description="Deprecated, use `k8s.hpa.pod.min` instead.",
        unit="{pod}",
    )


K8S_HPA_POD_CURRENT = "k8s.hpa.pod.current"
"""
Current number of replica pods managed by this horizontal pod autoscaler, as last seen by the autoscaler
Instrument
Unit: {pod}
Note: This metric aligns with the `currentReplicas` field of the
[K8s HorizontalPodAutoscalerStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscalerstatus-v2-autoscaling).
"""


def create_k8s_hpa_pod_current(meter):
    """Current number of replica pods managed by this horizontal pod autoscaler, as last seen by the autoscaler"""
    return meter.create_up_down_counter(
        name=K8S_HPA_POD_CURRENT,
        description="Current number of replica pods managed by this horizontal pod autoscaler, as last seen by the autoscaler.",
        unit="{pod}",
    )


K8S_HPA_POD_DESIRED = "k8s.hpa.pod.desired"
"""
Desired number of replica pods managed by this horizontal pod autoscaler, as last calculated by the autoscaler
Instrument
Unit: {pod}
Note: This metric aligns with the `desiredReplicas` field of the
[K8s HorizontalPodAutoscalerStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscalerstatus-v2-autoscaling).
"""


def create_k8s_hpa_pod_desired(meter):
    """Desired number of replica pods managed by this horizontal pod autoscaler, as last calculated by the autoscaler"""
    return meter.create_up_down_counter(
        name=K8S_HPA_POD_DESIRED,
        description="Desired number of replica pods managed by this horizontal pod autoscaler, as last calculated by the autoscaler.",
        unit="{pod}",
    )


K8S_HPA_POD_MAX = "k8s.hpa.pod.max"
"""
The upper limit for the number of replica pods to which the autoscaler can scale up
Instrument
Unit: {pod}
Note: This metric aligns with the `maxReplicas` field of the
[K8s HorizontalPodAutoscalerSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscalerspec-v2-autoscaling).
"""


def create_k8s_hpa_pod_max(meter):
    """The upper limit for the number of replica pods to which the autoscaler can scale up"""
    return meter.create_up_down_counter(
        name=K8S_HPA_POD_MAX,
        description="The upper limit for the number of replica pods to which the autoscaler can scale up.",
        unit="{pod}",
    )


K8S_HPA_POD_MIN = "k8s.hpa.pod.min"
"""
The lower limit for the number of replica pods to which the autoscaler can scale down
Instrument
Unit: {pod}
Note: This metric aligns with the `minReplicas` field of the
[K8s HorizontalPodAutoscalerSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#horizontalpodautoscalerspec-v2-autoscaling).
"""


def create_k8s_hpa_pod_min(meter):
    """The lower limit for the number of replica pods to which the autoscaler can scale down"""
    return meter.create_up_down_counter(
        name=K8S_HPA_POD_MIN,
        description="The lower limit for the number of replica pods to which the autoscaler can scale down.",
        unit="{pod}",
    )


K8S_JOB_ACTIVE_PODS = "k8s.job.active_pods"
"""
Deprecated: Replaced by `k8s.job.pod.active`.
"""


def create_k8s_job_active_pods(meter):
    """Deprecated, use `k8s.job.pod.active` instead"""
    return meter.create_up_down_counter(
        name=K8S_JOB_ACTIVE_PODS,
        description="Deprecated, use `k8s.job.pod.active` instead.",
        unit="{pod}",
    )


K8S_JOB_DESIRED_SUCCESSFUL_PODS = "k8s.job.desired_successful_pods"
"""
Deprecated: Replaced by `k8s.job.pod.desired_successful`.
"""


def create_k8s_job_desired_successful_pods(meter):
    """Deprecated, use `k8s.job.pod.desired_successful` instead"""
    return meter.create_up_down_counter(
        name=K8S_JOB_DESIRED_SUCCESSFUL_PODS,
        description="Deprecated, use `k8s.job.pod.desired_successful` instead.",
        unit="{pod}",
    )


K8S_JOB_FAILED_PODS = "k8s.job.failed_pods"
"""
Deprecated: Replaced by `k8s.job.pod.failed`.
"""


def create_k8s_job_failed_pods(meter):
    """Deprecated, use `k8s.job.pod.failed` instead"""
    return meter.create_up_down_counter(
        name=K8S_JOB_FAILED_PODS,
        description="Deprecated, use `k8s.job.pod.failed` instead.",
        unit="{pod}",
    )


K8S_JOB_MAX_PARALLEL_PODS = "k8s.job.max_parallel_pods"
"""
Deprecated: Replaced by `k8s.job.pod.max_parallel`.
"""


def create_k8s_job_max_parallel_pods(meter):
    """Deprecated, use `k8s.job.pod.max_parallel` instead"""
    return meter.create_up_down_counter(
        name=K8S_JOB_MAX_PARALLEL_PODS,
        description="Deprecated, use `k8s.job.pod.max_parallel` instead.",
        unit="{pod}",
    )


K8S_JOB_POD_ACTIVE = "k8s.job.pod.active"
"""
The number of pending and actively running pods for a job
Instrument
Unit: {pod}
Note: This metric aligns with the `active` field of the
[K8s JobStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#jobstatus-v1-batch).
"""


def create_k8s_job_pod_active(meter):
    """The number of pending and actively running pods for a job"""
    return meter.create_up_down_counter(
        name=K8S_JOB_POD_ACTIVE,
        description="The number of pending and actively running pods for a job.",
        unit="{pod}",
    )


K8S_JOB_POD_DESIRED_SUCCESSFUL = "k8s.job.pod.desired_successful"
"""
The desired number of successfully finished pods the job should be run with
Instrument
Unit: {pod}
Note: This metric aligns with the `completions` field of the
[K8s JobSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#jobspec-v1-batch).
"""


def create_k8s_job_pod_desired_successful(meter):
    """The desired number of successfully finished pods the job should be run with"""
    return meter.create_up_down_counter(
        name=K8S_JOB_POD_DESIRED_SUCCESSFUL,
        description="The desired number of successfully finished pods the job should be run with.",
        unit="{pod}",
    )


K8S_JOB_POD_FAILED = "k8s.job.pod.failed"
"""
The number of pods which reached phase Failed for a job
Instrument
Unit: {pod}
Note: This metric aligns with the `failed` field of the
[K8s JobStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#jobstatus-v1-batch).
"""


def create_k8s_job_pod_failed(meter):
    """The number of pods which reached phase Failed for a job"""
    return meter.create_up_down_counter(
        name=K8S_JOB_POD_FAILED,
        description="The number of pods which reached phase Failed for a job.",
        unit="{pod}",
    )


K8S_JOB_POD_MAX_PARALLEL = "k8s.job.pod.max_parallel"
"""
The max desired number of pods the job should run at any given time
Instrument
Unit: {pod}
Note: This metric aligns with the `parallelism` field of the
[K8s JobSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#jobspec-v1-batch).
"""


def create_k8s_job_pod_max_parallel(meter):
    """The max desired number of pods the job should run at any given time"""
    return meter.create_up_down_counter(
        name=K8S_JOB_POD_MAX_PARALLEL,
        description="The max desired number of pods the job should run at any given time.",
        unit="{pod}",
    )


K8S_JOB_POD_SUCCESSFUL = "k8s.job.pod.successful"
"""
The number of pods which reached phase Succeeded for a job
Instrument
Unit: {pod}
Note: This metric aligns with the `succeeded` field of the
[K8s JobStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#jobstatus-v1-batch).
"""


def create_k8s_job_pod_successful(meter):
    """The number of pods which reached phase Succeeded for a job"""
    return meter.create_up_down_counter(
        name=K8S_JOB_POD_SUCCESSFUL,
        description="The number of pods which reached phase Succeeded for a job.",
        unit="{pod}",
    )


K8S_JOB_SUCCESSFUL_PODS = "k8s.job.successful_pods"
"""
Deprecated: Replaced by `k8s.job.pod.successful`.
"""


def create_k8s_job_successful_pods(meter):
    """Deprecated, use `k8s.job.pod.successful` instead"""
    return meter.create_up_down_counter(
        name=K8S_JOB_SUCCESSFUL_PODS,
        description="Deprecated, use `k8s.job.pod.successful` instead.",
        unit="{pod}",
    )


K8S_NAMESPACE_PHASE = "k8s.namespace.phase"
"""
Describes number of K8s namespaces that are currently in a given phase
Instrument
Unit: {namespace}
"""


def create_k8s_namespace_phase(meter):
    """Describes number of K8s namespaces that are currently in a given phase"""
    return meter.create_up_down_counter(
        name=K8S_NAMESPACE_PHASE,
        description="Describes number of K8s namespaces that are currently in a given phase.",
        unit="{namespace}",
    )


K8S_NODE_ALLOCATABLE_CPU = "k8s.node.allocatable.cpu"
"""
Deprecated: Replaced by `k8s.node.cpu.allocatable`.
"""


def create_k8s_node_allocatable_cpu(meter):
    """Deprecated, use `k8s.node.cpu.allocatable` instead"""
    return meter.create_up_down_counter(
        name=K8S_NODE_ALLOCATABLE_CPU,
        description="Deprecated, use `k8s.node.cpu.allocatable` instead.",
        unit="{cpu}",
    )


K8S_NODE_ALLOCATABLE_EPHEMERAL_STORAGE = (
    "k8s.node.allocatable.ephemeral_storage"
)
"""
Deprecated: Replaced by `k8s.node.ephemeral_storage.allocatable`.
"""


def create_k8s_node_allocatable_ephemeral_storage(
    meter
):
    """Deprecated, use `k8s.node.ephemeral_storage.allocatable` instead"""
    return meter.create_up_down_counter(
        name=K8S_NODE_ALLOCATABLE_EPHEMERAL_STORAGE,
        description="Deprecated, use `k8s.node.ephemeral_storage.allocatable` instead.",
        unit="By",
    )


K8S_NODE_ALLOCATABLE_MEMORY = "k8s.node.allocatable.memory"
"""
Deprecated: Replaced by `k8s.node.memory.allocatable`.
"""


def create_k8s_node_allocatable_memory(meter):
    """Deprecated, use `k8s.node.memory.allocatable` instead"""
    return meter.create_up_down_counter(
        name=K8S_NODE_ALLOCATABLE_MEMORY,
        description="Deprecated, use `k8s.node.memory.allocatable` instead.",
        unit="By",
    )


K8S_NODE_ALLOCATABLE_PODS = "k8s.node.allocatable.pods"
"""
Deprecated: Replaced by `k8s.node.pod.allocatable`.
"""


def create_k8s_node_allocatable_pods(meter):
    """Deprecated, use `k8s.node.pod.allocatable` instead"""
    return meter.create_up_down_counter(
        name=K8S_NODE_ALLOCATABLE_PODS,
        description="Deprecated, use `k8s.node.pod.allocatable` instead.",
        unit="{pod}",
    )


K8S_NODE_CONDITION_STATUS = "k8s.node.condition.status"
"""
Describes the condition of a particular Node
Instrument
Unit: {node}
Note: All possible node condition pairs (type and status) will be reported at each time interval to avoid missing metrics. Condition pairs corresponding to the current conditions' statuses will be non-zero.
"""


def create_k8s_node_condition_status(meter):
    """Describes the condition of a particular Node"""
    return meter.create_up_down_counter(
        name=K8S_NODE_CONDITION_STATUS,
        description="Describes the condition of a particular Node.",
        unit="{node}",
    )


K8S_NODE_CPU_ALLOCATABLE = "k8s.node.cpu.allocatable"
"""
Amount of cpu allocatable on the node
Instrument
Unit: {cpu}
"""


def create_k8s_node_cpu_allocatable(meter):
    """Amount of cpu allocatable on the node"""
    return meter.create_up_down_counter(
        name=K8S_NODE_CPU_ALLOCATABLE,
        description="Amount of cpu allocatable on the node.",
        unit="{cpu}",
    )


K8S_NODE_CPU_TIME = "k8s.node.cpu.time"
"""
Total CPU time consumed
Instrument
Unit
Note: Total CPU time consumed by the specific Node on all available CPU cores.
"""


def create_k8s_node_cpu_time(meter):
    """Total CPU time consumed"""
    return meter.create_counter(
        name=K8S_NODE_CPU_TIME,
        description="Total CPU time consumed.",
        unit="s",
    )


K8S_NODE_CPU_USAGE = "k8s.node.cpu.usage"
"""
Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs
Instrument
Unit: {cpu}
Note: CPU usage of the specific Node on all available CPU cores, averaged over the sample window.
"""


def create_k8s_node_cpu_usage(
    meter, callbacks
):
    """Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"""
    return meter.create_observable_gauge(
        name=K8S_NODE_CPU_USAGE,
        callbacks=callbacks,
        description="Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs.",
        unit="{cpu}",
    )


K8S_NODE_EPHEMERAL_STORAGE_ALLOCATABLE = (
    "k8s.node.ephemeral_storage.allocatable"
)
"""
Amount of ephemeral-storage allocatable on the node
Instrument
Unit
"""


def create_k8s_node_ephemeral_storage_allocatable(
    meter
):
    """Amount of ephemeral-storage allocatable on the node"""
    return meter.create_up_down_counter(
        name=K8S_NODE_EPHEMERAL_STORAGE_ALLOCATABLE,
        description="Amount of ephemeral-storage allocatable on the node.",
        unit="By",
    )


K8S_NODE_FILESYSTEM_AVAILABLE = "k8s.node.filesystem.available"
"""
Node filesystem available bytes
Instrument
Unit
Note: This metric is derived from the
[FsStats.AvailableBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [NodeStats.Fs](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#NodeStats)
of the Kubelet's stats API.
"""


def create_k8s_node_filesystem_available(meter):
    """Node filesystem available bytes"""
    return meter.create_up_down_counter(
        name=K8S_NODE_FILESYSTEM_AVAILABLE,
        description="Node filesystem available bytes.",
        unit="By",
    )


K8S_NODE_FILESYSTEM_CAPACITY = "k8s.node.filesystem.capacity"
"""
Node filesystem capacity
Instrument
Unit
Note: This metric is derived from the
[FsStats.CapacityBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [NodeStats.Fs](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#NodeStats)
of the Kubelet's stats API.
"""


def create_k8s_node_filesystem_capacity(meter):
    """Node filesystem capacity"""
    return meter.create_up_down_counter(
        name=K8S_NODE_FILESYSTEM_CAPACITY,
        description="Node filesystem capacity.",
        unit="By",
    )


K8S_NODE_FILESYSTEM_USAGE = "k8s.node.filesystem.usage"
"""
Node filesystem usage
Instrument
Unit
Note: This may not equal capacity - available.

This metric is derived from the
[FsStats.UsedBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [NodeStats.Fs](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#NodeStats)
of the Kubelet's stats API.
"""


def create_k8s_node_filesystem_usage(meter):
    """Node filesystem usage"""
    return meter.create_up_down_counter(
        name=K8S_NODE_FILESYSTEM_USAGE,
        description="Node filesystem usage.",
        unit="By",
    )


K8S_NODE_MEMORY_ALLOCATABLE = "k8s.node.memory.allocatable"
"""
Amount of memory allocatable on the node
Instrument
Unit
"""


def create_k8s_node_memory_allocatable(meter):
    """Amount of memory allocatable on the node"""
    return meter.create_up_down_counter(
        name=K8S_NODE_MEMORY_ALLOCATABLE,
        description="Amount of memory allocatable on the node.",
        unit="By",
    )


K8S_NODE_MEMORY_AVAILABLE = "k8s.node.memory.available"
"""
Node memory available
Instrument
Unit
Note: Available memory for use.  This is defined as the memory limit - workingSetBytes. If memory limit is undefined, the available bytes is omitted.
This metric is derived from the [MemoryStats.AvailableBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [NodeStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#NodeStats) of the Kubelet's stats API.
"""


def create_k8s_node_memory_available(meter):
    """Node memory available"""
    return meter.create_up_down_counter(
        name=K8S_NODE_MEMORY_AVAILABLE,
        description="Node memory available.",
        unit="By",
    )


K8S_NODE_MEMORY_PAGING_FAULTS = "k8s.node.memory.paging.faults"
"""
Node memory paging faults
Instrument
Unit: {fault}
Note: Cumulative number of major/minor page faults.
This metric is derived from the [MemoryStats.PageFaults](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) and [MemoryStats.MajorPageFaults](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) fields of the [NodeStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#NodeStats) of the Kubelet's stats API.
"""


def create_k8s_node_memory_paging_faults(meter):
    """Node memory paging faults"""
    return meter.create_counter(
        name=K8S_NODE_MEMORY_PAGING_FAULTS,
        description="Node memory paging faults.",
        unit="{fault}",
    )


K8S_NODE_MEMORY_RSS = "k8s.node.memory.rss"
"""
Node memory RSS
Instrument
Unit
Note: The amount of anonymous and swap cache memory (includes transparent hugepages).
This metric is derived from the [MemoryStats.RSSBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [NodeStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#NodeStats) of the Kubelet's stats API.
"""


def create_k8s_node_memory_rss(meter):
    """Node memory RSS"""
    return meter.create_up_down_counter(
        name=K8S_NODE_MEMORY_RSS,
        description="Node memory RSS.",
        unit="By",
    )


K8S_NODE_MEMORY_USAGE = "k8s.node.memory.usage"
"""
Memory usage of the Node
Instrument
Unit
Note: Total memory usage of the Node.
"""


def create_k8s_node_memory_usage(
    meter, callbacks
):
    """Memory usage of the Node"""
    return meter.create_observable_gauge(
        name=K8S_NODE_MEMORY_USAGE,
        callbacks=callbacks,
        description="Memory usage of the Node.",
        unit="By",
    )


K8S_NODE_MEMORY_WORKING_SET = "k8s.node.memory.working_set"
"""
Node memory working set
Instrument
Unit
Note: The amount of working set memory. This includes recently accessed memory, dirty memory, and kernel memory. WorkingSetBytes is <= UsageBytes.
This metric is derived from the [MemoryStats.WorkingSetBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [NodeStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#NodeStats) of the Kubelet's stats API.
"""


def create_k8s_node_memory_working_set(meter):
    """Node memory working set"""
    return meter.create_up_down_counter(
        name=K8S_NODE_MEMORY_WORKING_SET,
        description="Node memory working set.",
        unit="By",
    )


K8S_NODE_NETWORK_ERRORS = "k8s.node.network.errors"
"""
Node network errors
Instrument
Unit: {error}
"""


def create_k8s_node_network_errors(meter):
    """Node network errors"""
    return meter.create_counter(
        name=K8S_NODE_NETWORK_ERRORS,
        description="Node network errors.",
        unit="{error}",
    )


K8S_NODE_NETWORK_IO = "k8s.node.network.io"
"""
Network bytes for the Node
Instrument
Unit
"""


def create_k8s_node_network_io(meter):
    """Network bytes for the Node"""
    return meter.create_counter(
        name=K8S_NODE_NETWORK_IO,
        description="Network bytes for the Node.",
        unit="By",
    )


K8S_NODE_POD_ALLOCATABLE = "k8s.node.pod.allocatable"
"""
Amount of pods allocatable on the node
Instrument
Unit: {pod}
"""


def create_k8s_node_pod_allocatable(meter):
    """Amount of pods allocatable on the node"""
    return meter.create_up_down_counter(
        name=K8S_NODE_POD_ALLOCATABLE,
        description="Amount of pods allocatable on the node.",
        unit="{pod}",
    )


K8S_NODE_UPTIME = "k8s.node.uptime"
"""
The time the Node has been running
Instrument
Unit
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_k8s_node_uptime(
    meter, callbacks
):
    """The time the Node has been running"""
    return meter.create_observable_gauge(
        name=K8S_NODE_UPTIME,
        callbacks=callbacks,
        description="The time the Node has been running.",
        unit="s",
    )


K8S_POD_CPU_TIME = "k8s.pod.cpu.time"
"""
Total CPU time consumed
Instrument
Unit
Note: Total CPU time consumed by the specific Pod on all available CPU cores.
"""


def create_k8s_pod_cpu_time(meter):
    """Total CPU time consumed"""
    return meter.create_counter(
        name=K8S_POD_CPU_TIME,
        description="Total CPU time consumed.",
        unit="s",
    )


K8S_POD_CPU_USAGE = "k8s.pod.cpu.usage"
"""
Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs
Instrument
Unit: {cpu}
Note: CPU usage of the specific Pod on all available CPU cores, averaged over the sample window.
"""


def create_k8s_pod_cpu_usage(
    meter, callbacks
):
    """Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"""
    return meter.create_observable_gauge(
        name=K8S_POD_CPU_USAGE,
        callbacks=callbacks,
        description="Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs.",
        unit="{cpu}",
    )


K8S_POD_FILESYSTEM_AVAILABLE = "k8s.pod.filesystem.available"
"""
Pod filesystem available bytes
Instrument
Unit
Note: This metric is derived from the
[FsStats.AvailableBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [PodStats.EphemeralStorage](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats)
of the Kubelet's stats API.
"""


def create_k8s_pod_filesystem_available(meter):
    """Pod filesystem available bytes"""
    return meter.create_up_down_counter(
        name=K8S_POD_FILESYSTEM_AVAILABLE,
        description="Pod filesystem available bytes.",
        unit="By",
    )


K8S_POD_FILESYSTEM_CAPACITY = "k8s.pod.filesystem.capacity"
"""
Pod filesystem capacity
Instrument
Unit
Note: This metric is derived from the
[FsStats.CapacityBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [PodStats.EphemeralStorage](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats)
of the Kubelet's stats API.
"""


def create_k8s_pod_filesystem_capacity(meter):
    """Pod filesystem capacity"""
    return meter.create_up_down_counter(
        name=K8S_POD_FILESYSTEM_CAPACITY,
        description="Pod filesystem capacity.",
        unit="By",
    )


K8S_POD_FILESYSTEM_USAGE = "k8s.pod.filesystem.usage"
"""
Pod filesystem usage
Instrument
Unit
Note: This may not equal capacity - available.

This metric is derived from the
[FsStats.UsedBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#FsStats) field
of the [PodStats.EphemeralStorage](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats)
of the Kubelet's stats API.
"""


def create_k8s_pod_filesystem_usage(meter):
    """Pod filesystem usage"""
    return meter.create_up_down_counter(
        name=K8S_POD_FILESYSTEM_USAGE,
        description="Pod filesystem usage.",
        unit="By",
    )


K8S_POD_MEMORY_AVAILABLE = "k8s.pod.memory.available"
"""
Pod memory available
Instrument
Unit
Note: Available memory for use.  This is defined as the memory limit - workingSetBytes. If memory limit is undefined, the available bytes is omitted.
This metric is derived from the [MemoryStats.AvailableBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [PodStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#PodStats) of the Kubelet's stats API.
"""


def create_k8s_pod_memory_available(meter):
    """Pod memory available"""
    return meter.create_up_down_counter(
        name=K8S_POD_MEMORY_AVAILABLE,
        description="Pod memory available.",
        unit="By",
    )


K8S_POD_MEMORY_PAGING_FAULTS = "k8s.pod.memory.paging.faults"
"""
Pod memory paging faults
Instrument
Unit: {fault}
Note: Cumulative number of major/minor page faults.
This metric is derived from the [MemoryStats.PageFaults](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) and [MemoryStats.MajorPageFaults](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [PodStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#PodStats) of the Kubelet's stats API.
"""


def create_k8s_pod_memory_paging_faults(meter):
    """Pod memory paging faults"""
    return meter.create_counter(
        name=K8S_POD_MEMORY_PAGING_FAULTS,
        description="Pod memory paging faults.",
        unit="{fault}",
    )


K8S_POD_MEMORY_RSS = "k8s.pod.memory.rss"
"""
Pod memory RSS
Instrument
Unit
Note: The amount of anonymous and swap cache memory (includes transparent hugepages).
This metric is derived from the [MemoryStats.RSSBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [PodStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#PodStats) of the Kubelet's stats API.
"""


def create_k8s_pod_memory_rss(meter):
    """Pod memory RSS"""
    return meter.create_up_down_counter(
        name=K8S_POD_MEMORY_RSS,
        description="Pod memory RSS.",
        unit="By",
    )


K8S_POD_MEMORY_USAGE = "k8s.pod.memory.usage"
"""
Memory usage of the Pod
Instrument
Unit
Note: Total memory usage of the Pod.
"""


def create_k8s_pod_memory_usage(
    meter, callbacks
):
    """Memory usage of the Pod"""
    return meter.create_observable_gauge(
        name=K8S_POD_MEMORY_USAGE,
        callbacks=callbacks,
        description="Memory usage of the Pod.",
        unit="By",
    )


K8S_POD_MEMORY_WORKING_SET = "k8s.pod.memory.working_set"
"""
Pod memory working set
Instrument
Unit
Note: The amount of working set memory. This includes recently accessed memory, dirty memory, and kernel memory. WorkingSetBytes is <= UsageBytes.
This metric is derived from the [MemoryStats.WorkingSetBytes](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#MemoryStats) field of the [PodStats.Memory](https://pkg.go.dev/k8s.io/kubelet@v0.34.0/pkg/apis/stats/v1alpha1#PodStats) of the Kubelet's stats API.
"""


def create_k8s_pod_memory_working_set(meter):
    """Pod memory working set"""
    return meter.create_up_down_counter(
        name=K8S_POD_MEMORY_WORKING_SET,
        description="Pod memory working set.",
        unit="By",
    )


K8S_POD_NETWORK_ERRORS = "k8s.pod.network.errors"
"""
Pod network errors
Instrument
Unit: {error}
"""


def create_k8s_pod_network_errors(meter):
    """Pod network errors"""
    return meter.create_counter(
        name=K8S_POD_NETWORK_ERRORS,
        description="Pod network errors.",
        unit="{error}",
    )


K8S_POD_NETWORK_IO = "k8s.pod.network.io"
"""
Network bytes for the Pod
Instrument
Unit
"""


def create_k8s_pod_network_io(meter):
    """Network bytes for the Pod"""
    return meter.create_counter(
        name=K8S_POD_NETWORK_IO,
        description="Network bytes for the Pod.",
        unit="By",
    )


K8S_POD_STATUS_PHASE = "k8s.pod.status.phase"
"""
Describes number of K8s Pods that are currently in a given phase
Instrument
Unit: {pod}
Note: All possible pod phases will be reported at each time interval to avoid missing metrics.
Only the value corresponding to the current phase will be non-zero.
"""


def create_k8s_pod_status_phase(meter):
    """Describes number of K8s Pods that are currently in a given phase"""
    return meter.create_up_down_counter(
        name=K8S_POD_STATUS_PHASE,
        description="Describes number of K8s Pods that are currently in a given phase.",
        unit="{pod}",
    )


K8S_POD_STATUS_REASON = "k8s.pod.status.reason"
"""
Describes the number of K8s Pods that are currently in a state for a given reason
Instrument
Unit: {pod}
Note: All possible pod status reasons will be reported at each time interval to avoid missing metrics.
Only the value corresponding to the current reason will be non-zero.
"""


def create_k8s_pod_status_reason(meter):
    """Describes the number of K8s Pods that are currently in a state for a given reason"""
    return meter.create_up_down_counter(
        name=K8S_POD_STATUS_REASON,
        description="Describes the number of K8s Pods that are currently in a state for a given reason.",
        unit="{pod}",
    )


K8S_POD_UPTIME = "k8s.pod.uptime"
"""
The time the Pod has been running
Instrument
Unit
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_k8s_pod_uptime(
    meter, callbacks
):
    """The time the Pod has been running"""
    return meter.create_observable_gauge(
        name=K8S_POD_UPTIME,
        callbacks=callbacks,
        description="The time the Pod has been running.",
        unit="s",
    )


K8S_POD_VOLUME_AVAILABLE = "k8s.pod.volume.available"
"""
Pod volume storage space available
Instrument
Unit
Note: This metric is derived from the
[VolumeStats.AvailableBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.
"""


def create_k8s_pod_volume_available(meter):
    """Pod volume storage space available"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_AVAILABLE,
        description="Pod volume storage space available.",
        unit="By",
    )


K8S_POD_VOLUME_CAPACITY = "k8s.pod.volume.capacity"
"""
Pod volume total capacity
Instrument
Unit
Note: This metric is derived from the
[VolumeStats.CapacityBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.
"""


def create_k8s_pod_volume_capacity(meter):
    """Pod volume total capacity"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_CAPACITY,
        description="Pod volume total capacity.",
        unit="By",
    )


K8S_POD_VOLUME_INODE_COUNT = "k8s.pod.volume.inode.count"
"""
The total inodes in the filesystem of the Pod's volume
Instrument
Unit: {inode}
Note: This metric is derived from the
[VolumeStats.Inodes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.
"""


def create_k8s_pod_volume_inode_count(meter):
    """The total inodes in the filesystem of the Pod's volume"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_INODE_COUNT,
        description="The total inodes in the filesystem of the Pod's volume.",
        unit="{inode}",
    )


K8S_POD_VOLUME_INODE_FREE = "k8s.pod.volume.inode.free"
"""
The free inodes in the filesystem of the Pod's volume
Instrument
Unit: {inode}
Note: This metric is derived from the
[VolumeStats.InodesFree](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.
"""


def create_k8s_pod_volume_inode_free(meter):
    """The free inodes in the filesystem of the Pod's volume"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_INODE_FREE,
        description="The free inodes in the filesystem of the Pod's volume.",
        unit="{inode}",
    )


K8S_POD_VOLUME_INODE_USED = "k8s.pod.volume.inode.used"
"""
The inodes used by the filesystem of the Pod's volume
Instrument
Unit: {inode}
Note: This metric is derived from the
[VolumeStats.InodesUsed](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.

This may not be equal to `inodes - free` because filesystem may share inodes with other filesystems.
"""


def create_k8s_pod_volume_inode_used(meter):
    """The inodes used by the filesystem of the Pod's volume"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_INODE_USED,
        description="The inodes used by the filesystem of the Pod's volume.",
        unit="{inode}",
    )


K8S_POD_VOLUME_USAGE = "k8s.pod.volume.usage"
"""
Pod volume usage
Instrument
Unit
Note: This may not equal capacity - available.

This metric is derived from the
[VolumeStats.UsedBytes](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#VolumeStats) field
of the [PodStats](https://pkg.go.dev/k8s.io/kubelet@v0.33.0/pkg/apis/stats/v1alpha1#PodStats) of the
Kubelet's stats API.
"""


def create_k8s_pod_volume_usage(meter):
    """Pod volume usage"""
    return meter.create_up_down_counter(
        name=K8S_POD_VOLUME_USAGE,
        description="Pod volume usage.",
        unit="By",
    )


K8S_REPLICASET_AVAILABLE_PODS = "k8s.replicaset.available_pods"
"""
Deprecated: Replaced by `k8s.replicaset.pod.available`.
"""


def create_k8s_replicaset_available_pods(meter):
    """Deprecated, use `k8s.replicaset.pod.available` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICASET_AVAILABLE_PODS,
        description="Deprecated, use `k8s.replicaset.pod.available` instead.",
        unit="{pod}",
    )


K8S_REPLICASET_DESIRED_PODS = "k8s.replicaset.desired_pods"
"""
Deprecated: Replaced by `k8s.replicaset.pod.desired`.
"""


def create_k8s_replicaset_desired_pods(meter):
    """Deprecated, use `k8s.replicaset.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICASET_DESIRED_PODS,
        description="Deprecated, use `k8s.replicaset.pod.desired` instead.",
        unit="{pod}",
    )


K8S_REPLICASET_POD_AVAILABLE = "k8s.replicaset.pod.available"
"""
Total number of available replica pods (ready for at least minReadySeconds) targeted by this replicaset
Instrument
Unit: {pod}
Note: This metric aligns with the `availableReplicas` field of the
[K8s ReplicaSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#replicasetstatus-v1-apps).
"""


def create_k8s_replicaset_pod_available(meter):
    """Total number of available replica pods (ready for at least minReadySeconds) targeted by this replicaset"""
    return meter.create_up_down_counter(
        name=K8S_REPLICASET_POD_AVAILABLE,
        description="Total number of available replica pods (ready for at least minReadySeconds) targeted by this replicaset.",
        unit="{pod}",
    )


K8S_REPLICASET_POD_DESIRED = "k8s.replicaset.pod.desired"
"""
Number of desired replica pods in this replicaset
Instrument
Unit: {pod}
Note: This metric aligns with the `replicas` field of the
[K8s ReplicaSetSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#replicasetspec-v1-apps).
"""


def create_k8s_replicaset_pod_desired(meter):
    """Number of desired replica pods in this replicaset"""
    return meter.create_up_down_counter(
        name=K8S_REPLICASET_POD_DESIRED,
        description="Number of desired replica pods in this replicaset.",
        unit="{pod}",
    )


K8S_REPLICATION_CONTROLLER_AVAILABLE_PODS = (
    "k8s.replication_controller.available_pods"
)
"""
Deprecated: Replaced by `k8s.replicationcontroller.pod.available`.
"""


def create_k8s_replication_controller_available_pods(
    meter
):
    """Deprecated, use `k8s.replicationcontroller.pod.available` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATION_CONTROLLER_AVAILABLE_PODS,
        description="Deprecated, use `k8s.replicationcontroller.pod.available` instead.",
        unit="{pod}",
    )


K8S_REPLICATION_CONTROLLER_DESIRED_PODS = (
    "k8s.replication_controller.desired_pods"
)
"""
Deprecated: Replaced by `k8s.replicationcontroller.pod.desired`.
"""


def create_k8s_replication_controller_desired_pods(
    meter
):
    """Deprecated, use `k8s.replicationcontroller.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATION_CONTROLLER_DESIRED_PODS,
        description="Deprecated, use `k8s.replicationcontroller.pod.desired` instead.",
        unit="{pod}",
    )


K8S_REPLICATIONCONTROLLER_AVAILABLE_PODS = (
    "k8s.replicationcontroller.available_pods"
)
"""
Deprecated: Replaced by `k8s.replicationcontroller.pod.available`.
"""


def create_k8s_replicationcontroller_available_pods(
    meter
):
    """Deprecated, use `k8s.replicationcontroller.pod.available` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATIONCONTROLLER_AVAILABLE_PODS,
        description="Deprecated, use `k8s.replicationcontroller.pod.available` instead.",
        unit="{pod}",
    )


K8S_REPLICATIONCONTROLLER_DESIRED_PODS = (
    "k8s.replicationcontroller.desired_pods"
)
"""
Deprecated: Replaced by `k8s.replicationcontroller.pod.desired`.
"""


def create_k8s_replicationcontroller_desired_pods(
    meter
):
    """Deprecated, use `k8s.replicationcontroller.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATIONCONTROLLER_DESIRED_PODS,
        description="Deprecated, use `k8s.replicationcontroller.pod.desired` instead.",
        unit="{pod}",
    )


K8S_REPLICATIONCONTROLLER_POD_AVAILABLE = (
    "k8s.replicationcontroller.pod.available"
)
"""
Total number of available replica pods (ready for at least minReadySeconds) targeted by this replication controller
Instrument
Unit: {pod}
Note: This metric aligns with the `availableReplicas` field of the
[K8s ReplicationControllerStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#replicationcontrollerstatus-v1-core).
"""


def create_k8s_replicationcontroller_pod_available(
    meter
):
    """Total number of available replica pods (ready for at least minReadySeconds) targeted by this replication controller"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATIONCONTROLLER_POD_AVAILABLE,
        description="Total number of available replica pods (ready for at least minReadySeconds) targeted by this replication controller.",
        unit="{pod}",
    )


K8S_REPLICATIONCONTROLLER_POD_DESIRED = (
    "k8s.replicationcontroller.pod.desired"
)
"""
Number of desired replica pods in this replication controller
Instrument
Unit: {pod}
Note: This metric aligns with the `replicas` field of the
[K8s ReplicationControllerSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#replicationcontrollerspec-v1-core).
"""


def create_k8s_replicationcontroller_pod_desired(
    meter
):
    """Number of desired replica pods in this replication controller"""
    return meter.create_up_down_counter(
        name=K8S_REPLICATIONCONTROLLER_POD_DESIRED,
        description="Number of desired replica pods in this replication controller.",
        unit="{pod}",
    )


K8S_RESOURCEQUOTA_CPU_LIMIT_HARD = "k8s.resourcequota.cpu.limit.hard"
"""
The CPU limits in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_cpu_limit_hard(meter):
    """The CPU limits in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_CPU_LIMIT_HARD,
        description="The CPU limits in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="{cpu}",
    )


K8S_RESOURCEQUOTA_CPU_LIMIT_USED = "k8s.resourcequota.cpu.limit.used"
"""
The CPU limits in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_cpu_limit_used(meter):
    """The CPU limits in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_CPU_LIMIT_USED,
        description="The CPU limits in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="{cpu}",
    )


K8S_RESOURCEQUOTA_CPU_REQUEST_HARD = (
    "k8s.resourcequota.cpu.request.hard"
)
"""
The CPU requests in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_cpu_request_hard(meter):
    """The CPU requests in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_CPU_REQUEST_HARD,
        description="The CPU requests in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="{cpu}",
    )


K8S_RESOURCEQUOTA_CPU_REQUEST_USED = (
    "k8s.resourcequota.cpu.request.used"
)
"""
The CPU requests in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit: {cpu}
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_cpu_request_used(meter):
    """The CPU requests in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_CPU_REQUEST_USED,
        description="The CPU requests in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="{cpu}",
    )


K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_LIMIT_HARD = (
    "k8s.resourcequota.ephemeral_storage.limit.hard"
)
"""
The sum of local ephemeral storage limits in the namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_ephemeral_storage_limit_hard(
    meter
):
    """The sum of local ephemeral storage limits in the namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_LIMIT_HARD,
        description="The sum of local ephemeral storage limits in the namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_LIMIT_USED = (
    "k8s.resourcequota.ephemeral_storage.limit.used"
)
"""
The sum of local ephemeral storage limits in the namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_ephemeral_storage_limit_used(
    meter
):
    """The sum of local ephemeral storage limits in the namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_LIMIT_USED,
        description="The sum of local ephemeral storage limits in the namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_REQUEST_HARD = (
    "k8s.resourcequota.ephemeral_storage.request.hard"
)
"""
The sum of local ephemeral storage requests in the namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_ephemeral_storage_request_hard(
    meter
):
    """The sum of local ephemeral storage requests in the namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_REQUEST_HARD,
        description="The sum of local ephemeral storage requests in the namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_REQUEST_USED = (
    "k8s.resourcequota.ephemeral_storage.request.used"
)
"""
The sum of local ephemeral storage requests in the namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_ephemeral_storage_request_used(
    meter
):
    """The sum of local ephemeral storage requests in the namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_EPHEMERAL_STORAGE_REQUEST_USED,
        description="The sum of local ephemeral storage requests in the namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_HUGEPAGE_COUNT_REQUEST_HARD = (
    "k8s.resourcequota.hugepage_count.request.hard"
)
"""
The huge page requests in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit: {hugepage}
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_hugepage_count_request_hard(
    meter
):
    """The huge page requests in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_HUGEPAGE_COUNT_REQUEST_HARD,
        description="The huge page requests in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="{hugepage}",
    )


K8S_RESOURCEQUOTA_HUGEPAGE_COUNT_REQUEST_USED = (
    "k8s.resourcequota.hugepage_count.request.used"
)
"""
The huge page requests in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit: {hugepage}
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_hugepage_count_request_used(
    meter
):
    """The huge page requests in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_HUGEPAGE_COUNT_REQUEST_USED,
        description="The huge page requests in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="{hugepage}",
    )


K8S_RESOURCEQUOTA_MEMORY_LIMIT_HARD = (
    "k8s.resourcequota.memory.limit.hard"
)
"""
The memory limits in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_memory_limit_hard(meter):
    """The memory limits in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_MEMORY_LIMIT_HARD,
        description="The memory limits in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_MEMORY_LIMIT_USED = (
    "k8s.resourcequota.memory.limit.used"
)
"""
The memory limits in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_memory_limit_used(meter):
    """The memory limits in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_MEMORY_LIMIT_USED,
        description="The memory limits in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_MEMORY_REQUEST_HARD = (
    "k8s.resourcequota.memory.request.hard"
)
"""
The memory requests in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_memory_request_hard(
    meter
):
    """The memory requests in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_MEMORY_REQUEST_HARD,
        description="The memory requests in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_MEMORY_REQUEST_USED = (
    "k8s.resourcequota.memory.request.used"
)
"""
The memory requests in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_memory_request_used(
    meter
):
    """The memory requests in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_MEMORY_REQUEST_USED,
        description="The memory requests in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_OBJECT_COUNT_HARD = (
    "k8s.resourcequota.object_count.hard"
)
"""
The object count limits in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit: {object}
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_object_count_hard(meter):
    """The object count limits in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_OBJECT_COUNT_HARD,
        description="The object count limits in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="{object}",
    )


K8S_RESOURCEQUOTA_OBJECT_COUNT_USED = (
    "k8s.resourcequota.object_count.used"
)
"""
The object count limits in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit: {object}
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).
"""


def create_k8s_resourcequota_object_count_used(meter):
    """The object count limits in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_OBJECT_COUNT_USED,
        description="The object count limits in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="{object}",
    )


K8S_RESOURCEQUOTA_PERSISTENTVOLUMECLAIM_COUNT_HARD = (
    "k8s.resourcequota.persistentvolumeclaim_count.hard"
)
"""
The total number of PersistentVolumeClaims that can exist in the namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit: {persistentvolumeclaim}
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_k8s_resourcequota_persistentvolumeclaim_count_hard(
    meter
):
    """The total number of PersistentVolumeClaims that can exist in the namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_PERSISTENTVOLUMECLAIM_COUNT_HARD,
        description="The total number of PersistentVolumeClaims that can exist in the namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="{persistentvolumeclaim}",
    )


K8S_RESOURCEQUOTA_PERSISTENTVOLUMECLAIM_COUNT_USED = (
    "k8s.resourcequota.persistentvolumeclaim_count.used"
)
"""
The total number of PersistentVolumeClaims that can exist in the namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit: {persistentvolumeclaim}
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_k8s_resourcequota_persistentvolumeclaim_count_used(
    meter
):
    """The total number of PersistentVolumeClaims that can exist in the namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_PERSISTENTVOLUMECLAIM_COUNT_USED,
        description="The total number of PersistentVolumeClaims that can exist in the namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="{persistentvolumeclaim}",
    )


K8S_RESOURCEQUOTA_STORAGE_REQUEST_HARD = (
    "k8s.resourcequota.storage.request.hard"
)
"""
The storage requests in a specific namespace.
The value represents the configured quota limit of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `hard` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_k8s_resourcequota_storage_request_hard(
    meter
):
    """The storage requests in a specific namespace.
    The value represents the configured quota limit of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_STORAGE_REQUEST_HARD,
        description="The storage requests in a specific namespace. The value represents the configured quota limit of the resource in the namespace.",
        unit="By",
    )


K8S_RESOURCEQUOTA_STORAGE_REQUEST_USED = (
    "k8s.resourcequota.storage.request.used"
)
"""
The storage requests in a specific namespace.
The value represents the current observed total usage of the resource in the namespace
Instrument
Unit
Note: This metric is retrieved from the `used` field of the
[K8s ResourceQuotaStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcequotastatus-v1-core).

The `k8s.storageclass.name` should be required when a resource quota is defined for a specific
storage class.
"""


def create_k8s_resourcequota_storage_request_used(
    meter
):
    """The storage requests in a specific namespace.
    The value represents the current observed total usage of the resource in the namespace"""
    return meter.create_up_down_counter(
        name=K8S_RESOURCEQUOTA_STORAGE_REQUEST_USED,
        description="The storage requests in a specific namespace. The value represents the current observed total usage of the resource in the namespace.",
        unit="By",
    )


K8S_SERVICE_ENDPOINT_COUNT = "k8s.service.endpoint.count"
"""
Number of endpoints for a service by condition and address type
Instrument
Unit: {endpoint}
Note: This metric is derived from the Kubernetes [EndpointSlice API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/).
It reports the number of network endpoints backing a Service, broken down by their condition and address type.

In dual-stack or multi-protocol clusters, separate counts are reported for each address family (`IPv4`, `IPv6`, `FQDN`).

When the optional `zone` attribute is enabled, counts are further broken down by availability zone for zone-aware monitoring.

An endpoint may be reported under multiple conditions simultaneously (e.g., both `serving` and `terminating` during a graceful shutdown).
See [K8s EndpointConditions](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) for more details.

The conditions represent:
- `ready`: Endpoints capable of receiving new connections.
- `serving`: Endpoints currently handling traffic.
- `terminating`: Endpoints that are being phased out but may still be handling existing connections.

For Services with `publishNotReadyAddresses` enabled (common for headless StatefulSets),
this metric will include endpoints that are published despite not being ready.
The `k8s.service.publish_not_ready_addresses` resource attribute indicates this setting.
"""


def create_k8s_service_endpoint_count(
    meter, callbacks
):
    """Number of endpoints for a service by condition and address type"""
    return meter.create_observable_gauge(
        name=K8S_SERVICE_ENDPOINT_COUNT,
        callbacks=callbacks,
        description="Number of endpoints for a service by condition and address type.",
        unit="{endpoint}",
    )


K8S_SERVICE_LOAD_BALANCER_INGRESS_COUNT = (
    "k8s.service.load_balancer.ingress.count"
)
"""
Number of load balancer ingress points (external IPs/hostnames) assigned to the service
Instrument
Unit: {ingress}
Note: This metric reports the number of external ingress points (IP addresses or hostnames)
assigned to a LoadBalancer Service.

It is only emitted for Services of type `LoadBalancer` and reflects the assignments
made by the underlying infrastructure's load balancer controller in the
[.status.loadBalancer.ingress](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceStatus) field.

A value of `0` indicates that no ingress points have been assigned yet (e.g., during provisioning).
A value greater than `1` may occur when multiple IPs or hostnames are assigned (e.g., dual-stack configurations).

This metric signals that external endpoints have been assigned by the load balancer controller, but it does not
guarantee that the load balancer is healthy.
"""


def create_k8s_service_load_balancer_ingress_count(
    meter, callbacks
):
    """Number of load balancer ingress points (external IPs/hostnames) assigned to the service"""
    return meter.create_observable_gauge(
        name=K8S_SERVICE_LOAD_BALANCER_INGRESS_COUNT,
        callbacks=callbacks,
        description="Number of load balancer ingress points (external IPs/hostnames) assigned to the service.",
        unit="{ingress}",
    )


K8S_STATEFULSET_CURRENT_PODS = "k8s.statefulset.current_pods"
"""
Deprecated: Replaced by `k8s.statefulset.pod.current`.
"""


def create_k8s_statefulset_current_pods(meter):
    """Deprecated, use `k8s.statefulset.pod.current` instead"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_CURRENT_PODS,
        description="Deprecated, use `k8s.statefulset.pod.current` instead.",
        unit="{pod}",
    )


K8S_STATEFULSET_DESIRED_PODS = "k8s.statefulset.desired_pods"
"""
Deprecated: Replaced by `k8s.statefulset.pod.desired`.
"""


def create_k8s_statefulset_desired_pods(meter):
    """Deprecated, use `k8s.statefulset.pod.desired` instead"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_DESIRED_PODS,
        description="Deprecated, use `k8s.statefulset.pod.desired` instead.",
        unit="{pod}",
    )


K8S_STATEFULSET_POD_CURRENT = "k8s.statefulset.pod.current"
"""
The number of replica pods created by the statefulset controller from the statefulset version indicated by currentRevision
Instrument
Unit: {pod}
Note: This metric aligns with the `currentReplicas` field of the
[K8s StatefulSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#statefulsetstatus-v1-apps).
"""


def create_k8s_statefulset_pod_current(meter):
    """The number of replica pods created by the statefulset controller from the statefulset version indicated by currentRevision"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_POD_CURRENT,
        description="The number of replica pods created by the statefulset controller from the statefulset version indicated by currentRevision.",
        unit="{pod}",
    )


K8S_STATEFULSET_POD_DESIRED = "k8s.statefulset.pod.desired"
"""
Number of desired replica pods in this statefulset
Instrument
Unit: {pod}
Note: This metric aligns with the `replicas` field of the
[K8s StatefulSetSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#statefulsetspec-v1-apps).
"""


def create_k8s_statefulset_pod_desired(meter):
    """Number of desired replica pods in this statefulset"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_POD_DESIRED,
        description="Number of desired replica pods in this statefulset.",
        unit="{pod}",
    )


K8S_STATEFULSET_POD_READY = "k8s.statefulset.pod.ready"
"""
The number of replica pods created for this statefulset with a Ready Condition
Instrument
Unit: {pod}
Note: This metric aligns with the `readyReplicas` field of the
[K8s StatefulSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#statefulsetstatus-v1-apps).
"""


def create_k8s_statefulset_pod_ready(meter):
    """The number of replica pods created for this statefulset with a Ready Condition"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_POD_READY,
        description="The number of replica pods created for this statefulset with a Ready Condition.",
        unit="{pod}",
    )


K8S_STATEFULSET_POD_UPDATED = "k8s.statefulset.pod.updated"
"""
Number of replica pods created by the statefulset controller from the statefulset version indicated by updateRevision
Instrument
Unit: {pod}
Note: This metric aligns with the `updatedReplicas` field of the
[K8s StatefulSetStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#statefulsetstatus-v1-apps).
"""


def create_k8s_statefulset_pod_updated(meter):
    """Number of replica pods created by the statefulset controller from the statefulset version indicated by updateRevision"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_POD_UPDATED,
        description="Number of replica pods created by the statefulset controller from the statefulset version indicated by updateRevision.",
        unit="{pod}",
    )


K8S_STATEFULSET_READY_PODS = "k8s.statefulset.ready_pods"
"""
Deprecated: Replaced by `k8s.statefulset.pod.ready`.
"""


def create_k8s_statefulset_ready_pods(meter):
    """Deprecated, use `k8s.statefulset.pod.ready` instead"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_READY_PODS,
        description="Deprecated, use `k8s.statefulset.pod.ready` instead.",
        unit="{pod}",
    )


K8S_STATEFULSET_UPDATED_PODS = "k8s.statefulset.updated_pods"
"""
Deprecated: Replaced by `k8s.statefulset.pod.updated`.
"""


def create_k8s_statefulset_updated_pods(meter):
    """Deprecated, use `k8s.statefulset.pod.updated` instead"""
    return meter.create_up_down_counter(
        name=K8S_STATEFULSET_UPDATED_PODS,
        description="Deprecated, use `k8s.statefulset.pod.updated` instead.",
        unit="{pod}",
    )

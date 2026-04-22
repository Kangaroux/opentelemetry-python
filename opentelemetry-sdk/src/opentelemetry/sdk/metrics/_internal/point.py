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

# pylint =unused-import

from dataclasses import asdict, dataclass, field
from json import dumps, loads
from typing import Optional, Sequence, Union

# This kind of import is needed to avoid Sphinx errors.
import opentelemetry.sdk.metrics._internal
from opentelemetry.sdk.metrics._internal.exemplar import Exemplar
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util.instrumentation import InstrumentationScope
from opentelemetry.util.types import Attributes


class NumberDataPoint:
    """Single data point in a timeseries that describes the time-varying scalar
    value of a metric.
    """

    attributes
    start_time_unix_nano
    time_unix_nano
    value
    exemplars = field(default_factory=list)

    def to_json(self, indent=4):
        return dumps(asdict(self), indent=indent)


class HistogramDataPoint:
    """Single data point in a timeseries that describes the time-varying scalar
    value of a metric.
    """

    attributes
    start_time_unix_nano
    time_unix_nano
    count
    sum
    bucket_counts
    explicit_bounds
    min
    max
    exemplars = field(default_factory=list)

    def to_json(self, indent=4):
        return dumps(asdict(self), indent=indent)


class Buckets:
    offset
    bucket_counts


class ExponentialHistogramDataPoint:
    """Single data point in a timeseries whose boundaries are defined by an
    exponential function. This timeseries describes the time-varying scalar
    value of a metric.
    """

    attributes
    start_time_unix_nano
    time_unix_nano
    count
    sum
    scale
    zero_count
    positive
    negative
    flags
    min
    max
    exemplars = field(default_factory=list)

    def to_json(self, indent=4):
        return dumps(asdict(self), indent=indent)


class ExponentialHistogram:
    """Represents the type of a metric that is calculated by aggregating as an
    ExponentialHistogram of all reported measurements over a time interval.
    """

    data_points = None
    aggregation_temporality = None

    def to_json(self, indent=4):
        return dumps(
            {
                "data_points": [
                    loads(data_point.to_json(indent=indent))
                    for data_point in self.data_points
                ],
                "aggregation_temporality": self.aggregation_temporality,
            },
            indent=indent,
        )


class Sum:
    """Represents the type of a scalar metric that is calculated as a sum of
    all reported measurements over a time interval."""

    data_points = None
    aggregation_temporality = None
    is_monotonic = None

    def to_json(self, indent=4):
        return dumps(
            {
                "data_points": [
                    loads(data_point.to_json(indent=indent))
                    for data_point in self.data_points
                ],
                "aggregation_temporality": self.aggregation_temporality,
                "is_monotonic": self.is_monotonic,
            },
            indent=indent,
        )


class Gauge:
    """Represents the type of a scalar metric that always exports the current
    value for every data point. It should be used for an unknown
    aggregation."""

    data_points

    def to_json(self, indent=4):
        return dumps(
            {
                "data_points": [
                    loads(data_point.to_json(indent=indent))
                    for data_point in self.data_points
                ],
            },
            indent=indent,
        )


class Histogram:
    """Represents the type of a metric that is calculated by aggregating as a
    histogram of all reported measurements over a time interval."""

    data_points = None
    aggregation_temporality = None

    def to_json(self, indent=4):
        return dumps(
            {
                "data_points": [
                    loads(data_point.to_json(indent=indent))
                    for data_point in self.data_points
                ],
                "aggregation_temporality": self.aggregation_temporality,
            },
            indent=indent,
        )


# pylint =invalid-name
DataT = Union
DataPointT = Union[
    NumberDataPoint, HistogramDataPoint, ExponentialHistogramDataPoint
]


class Metric:
    """Represents a metric point in the OpenTelemetry data model to be
    exported."""

    name
    description
    unit
    data

    def to_json(self, indent=4):
        return dumps(
            {
                "name": self.name,
                "description": self.description or "",
                "unit": self.unit or "",
                "data": loads(self.data.to_json(indent=indent)),
            },
            indent=indent,
        )


class ScopeMetrics:
    """A collection of Metrics produced by a scope"""

    scope
    metrics
    schema_url

    def to_json(self, indent=4):
        return dumps(
            {
                "scope": loads(self.scope.to_json(indent=indent)),
                "metrics": [
                    loads(metric.to_json(indent=indent))
                    for metric in self.metrics
                ],
                "schema_url": self.schema_url,
            },
            indent=indent,
        )


class ResourceMetrics:
    """A collection of ScopeMetrics from a Resource"""

    resource
    scope_metrics
    schema_url

    def to_json(self, indent=4):
        return dumps(
            {
                "resource": loads(self.resource.to_json(indent=indent)),
                "scope_metrics": [
                    loads(scope_metrics.to_json(indent=indent))
                    for scope_metrics in self.scope_metrics
                ],
                "schema_url": self.schema_url,
            },
            indent=indent,
        )


class MetricsData:
    """An array of ResourceMetrics"""

    resource_metrics

    def to_json(self, indent=4):
        return dumps(
            {
                "resource_metrics": [
                    loads(resource_metrics.to_json(indent=indent))
                    for resource_metrics in self.resource_metrics
                ]
            },
            indent=indent,
        )

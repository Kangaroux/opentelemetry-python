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

from json import dumps, loads
from typing import Optional, Sequence, Union

# This kind of import is needed to avoid Sphinx errors.
import opentelemetry.sdk.metrics._internal
from opentelemetry.sdk.metrics._internal.exemplar import Exemplar
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util.instrumentation import InstrumentationScope
from opentelemetry.util.types import Attributes


def _asdict(obj):
    """Recursively convert an object to a dict, similar to dataclasses.asdict."""
    if hasattr(obj, '__dict__') and not isinstance(obj, type):
        result = {}
        for k, v in obj.__dict__.items():
            result[k] = _asdict(v)
        return result
    elif isinstance(obj, dict):
        return {k: _asdict(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return type(obj)(_asdict(item) for item in obj)
    elif isinstance(obj, (set, frozenset)):
        return [_asdict(item) for item in obj]
    return obj


class NumberDataPoint(object):
    """Single data point in a timeseries that describes the time-varying scalar
    value of a metric.
    """

    def __init__(self, attributes=None, start_time_unix_nano=None, time_unix_nano=None, value=None, exemplars=None):
        self.attributes = attributes
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.value = value
        self.exemplars = exemplars if exemplars is not None else []

    def __eq__(self, other):
        if not isinstance(other, NumberDataPoint):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "NumberDataPoint(attributes={}, start_time_unix_nano={}, time_unix_nano={}, value={}, exemplars={})".format(
            self.attributes, self.start_time_unix_nano, self.time_unix_nano, self.value, self.exemplars)

    def to_json(self, indent=4):
        return dumps(_asdict(self), indent=indent)


class HistogramDataPoint(object):
    """Single data point in a timeseries that describes the time-varying scalar
    value of a metric.
    """

    def __init__(self, attributes=None, start_time_unix_nano=None, time_unix_nano=None, count=None, sum=None, bucket_counts=None, explicit_bounds=None, min=None, max=None, exemplars=None):
        self.attributes = attributes
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.count = count
        self.sum = sum
        self.bucket_counts = bucket_counts
        self.explicit_bounds = explicit_bounds
        self.min = min
        self.max = max
        self.exemplars = exemplars if exemplars is not None else []

    def __eq__(self, other):
        if not isinstance(other, HistogramDataPoint):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "HistogramDataPoint(attributes={}, start_time_unix_nano={}, time_unix_nano={}, count={}, sum={}, bucket_counts={}, explicit_bounds={}, min={}, max={}, exemplars={})".format(
            self.attributes, self.start_time_unix_nano, self.time_unix_nano, self.count, self.sum, self.bucket_counts, self.explicit_bounds, self.min, self.max, self.exemplars)

    def to_json(self, indent=4):
        return dumps(_asdict(self), indent=indent)


class Buckets(object):

    def __init__(self, offset=None, bucket_counts=None):
        self.offset = offset
        self.bucket_counts = bucket_counts

    def __eq__(self, other):
        if not isinstance(other, Buckets):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Buckets(offset={}, bucket_counts={})".format(self.offset, self.bucket_counts)


class ExponentialHistogramDataPoint(object):
    """Single data point in a timeseries whose boundaries are defined by an
    exponential function. This timeseries describes the time-varying scalar
    value of a metric.
    """

    def __init__(self, attributes=None, start_time_unix_nano=None, time_unix_nano=None, count=None, sum=None, scale=None, zero_count=None, positive=None, negative=None, flags=None, min=None, max=None, exemplars=None):
        self.attributes = attributes
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.count = count
        self.sum = sum
        self.scale = scale
        self.zero_count = zero_count
        self.positive = positive
        self.negative = negative
        self.flags = flags
        self.min = min
        self.max = max
        self.exemplars = exemplars if exemplars is not None else []

    def __eq__(self, other):
        if not isinstance(other, ExponentialHistogramDataPoint):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "ExponentialHistogramDataPoint(attributes={}, start_time_unix_nano={}, time_unix_nano={}, count={}, sum={}, scale={}, zero_count={}, positive={}, negative={}, flags={}, min={}, max={}, exemplars={})".format(
            self.attributes, self.start_time_unix_nano, self.time_unix_nano, self.count, self.sum, self.scale, self.zero_count, self.positive, self.negative, self.flags, self.min, self.max, self.exemplars)

    def to_json(self, indent=4):
        return dumps(_asdict(self), indent=indent)


class ExponentialHistogram(object):
    """Represents the type of a metric that is calculated by aggregating as an
    ExponentialHistogram of all reported measurements over a time interval.
    """

    def __init__(self, data_points=None, aggregation_temporality=None):
        self.data_points = data_points
        self.aggregation_temporality = aggregation_temporality

    def __eq__(self, other):
        if not isinstance(other, ExponentialHistogram):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "ExponentialHistogram(data_points={}, aggregation_temporality={})".format(
            self.data_points, self.aggregation_temporality)

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


class Sum(object):
    """Represents the type of a scalar metric that is calculated as a sum of
    all reported measurements over a time interval."""

    def __init__(self, data_points=None, aggregation_temporality=None, is_monotonic=None):
        self.data_points = data_points
        self.aggregation_temporality = aggregation_temporality
        self.is_monotonic = is_monotonic

    def __eq__(self, other):
        if not isinstance(other, Sum):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Sum(data_points={}, aggregation_temporality={}, is_monotonic={})".format(
            self.data_points, self.aggregation_temporality, self.is_monotonic)

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


class Gauge(object):
    """Represents the type of a scalar metric that always exports the current
    value for every data point. It should be used for an unknown
    aggregation."""

    def __init__(self, data_points=None):
        self.data_points = data_points

    def __eq__(self, other):
        if not isinstance(other, Gauge):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Gauge(data_points={})".format(self.data_points)

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


class Histogram(object):
    """Represents the type of a metric that is calculated by aggregating as a
    histogram of all reported measurements over a time interval."""

    def __init__(self, data_points=None, aggregation_temporality=None):
        self.data_points = data_points
        self.aggregation_temporality = aggregation_temporality

    def __eq__(self, other):
        if not isinstance(other, Histogram):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Histogram(data_points={}, aggregation_temporality={})".format(
            self.data_points, self.aggregation_temporality)

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


class Metric(object):
    """Represents a metric point in the OpenTelemetry data model to be
    exported."""

    def __init__(self, name=None, description=None, unit=None, data=None):
        self.name = name
        self.description = description
        self.unit = unit
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Metric):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "Metric(name={}, description={}, unit={}, data={})".format(
            self.name, self.description, self.unit, self.data)

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


class ScopeMetrics(object):
    """A collection of Metrics produced by a scope"""

    def __init__(self, scope=None, metrics=None, schema_url=None):
        self.scope = scope
        self.metrics = metrics
        self.schema_url = schema_url

    def __eq__(self, other):
        if not isinstance(other, ScopeMetrics):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "ScopeMetrics(scope={}, metrics={}, schema_url={})".format(
            self.scope, self.metrics, self.schema_url)

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


class ResourceMetrics(object):
    """A collection of ScopeMetrics from a Resource"""

    def __init__(self, resource=None, scope_metrics=None, schema_url=None):
        self.resource = resource
        self.scope_metrics = scope_metrics
        self.schema_url = schema_url

    def __eq__(self, other):
        if not isinstance(other, ResourceMetrics):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "ResourceMetrics(resource={}, scope_metrics={}, schema_url={})".format(
            self.resource, self.scope_metrics, self.schema_url)

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


class MetricsData(object):
    """An array of ResourceMetrics"""

    def __init__(self, resource_metrics=None):
        self.resource_metrics = resource_metrics

    def __eq__(self, other):
        if not isinstance(other, MetricsData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "MetricsData(resource_metrics={})".format(self.resource_metrics)

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

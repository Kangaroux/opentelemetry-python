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

# AUTO-GENERATED from "opentelemetry/proto/metrics/v1/metrics.proto"
# DO NOT EDIT MANUALLY

import builtins
import dataclasses
import enum
import functools
import sys
import typing

if sys.version_info >= (3, 10):
    _dataclass = functools.partial(dataclasses.dataclass, slots=True)
else:
    _dataclass = dataclasses.dataclass

import opentelemetry.proto_json._json_codec
import opentelemetry.proto_json.common.v1.common
import opentelemetry.proto_json.resource.v1.resource


@typing.final
class AggregationTemporality(enum.IntEnum):
    """
    Generated from protobuf enum AggregationTemporality
    """

    AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
    AGGREGATION_TEMPORALITY_DELTA = 1
    AGGREGATION_TEMPORALITY_CUMULATIVE = 2

@typing.final
class DataPointFlags(enum.IntEnum):
    """
    Generated from protobuf enum DataPointFlags
    """

    DATA_POINT_FLAGS_DO_NOT_USE = 0
    DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1

@typing.final
@_dataclass
class MetricsData(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message MetricsData
    """

    resource_metrics = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.resource_metrics:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.resource_metrics, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            MetricsData instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceMetrics")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ResourceMetrics.from_dict(_v), "resource_metrics")

        return cls(**_args)


@typing.final
@_dataclass
class ResourceMetrics(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ResourceMetrics
    """

    resource = None
    scope_metrics = dataclasses.field(default_factory=builtins.list)
    schema_url = ""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.resource:
            _result = self.resource.to_dict()
        if self.scope_metrics:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.scope_metrics, lambda _v: _v.to_dict())
        if self.schema_url:
            _result = self.schema_url
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ResourceMetrics instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resource")
        if _value is not None:
            _args = opentelemetry.proto_json.resource.v1.resource.Resource.from_dict(_value)
        _value = data.get("scopeMetrics")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ScopeMetrics.from_dict(_v), "scope_metrics")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class ScopeMetrics(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ScopeMetrics
    """

    scope = None
    metrics = dataclasses.field(default_factory=builtins.list)
    schema_url = ""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.scope:
            _result = self.scope.to_dict()
        if self.metrics:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.metrics, lambda _v: _v.to_dict())
        if self.schema_url:
            _result = self.schema_url
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ScopeMetrics instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("scope")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.InstrumentationScope.from_dict(_value)
        _value = data.get("metrics")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Metric.from_dict(_v), "metrics")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Metric(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Metric
    """

    name = ""
    description = ""
    unit = ""
    gauge = None
    sum = None
    histogram = None
    exponential_histogram = None
    summary = None
    metadata = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.name:
            _result = self.name
        if self.description:
            _result = self.description
        if self.unit:
            _result = self.unit
        if self.metadata:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.metadata, lambda _v: _v.to_dict())
        if self.summary is not None:
            _result = self.summary.to_dict()
        elif self.exponential_histogram is not None:
            _result = self.exponential_histogram.to_dict()
        elif self.histogram is not None:
            _result = self.histogram.to_dict()
        elif self.sum is not None:
            _result = self.sum.to_dict()
        elif self.gauge is not None:
            _result = self.gauge.to_dict()
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Metric instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("name")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "name")
            _args = _value
        _value = data.get("description")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "description")
            _args = _value
        _value = data.get("unit")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "unit")
            _args = _value
        _value = data.get("metadata")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "metadata")
        _value = data.get("summary")
        if _value is not None:
            _args = Summary.from_dict(_value)
        _value = data.get("exponentialHistogram")
        if _value is not None:
            _args = ExponentialHistogram.from_dict(_value)
        _value = data.get("histogram")
        if _value is not None:
            _args = Histogram.from_dict(_value)
        _value = data.get("sum")
        if _value is not None:
            _args = Sum.from_dict(_value)
        _value = data.get("gauge")
        if _value is not None:
            _args = Gauge.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class Gauge(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Gauge
    """

    data_points = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.data_points:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.data_points, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Gauge instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("dataPoints")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: NumberDataPoint.from_dict(_v), "data_points")

        return cls(**_args)


@typing.final
@_dataclass
class Sum(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Sum
    """

    data_points = dataclasses.field(default_factory=builtins.list)
    aggregation_temporality = 0
    is_monotonic = False

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.data_points:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.data_points, lambda _v: _v.to_dict())
        if self.aggregation_temporality:
            _result = builtins.int(self.aggregation_temporality)
        if self.is_monotonic:
            _result = self.is_monotonic
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Sum instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("dataPoints")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: NumberDataPoint.from_dict(_v), "data_points")
        _value = data.get("aggregationTemporality")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "aggregation_temporality")
            _args = AggregationTemporality(_value)
        _value = data.get("isMonotonic")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.bool, "is_monotonic")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Histogram(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Histogram
    """

    data_points = dataclasses.field(default_factory=builtins.list)
    aggregation_temporality = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.data_points:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.data_points, lambda _v: _v.to_dict())
        if self.aggregation_temporality:
            _result = builtins.int(self.aggregation_temporality)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Histogram instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("dataPoints")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: HistogramDataPoint.from_dict(_v), "data_points")
        _value = data.get("aggregationTemporality")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "aggregation_temporality")
            _args = AggregationTemporality(_value)

        return cls(**_args)


@typing.final
@_dataclass
class ExponentialHistogram(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExponentialHistogram
    """

    data_points = dataclasses.field(default_factory=builtins.list)
    aggregation_temporality = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.data_points:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.data_points, lambda _v: _v.to_dict())
        if self.aggregation_temporality:
            _result = builtins.int(self.aggregation_temporality)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ExponentialHistogram instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("dataPoints")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ExponentialHistogramDataPoint.from_dict(_v), "data_points")
        _value = data.get("aggregationTemporality")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "aggregation_temporality")
            _args = AggregationTemporality(_value)

        return cls(**_args)


@typing.final
@_dataclass
class Summary(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Summary
    """

    data_points = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.data_points:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.data_points, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Summary instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("dataPoints")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: SummaryDataPoint.from_dict(_v), "data_points")

        return cls(**_args)


@typing.final
@_dataclass
class NumberDataPoint(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message NumberDataPoint
    """

    attributes = dataclasses.field(default_factory=builtins.list)
    start_time_unix_nano = 0
    time_unix_nano = 0
    as_double = None
    as_int = None
    exemplars = dataclasses.field(default_factory=builtins.list)
    flags = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.start_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_time_unix_nano)
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.exemplars:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.exemplars, lambda _v: _v.to_dict())
        if self.flags:
            _result = self.flags
        if self.as_int is not None:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.as_int)
        elif self.as_double is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.as_double)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            NumberDataPoint instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("startTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_time_unix_nano")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("exemplars")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Exemplar.from_dict(_v), "exemplars")
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value
        _value = data.get("asInt")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "as_int")
        _value = data.get("asDouble")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "as_double")

        return cls(**_args)


@typing.final
@_dataclass
class HistogramDataPoint(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message HistogramDataPoint
    """

    attributes = dataclasses.field(default_factory=builtins.list)
    start_time_unix_nano = 0
    time_unix_nano = 0
    count = 0
    sum = None
    bucket_counts = dataclasses.field(default_factory=builtins.list)
    explicit_bounds = dataclasses.field(default_factory=builtins.list)
    exemplars = dataclasses.field(default_factory=builtins.list)
    flags = 0
    min = None
    max = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.start_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_time_unix_nano)
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.count:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.count)
        if self.sum is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.sum)
        if self.bucket_counts:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.bucket_counts, lambda _v: opentelemetry.proto_json._json_codec.encode_int64(_v))
        if self.explicit_bounds:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.explicit_bounds, lambda _v: opentelemetry.proto_json._json_codec.encode_float(_v))
        if self.exemplars:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.exemplars, lambda _v: _v.to_dict())
        if self.flags:
            _result = self.flags
        if self.min is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.min)
        if self.max is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.max)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            HistogramDataPoint instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("startTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_time_unix_nano")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("count")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "count")
        _value = data.get("sum")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "sum")
        _value = data.get("bucketCounts")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json._json_codec.decode_int64(_v, "bucket_counts"), "bucket_counts")
        _value = data.get("explicitBounds")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json._json_codec.decode_float(_v, "explicit_bounds"), "explicit_bounds")
        _value = data.get("exemplars")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Exemplar.from_dict(_v), "exemplars")
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value
        _value = data.get("min")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "min")
        _value = data.get("max")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "max")

        return cls(**_args)


@typing.final
@_dataclass
class ExponentialHistogramDataPoint(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExponentialHistogramDataPoint
    """

    @typing.final
    @_dataclass
    class Buckets(opentelemetry.proto_json._json_codec.JsonMessage):
        """
        Generated from protobuf message Buckets
        """

        offset = 0
        bucket_counts = dataclasses.field(default_factory=builtins.list)

        def to_dict(self):
            """
            Convert this message to a dictionary with lowerCamelCase keys.

            Returns:
                Dictionary representation following OTLP JSON encoding
            """
            _result = {}
            if self.offset:
                _result = self.offset
            if self.bucket_counts:
                _result = opentelemetry.proto_json._json_codec.encode_repeated(self.bucket_counts, lambda _v: opentelemetry.proto_json._json_codec.encode_int64(_v))
            return _result

        @builtins.classmethod
        def from_dict(cls, data):
            """
            Create from a dictionary with lowerCamelCase keys.

            Args:
                data: Dictionary representation following OTLP JSON encoding

            Returns:
                Buckets instance
            """
            opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
            _args = {}

            _value = data.get("offset")
            if _value is not None:
                opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "offset")
                _args = _value
            _value = data.get("bucketCounts")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json._json_codec.decode_int64(_v, "bucket_counts"), "bucket_counts")

            return cls(**_args)

    attributes = dataclasses.field(default_factory=builtins.list)
    start_time_unix_nano = 0
    time_unix_nano = 0
    count = 0
    sum = None
    scale = 0
    zero_count = 0
    positive = None
    negative = None
    flags = 0
    exemplars = dataclasses.field(default_factory=builtins.list)
    min = None
    max = None
    zero_threshold = 0.0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.start_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_time_unix_nano)
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.count:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.count)
        if self.sum is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.sum)
        if self.scale:
            _result = self.scale
        if self.zero_count:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.zero_count)
        if self.positive:
            _result = self.positive.to_dict()
        if self.negative:
            _result = self.negative.to_dict()
        if self.flags:
            _result = self.flags
        if self.exemplars:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.exemplars, lambda _v: _v.to_dict())
        if self.min is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.min)
        if self.max is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.max)
        if self.zero_threshold:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.zero_threshold)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ExponentialHistogramDataPoint instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("startTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_time_unix_nano")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("count")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "count")
        _value = data.get("sum")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "sum")
        _value = data.get("scale")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "scale")
            _args = _value
        _value = data.get("zeroCount")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "zero_count")
        _value = data.get("positive")
        if _value is not None:
            _args = ExponentialHistogramDataPoint.Buckets.from_dict(_value)
        _value = data.get("negative")
        if _value is not None:
            _args = ExponentialHistogramDataPoint.Buckets.from_dict(_value)
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value
        _value = data.get("exemplars")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Exemplar.from_dict(_v), "exemplars")
        _value = data.get("min")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "min")
        _value = data.get("max")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "max")
        _value = data.get("zeroThreshold")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "zero_threshold")

        return cls(**_args)


@typing.final
@_dataclass
class SummaryDataPoint(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message SummaryDataPoint
    """

    @typing.final
    @_dataclass
    class ValueAtQuantile(opentelemetry.proto_json._json_codec.JsonMessage):
        """
        Generated from protobuf message ValueAtQuantile
        """

        quantile = 0.0
        value = 0.0

        def to_dict(self):
            """
            Convert this message to a dictionary with lowerCamelCase keys.

            Returns:
                Dictionary representation following OTLP JSON encoding
            """
            _result = {}
            if self.quantile:
                _result = opentelemetry.proto_json._json_codec.encode_float(self.quantile)
            if self.value:
                _result = opentelemetry.proto_json._json_codec.encode_float(self.value)
            return _result

        @builtins.classmethod
        def from_dict(cls, data):
            """
            Create from a dictionary with lowerCamelCase keys.

            Args:
                data: Dictionary representation following OTLP JSON encoding

            Returns:
                ValueAtQuantile instance
            """
            opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
            _args = {}

            _value = data.get("quantile")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_float(_value, "quantile")
            _value = data.get("value")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_float(_value, "value")

            return cls(**_args)

    attributes = dataclasses.field(default_factory=builtins.list)
    start_time_unix_nano = 0
    time_unix_nano = 0
    count = 0
    sum = 0.0
    quantile_values = dataclasses.field(default_factory=builtins.list)
    flags = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.start_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_time_unix_nano)
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.count:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.count)
        if self.sum:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.sum)
        if self.quantile_values:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.quantile_values, lambda _v: _v.to_dict())
        if self.flags:
            _result = self.flags
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            SummaryDataPoint instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("startTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_time_unix_nano")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("count")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "count")
        _value = data.get("sum")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "sum")
        _value = data.get("quantileValues")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: SummaryDataPoint.ValueAtQuantile.from_dict(_v), "quantile_values")
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Exemplar(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Exemplar
    """

    filtered_attributes = dataclasses.field(default_factory=builtins.list)
    time_unix_nano = 0
    as_double = None
    as_int = None
    span_id = b""
    trace_id = b""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.filtered_attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.filtered_attributes, lambda _v: _v.to_dict())
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.span_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.span_id)
        if self.trace_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.trace_id)
        if self.as_int is not None:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.as_int)
        elif self.as_double is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.as_double)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Exemplar instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("filteredAttributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "filtered_attributes")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("spanId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "span_id")
        _value = data.get("traceId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "trace_id")
        _value = data.get("asInt")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "as_int")
        _value = data.get("asDouble")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "as_double")

        return cls(**_args)

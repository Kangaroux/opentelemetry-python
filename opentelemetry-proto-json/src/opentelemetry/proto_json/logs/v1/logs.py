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

# AUTO-GENERATED from "opentelemetry/proto/logs/v1/logs.proto"
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
class SeverityNumber(enum.IntEnum):
    """
    Generated from protobuf enum SeverityNumber
    """

    SEVERITY_NUMBER_UNSPECIFIED = 0
    SEVERITY_NUMBER_TRACE = 1
    SEVERITY_NUMBER_TRACE2 = 2
    SEVERITY_NUMBER_TRACE3 = 3
    SEVERITY_NUMBER_TRACE4 = 4
    SEVERITY_NUMBER_DEBUG = 5
    SEVERITY_NUMBER_DEBUG2 = 6
    SEVERITY_NUMBER_DEBUG3 = 7
    SEVERITY_NUMBER_DEBUG4 = 8
    SEVERITY_NUMBER_INFO = 9
    SEVERITY_NUMBER_INFO2 = 10
    SEVERITY_NUMBER_INFO3 = 11
    SEVERITY_NUMBER_INFO4 = 12
    SEVERITY_NUMBER_WARN = 13
    SEVERITY_NUMBER_WARN2 = 14
    SEVERITY_NUMBER_WARN3 = 15
    SEVERITY_NUMBER_WARN4 = 16
    SEVERITY_NUMBER_ERROR = 17
    SEVERITY_NUMBER_ERROR2 = 18
    SEVERITY_NUMBER_ERROR3 = 19
    SEVERITY_NUMBER_ERROR4 = 20
    SEVERITY_NUMBER_FATAL = 21
    SEVERITY_NUMBER_FATAL2 = 22
    SEVERITY_NUMBER_FATAL3 = 23
    SEVERITY_NUMBER_FATAL4 = 24

@typing.final
class LogRecordFlags(enum.IntEnum):
    """
    Generated from protobuf enum LogRecordFlags
    """

    LOG_RECORD_FLAGS_DO_NOT_USE = 0
    LOG_RECORD_FLAGS_TRACE_FLAGS_MASK = 255

@typing.final
@_dataclass
class LogsData(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message LogsData
    """

    resource_logs = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.resource_logs:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.resource_logs, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            LogsData instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceLogs")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ResourceLogs.from_dict(_v), "resource_logs")

        return cls(**_args)


@typing.final
@_dataclass
class ResourceLogs(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ResourceLogs
    """

    resource = None
    scope_logs = dataclasses.field(default_factory=builtins.list)
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
        if self.scope_logs:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.scope_logs, lambda _v: _v.to_dict())
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
            ResourceLogs instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resource")
        if _value is not None:
            _args = opentelemetry.proto_json.resource.v1.resource.Resource.from_dict(_value)
        _value = data.get("scopeLogs")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ScopeLogs.from_dict(_v), "scope_logs")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class ScopeLogs(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ScopeLogs
    """

    scope = None
    log_records = dataclasses.field(default_factory=builtins.list)
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
        if self.log_records:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.log_records, lambda _v: _v.to_dict())
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
            ScopeLogs instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("scope")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.InstrumentationScope.from_dict(_value)
        _value = data.get("logRecords")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: LogRecord.from_dict(_v), "log_records")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class LogRecord(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message LogRecord
    """

    time_unix_nano = 0
    observed_time_unix_nano = 0
    severity_number = 0
    severity_text = ""
    body = None
    attributes = dataclasses.field(default_factory=builtins.list)
    dropped_attributes_count = 0
    flags = 0
    trace_id = b""
    span_id = b""
    event_name = ""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.observed_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.observed_time_unix_nano)
        if self.severity_number:
            _result = builtins.int(self.severity_number)
        if self.severity_text:
            _result = self.severity_text
        if self.body:
            _result = self.body.to_dict()
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.dropped_attributes_count:
            _result = self.dropped_attributes_count
        if self.flags:
            _result = self.flags
        if self.trace_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.trace_id)
        if self.span_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.span_id)
        if self.event_name:
            _result = self.event_name
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            LogRecord instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("observedTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "observed_time_unix_nano")
        _value = data.get("severityNumber")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "severity_number")
            _args = SeverityNumber(_value)
        _value = data.get("severityText")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "severity_text")
            _args = _value
        _value = data.get("body")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.AnyValue.from_dict(_value)
        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("droppedAttributesCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_attributes_count")
            _args = _value
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value
        _value = data.get("traceId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "trace_id")
        _value = data.get("spanId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "span_id")
        _value = data.get("eventName")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "event_name")
            _args = _value

        return cls(**_args)

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

# AUTO-GENERATED from "opentelemetry/proto/collector/logs/v1/logs_service.proto"
# DO NOT EDIT MANUALLY

import builtins
import dataclasses
import functools
import sys
import typing

if sys.version_info >= (3, 10):
    _dataclass = functools.partial(dataclasses.dataclass, slots=True)
else:
    _dataclass = dataclasses.dataclass

import opentelemetry.proto_json._json_codec
import opentelemetry.proto_json.logs.v1.logs


@typing.final
@_dataclass
class ExportLogsServiceRequest(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportLogsServiceRequest
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
            ExportLogsServiceRequest instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceLogs")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.logs.v1.logs.ResourceLogs.from_dict(_v), "resource_logs")

        return cls(**_args)


@typing.final
@_dataclass
class ExportLogsServiceResponse(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportLogsServiceResponse
    """

    partial_success = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.partial_success:
            _result = self.partial_success.to_dict()
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ExportLogsServiceResponse instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("partialSuccess")
        if _value is not None:
            _args = ExportLogsPartialSuccess.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class ExportLogsPartialSuccess(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportLogsPartialSuccess
    """

    rejected_log_records = 0
    error_message = ""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.rejected_log_records:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.rejected_log_records)
        if self.error_message:
            _result = self.error_message
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ExportLogsPartialSuccess instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("rejectedLogRecords")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "rejected_log_records")
        _value = data.get("errorMessage")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "error_message")
            _args = _value

        return cls(**_args)

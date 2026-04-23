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

# AUTO-GENERATED from "opentelemetry/proto/collector/trace/v1/trace_service.proto"
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
import opentelemetry.proto_json.trace.v1.trace


@typing.final
@_dataclass
class ExportTraceServiceRequest(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportTraceServiceRequest
    """

    resource_spans = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.resource_spans:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.resource_spans, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ExportTraceServiceRequest instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceSpans")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.trace.v1.trace.ResourceSpans.from_dict(_v), "resource_spans")

        return cls(**_args)


@typing.final
@_dataclass
class ExportTraceServiceResponse(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportTraceServiceResponse
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
            ExportTraceServiceResponse instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("partialSuccess")
        if _value is not None:
            _args = ExportTracePartialSuccess.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class ExportTracePartialSuccess(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ExportTracePartialSuccess
    """

    rejected_spans = 0
    error_message = ""

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.rejected_spans:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.rejected_spans)
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
            ExportTracePartialSuccess instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("rejectedSpans")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "rejected_spans")
        _value = data.get("errorMessage")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "error_message")
            _args = _value

        return cls(**_args)

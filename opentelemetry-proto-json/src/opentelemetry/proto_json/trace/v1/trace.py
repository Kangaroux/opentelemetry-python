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

# AUTO-GENERATED from "opentelemetry/proto/trace/v1/trace.proto"
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
class SpanFlags(enum.IntEnum):
    """
    Generated from protobuf enum SpanFlags
    """

    SPAN_FLAGS_DO_NOT_USE = 0
    SPAN_FLAGS_TRACE_FLAGS_MASK = 255
    SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 256
    SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 512

@typing.final
@_dataclass
class TracesData(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message TracesData
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
            TracesData instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceSpans")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ResourceSpans.from_dict(_v), "resource_spans")

        return cls(**_args)


@typing.final
@_dataclass
class ResourceSpans(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ResourceSpans
    """

    resource = None
    scope_spans = dataclasses.field(default_factory=builtins.list)
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
        if self.scope_spans:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.scope_spans, lambda _v: _v.to_dict())
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
            ResourceSpans instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resource")
        if _value is not None:
            _args = opentelemetry.proto_json.resource.v1.resource.Resource.from_dict(_value)
        _value = data.get("scopeSpans")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ScopeSpans.from_dict(_v), "scope_spans")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class ScopeSpans(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ScopeSpans
    """

    scope = None
    spans = dataclasses.field(default_factory=builtins.list)
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
        if self.spans:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.spans, lambda _v: _v.to_dict())
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
            ScopeSpans instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("scope")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.InstrumentationScope.from_dict(_value)
        _value = data.get("spans")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Span.from_dict(_v), "spans")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Span(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Span
    """

    @typing.final
    class SpanKind(enum.IntEnum):
        """
        Generated from protobuf enum SpanKind
        """

        SPAN_KIND_UNSPECIFIED = 0
        SPAN_KIND_INTERNAL = 1
        SPAN_KIND_SERVER = 2
        SPAN_KIND_CLIENT = 3
        SPAN_KIND_PRODUCER = 4
        SPAN_KIND_CONSUMER = 5

    @typing.final
    @_dataclass
    class Event(opentelemetry.proto_json._json_codec.JsonMessage):
        """
        Generated from protobuf message Event
        """

        time_unix_nano = 0
        name = ""
        attributes = dataclasses.field(default_factory=builtins.list)
        dropped_attributes_count = 0

        def to_dict(self):
            """
            Convert this message to a dictionary with lowerCamelCase keys.

            Returns:
                Dictionary representation following OTLP JSON encoding
            """
            _result = {}
            if self.time_unix_nano:
                _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
            if self.name:
                _result = self.name
            if self.attributes:
                _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
            if self.dropped_attributes_count:
                _result = self.dropped_attributes_count
            return _result

        @builtins.classmethod
        def from_dict(cls, data):
            """
            Create from a dictionary with lowerCamelCase keys.

            Args:
                data: Dictionary representation following OTLP JSON encoding

            Returns:
                Event instance
            """
            opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
            _args = {}

            _value = data.get("timeUnixNano")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
            _value = data.get("name")
            if _value is not None:
                opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "name")
                _args = _value
            _value = data.get("attributes")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
            _value = data.get("droppedAttributesCount")
            if _value is not None:
                opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_attributes_count")
                _args = _value

            return cls(**_args)

    @typing.final
    @_dataclass
    class Link(opentelemetry.proto_json._json_codec.JsonMessage):
        """
        Generated from protobuf message Link
        """

        trace_id = b""
        span_id = b""
        trace_state = ""
        attributes = dataclasses.field(default_factory=builtins.list)
        dropped_attributes_count = 0
        flags = 0

        def to_dict(self):
            """
            Convert this message to a dictionary with lowerCamelCase keys.

            Returns:
                Dictionary representation following OTLP JSON encoding
            """
            _result = {}
            if self.trace_id:
                _result = opentelemetry.proto_json._json_codec.encode_hex(self.trace_id)
            if self.span_id:
                _result = opentelemetry.proto_json._json_codec.encode_hex(self.span_id)
            if self.trace_state:
                _result = self.trace_state
            if self.attributes:
                _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
            if self.dropped_attributes_count:
                _result = self.dropped_attributes_count
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
                Link instance
            """
            opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
            _args = {}

            _value = data.get("traceId")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "trace_id")
            _value = data.get("spanId")
            if _value is not None:
                _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "span_id")
            _value = data.get("traceState")
            if _value is not None:
                opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "trace_state")
                _args = _value
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

            return cls(**_args)

    trace_id = b""
    span_id = b""
    trace_state = ""
    parent_span_id = b""
    flags = 0
    name = ""
    kind = 0
    start_time_unix_nano = 0
    end_time_unix_nano = 0
    attributes = dataclasses.field(default_factory=builtins.list)
    dropped_attributes_count = 0
    events = dataclasses.field(default_factory=builtins.list)
    dropped_events_count = 0
    links = dataclasses.field(default_factory=builtins.list)
    dropped_links_count = 0
    status = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.trace_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.trace_id)
        if self.span_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.span_id)
        if self.trace_state:
            _result = self.trace_state
        if self.parent_span_id:
            _result = opentelemetry.proto_json._json_codec.encode_hex(self.parent_span_id)
        if self.flags:
            _result = self.flags
        if self.name:
            _result = self.name
        if self.kind:
            _result = builtins.int(self.kind)
        if self.start_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_time_unix_nano)
        if self.end_time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.end_time_unix_nano)
        if self.attributes:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attributes, lambda _v: _v.to_dict())
        if self.dropped_attributes_count:
            _result = self.dropped_attributes_count
        if self.events:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.events, lambda _v: _v.to_dict())
        if self.dropped_events_count:
            _result = self.dropped_events_count
        if self.links:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.links, lambda _v: _v.to_dict())
        if self.dropped_links_count:
            _result = self.dropped_links_count
        if self.status:
            _result = self.status.to_dict()
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Span instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("traceId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "trace_id")
        _value = data.get("spanId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "span_id")
        _value = data.get("traceState")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "trace_state")
            _args = _value
        _value = data.get("parentSpanId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_hex(_value, "parent_span_id")
        _value = data.get("flags")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "flags")
            _args = _value
        _value = data.get("name")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "name")
            _args = _value
        _value = data.get("kind")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "kind")
            _args = Span.SpanKind(_value)
        _value = data.get("startTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_time_unix_nano")
        _value = data.get("endTimeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "end_time_unix_nano")
        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json.common.v1.common.KeyValue.from_dict(_v), "attributes")
        _value = data.get("droppedAttributesCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_attributes_count")
            _args = _value
        _value = data.get("events")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Span.Event.from_dict(_v), "events")
        _value = data.get("droppedEventsCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_events_count")
            _args = _value
        _value = data.get("links")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Span.Link.from_dict(_v), "links")
        _value = data.get("droppedLinksCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_links_count")
            _args = _value
        _value = data.get("status")
        if _value is not None:
            _args = Status.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class Status(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Status
    """

    @typing.final
    class StatusCode(enum.IntEnum):
        """
        Generated from protobuf enum StatusCode
        """

        STATUS_CODE_UNSET = 0
        STATUS_CODE_OK = 1
        STATUS_CODE_ERROR = 2

    message = ""
    code = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.message:
            _result = self.message
        if self.code:
            _result = builtins.int(self.code)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Status instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("message")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "message")
            _args = _value
        _value = data.get("code")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "code")
            _args = Status.StatusCode(_value)

        return cls(**_args)

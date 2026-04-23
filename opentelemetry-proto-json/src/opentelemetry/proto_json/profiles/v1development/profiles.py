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

# AUTO-GENERATED from "opentelemetry/proto/profiles/v1development/profiles.proto"
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
import opentelemetry.proto_json.common.v1.common
import opentelemetry.proto_json.resource.v1.resource


@typing.final
@_dataclass
class ProfilesDictionary(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ProfilesDictionary
    """

    mapping_table = dataclasses.field(default_factory=builtins.list)
    location_table = dataclasses.field(default_factory=builtins.list)
    function_table = dataclasses.field(default_factory=builtins.list)
    link_table = dataclasses.field(default_factory=builtins.list)
    string_table = dataclasses.field(default_factory=builtins.list)
    attribute_table = dataclasses.field(default_factory=builtins.list)
    stack_table = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.mapping_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.mapping_table, lambda _v: _v.to_dict())
        if self.location_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.location_table, lambda _v: _v.to_dict())
        if self.function_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.function_table, lambda _v: _v.to_dict())
        if self.link_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.link_table, lambda _v: _v.to_dict())
        if self.string_table:
            _result = self.string_table
        if self.attribute_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.attribute_table, lambda _v: _v.to_dict())
        if self.stack_table:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.stack_table, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ProfilesDictionary instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("mappingTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Mapping.from_dict(_v), "mapping_table")
        _value = data.get("locationTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Location.from_dict(_v), "location_table")
        _value = data.get("functionTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Function.from_dict(_v), "function_table")
        _value = data.get("linkTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Link.from_dict(_v), "link_table")
        _value = data.get("stringTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "string_table")
        _value = data.get("attributeTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: KeyValueAndUnit.from_dict(_v), "attribute_table")
        _value = data.get("stackTable")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Stack.from_dict(_v), "stack_table")

        return cls(**_args)


@typing.final
@_dataclass
class ProfilesData(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ProfilesData
    """

    resource_profiles = dataclasses.field(default_factory=builtins.list)
    dictionary = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.resource_profiles:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.resource_profiles, lambda _v: _v.to_dict())
        if self.dictionary:
            _result = self.dictionary.to_dict()
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ProfilesData instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resourceProfiles")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ResourceProfiles.from_dict(_v), "resource_profiles")
        _value = data.get("dictionary")
        if _value is not None:
            _args = ProfilesDictionary.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class ResourceProfiles(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ResourceProfiles
    """

    resource = None
    scope_profiles = dataclasses.field(default_factory=builtins.list)
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
        if self.scope_profiles:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.scope_profiles, lambda _v: _v.to_dict())
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
            ResourceProfiles instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("resource")
        if _value is not None:
            _args = opentelemetry.proto_json.resource.v1.resource.Resource.from_dict(_value)
        _value = data.get("scopeProfiles")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: ScopeProfiles.from_dict(_v), "scope_profiles")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class ScopeProfiles(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ScopeProfiles
    """

    scope = None
    profiles = dataclasses.field(default_factory=builtins.list)
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
        if self.profiles:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.profiles, lambda _v: _v.to_dict())
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
            ScopeProfiles instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("scope")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.InstrumentationScope.from_dict(_value)
        _value = data.get("profiles")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Profile.from_dict(_v), "profiles")
        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Profile(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Profile
    """

    sample_type = None
    samples = dataclasses.field(default_factory=builtins.list)
    time_unix_nano = 0
    duration_nano = 0
    period_type = None
    period = 0
    profile_id = b""
    dropped_attributes_count = 0
    original_payload_format = ""
    original_payload = b""
    attribute_indices = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.sample_type:
            _result = self.sample_type.to_dict()
        if self.samples:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.samples, lambda _v: _v.to_dict())
        if self.time_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.time_unix_nano)
        if self.duration_nano:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.duration_nano)
        if self.period_type:
            _result = self.period_type.to_dict()
        if self.period:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.period)
        if self.profile_id:
            _result = opentelemetry.proto_json._json_codec.encode_base64(self.profile_id)
        if self.dropped_attributes_count:
            _result = self.dropped_attributes_count
        if self.original_payload_format:
            _result = self.original_payload_format
        if self.original_payload:
            _result = opentelemetry.proto_json._json_codec.encode_base64(self.original_payload)
        if self.attribute_indices:
            _result = self.attribute_indices
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Profile instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("sampleType")
        if _value is not None:
            _args = ValueType.from_dict(_value)
        _value = data.get("samples")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Sample.from_dict(_v), "samples")
        _value = data.get("timeUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "time_unix_nano")
        _value = data.get("durationNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "duration_nano")
        _value = data.get("periodType")
        if _value is not None:
            _args = ValueType.from_dict(_value)
        _value = data.get("period")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "period")
        _value = data.get("profileId")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_base64(_value, "profile_id")
        _value = data.get("droppedAttributesCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_attributes_count")
            _args = _value
        _value = data.get("originalPayloadFormat")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "original_payload_format")
            _args = _value
        _value = data.get("originalPayload")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_base64(_value, "original_payload")
        _value = data.get("attributeIndices")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "attribute_indices")

        return cls(**_args)


@typing.final
@_dataclass
class Link(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Link
    """

    trace_id = b""
    span_id = b""

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

        return cls(**_args)


@typing.final
@_dataclass
class ValueType(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ValueType
    """

    type_strindex = 0
    unit_strindex = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.type_strindex:
            _result = self.type_strindex
        if self.unit_strindex:
            _result = self.unit_strindex
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ValueType instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("typeStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "type_strindex")
            _args = _value
        _value = data.get("unitStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "unit_strindex")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class Sample(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Sample
    """

    stack_index = 0
    values = dataclasses.field(default_factory=builtins.list)
    attribute_indices = dataclasses.field(default_factory=builtins.list)
    link_index = 0
    timestamps_unix_nano = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.stack_index:
            _result = self.stack_index
        if self.values:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.values, lambda _v: opentelemetry.proto_json._json_codec.encode_int64(_v))
        if self.attribute_indices:
            _result = self.attribute_indices
        if self.link_index:
            _result = self.link_index
        if self.timestamps_unix_nano:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.timestamps_unix_nano, lambda _v: opentelemetry.proto_json._json_codec.encode_int64(_v))
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Sample instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("stackIndex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "stack_index")
            _args = _value
        _value = data.get("values")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json._json_codec.decode_int64(_v, "values"), "values")
        _value = data.get("attributeIndices")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "attribute_indices")
        _value = data.get("linkIndex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "link_index")
            _args = _value
        _value = data.get("timestampsUnixNano")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: opentelemetry.proto_json._json_codec.decode_int64(_v, "timestamps_unix_nano"), "timestamps_unix_nano")

        return cls(**_args)


@typing.final
@_dataclass
class Mapping(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Mapping
    """

    memory_start = 0
    memory_limit = 0
    file_offset = 0
    filename_strindex = 0
    attribute_indices = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.memory_start:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.memory_start)
        if self.memory_limit:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.memory_limit)
        if self.file_offset:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.file_offset)
        if self.filename_strindex:
            _result = self.filename_strindex
        if self.attribute_indices:
            _result = self.attribute_indices
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Mapping instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("memoryStart")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "memory_start")
        _value = data.get("memoryLimit")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "memory_limit")
        _value = data.get("fileOffset")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "file_offset")
        _value = data.get("filenameStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "filename_strindex")
            _args = _value
        _value = data.get("attributeIndices")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "attribute_indices")

        return cls(**_args)


@typing.final
@_dataclass
class Stack(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Stack
    """

    location_indices = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.location_indices:
            _result = self.location_indices
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Stack instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("locationIndices")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "location_indices")

        return cls(**_args)


@typing.final
@_dataclass
class Location(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Location
    """

    mapping_index = 0
    address = 0
    lines = dataclasses.field(default_factory=builtins.list)
    attribute_indices = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.mapping_index:
            _result = self.mapping_index
        if self.address:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.address)
        if self.lines:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.lines, lambda _v: _v.to_dict())
        if self.attribute_indices:
            _result = self.attribute_indices
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Location instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("mappingIndex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "mapping_index")
            _args = _value
        _value = data.get("address")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "address")
        _value = data.get("lines")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: Line.from_dict(_v), "lines")
        _value = data.get("attributeIndices")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "attribute_indices")

        return cls(**_args)


@typing.final
@_dataclass
class Line(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Line
    """

    function_index = 0
    line = 0
    column = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.function_index:
            _result = self.function_index
        if self.line:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.line)
        if self.column:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.column)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Line instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("functionIndex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "function_index")
            _args = _value
        _value = data.get("line")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "line")
        _value = data.get("column")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "column")

        return cls(**_args)


@typing.final
@_dataclass
class Function(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message Function
    """

    name_strindex = 0
    system_name_strindex = 0
    filename_strindex = 0
    start_line = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.name_strindex:
            _result = self.name_strindex
        if self.system_name_strindex:
            _result = self.system_name_strindex
        if self.filename_strindex:
            _result = self.filename_strindex
        if self.start_line:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.start_line)
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            Function instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("nameStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "name_strindex")
            _args = _value
        _value = data.get("systemNameStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "system_name_strindex")
            _args = _value
        _value = data.get("filenameStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "filename_strindex")
            _args = _value
        _value = data.get("startLine")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "start_line")

        return cls(**_args)


@typing.final
@_dataclass
class KeyValueAndUnit(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message KeyValueAndUnit
    """

    key_strindex = 0
    value = None
    unit_strindex = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.key_strindex:
            _result = self.key_strindex
        if self.value:
            _result = self.value.to_dict()
        if self.unit_strindex:
            _result = self.unit_strindex
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            KeyValueAndUnit instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("keyStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "key_strindex")
            _args = _value
        _value = data.get("value")
        if _value is not None:
            _args = opentelemetry.proto_json.common.v1.common.AnyValue.from_dict(_value)
        _value = data.get("unitStrindex")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "unit_strindex")
            _args = _value

        return cls(**_args)

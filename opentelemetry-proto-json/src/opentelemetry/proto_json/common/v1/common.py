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

# AUTO-GENERATED from "opentelemetry/proto/common/v1/common.proto"
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


@typing.final
@_dataclass
class AnyValue(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message AnyValue
    """

    string_value = None
    bool_value = None
    int_value = None
    double_value = None
    array_value = None
    kvlist_value = None
    bytes_value = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.bytes_value is not None:
            _result = opentelemetry.proto_json._json_codec.encode_base64(self.bytes_value)
        elif self.kvlist_value is not None:
            _result = self.kvlist_value.to_dict()
        elif self.array_value is not None:
            _result = self.array_value.to_dict()
        elif self.double_value is not None:
            _result = opentelemetry.proto_json._json_codec.encode_float(self.double_value)
        elif self.int_value is not None:
            _result = opentelemetry.proto_json._json_codec.encode_int64(self.int_value)
        elif self.bool_value is not None:
            _result = self.bool_value
        elif self.string_value is not None:
            _result = self.string_value
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            AnyValue instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("bytesValue")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_base64(_value, "bytes_value")
        _value = data.get("kvlistValue")
        if _value is not None:
            _args = KeyValueList.from_dict(_value)
        _value = data.get("arrayValue")
        if _value is not None:
            _args = ArrayValue.from_dict(_value)
        _value = data.get("doubleValue")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_float(_value, "double_value")
        _value = data.get("intValue")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_int64(_value, "int_value")
        _value = data.get("boolValue")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.bool, "bool_value")
            _args = _value
        _value = data.get("stringValue")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "string_value")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class ArrayValue(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message ArrayValue
    """

    values = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.values:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.values, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            ArrayValue instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("values")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: AnyValue.from_dict(_v), "values")

        return cls(**_args)


@typing.final
@_dataclass
class KeyValueList(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message KeyValueList
    """

    values = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.values:
            _result = opentelemetry.proto_json._json_codec.encode_repeated(self.values, lambda _v: _v.to_dict())
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            KeyValueList instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("values")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: KeyValue.from_dict(_v), "values")

        return cls(**_args)


@typing.final
@_dataclass
class KeyValue(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message KeyValue
    """

    key = ""
    value = None

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.key:
            _result = self.key
        if self.value:
            _result = self.value.to_dict()
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            KeyValue instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("key")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "key")
            _args = _value
        _value = data.get("value")
        if _value is not None:
            _args = AnyValue.from_dict(_value)

        return cls(**_args)


@typing.final
@_dataclass
class InstrumentationScope(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message InstrumentationScope
    """

    name = ""
    version = ""
    attributes = dataclasses.field(default_factory=builtins.list)
    dropped_attributes_count = 0

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.name:
            _result = self.name
        if self.version:
            _result = self.version
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
            InstrumentationScope instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("name")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "name")
            _args = _value
        _value = data.get("version")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "version")
            _args = _value
        _value = data.get("attributes")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: KeyValue.from_dict(_v), "attributes")
        _value = data.get("droppedAttributesCount")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.int, "dropped_attributes_count")
            _args = _value

        return cls(**_args)


@typing.final
@_dataclass
class EntityRef(opentelemetry.proto_json._json_codec.JsonMessage):
    """
    Generated from protobuf message EntityRef
    """

    schema_url = ""
    type = ""
    id_keys = dataclasses.field(default_factory=builtins.list)
    description_keys = dataclasses.field(default_factory=builtins.list)

    def to_dict(self):
        """
        Convert this message to a dictionary with lowerCamelCase keys.

        Returns:
            Dictionary representation following OTLP JSON encoding
        """
        _result = {}
        if self.schema_url:
            _result = self.schema_url
        if self.type:
            _result = self.type
        if self.id_keys:
            _result = self.id_keys
        if self.description_keys:
            _result = self.description_keys
        return _result

    @builtins.classmethod
    def from_dict(cls, data):
        """
        Create from a dictionary with lowerCamelCase keys.

        Args:
            data: Dictionary representation following OTLP JSON encoding

        Returns:
            EntityRef instance
        """
        opentelemetry.proto_json._json_codec.validate_type(data, builtins.dict, "data")
        _args = {}

        _value = data.get("schemaUrl")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "schema_url")
            _args = _value
        _value = data.get("type")
        if _value is not None:
            opentelemetry.proto_json._json_codec.validate_type(_value, builtins.str, "type")
            _args = _value
        _value = data.get("idKeys")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "id_keys")
        _value = data.get("descriptionKeys")
        if _value is not None:
            _args = opentelemetry.proto_json._json_codec.decode_repeated(_value, lambda _v: _v, "description_keys")

        return cls(**_args)

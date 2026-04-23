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

import abc
import base64
import json
import math
import typing

T = typing.TypeVar("T")
M = typing.TypeVar("M", bound="JsonMessage")


class JsonMessage(abc.ABC):
    """
    Abstract base class for protobuf messages with JSON serialization.
    """

    @abc.abstractmethod
    def to_dict(self):
        """
        Convert this message to a dictionary.
        """

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, data):
        """
        Create an instance from a dictionary.
        """

    def to_json(self):
        """
        Serialize this message to a JSON string.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data):
        """
        Deserialize from a JSON string or bytes.
        """
        return cls.from_dict(json.loads(data))


def encode_hex(value):
    """
    Encode bytes as hex string.

    Args:
        value: The bytes to encode.
    Returns:
        Hex string representation of the input bytes.
    """
    return value.hex() if value else ""


def encode_base64(value):
    """
    Encode bytes as base64 string.
    Standard Proto3 JSON mapping for bytes.

    Args:
        value: The bytes to encode.
    Returns:
        Base64 string representation of the input bytes.
    """
    return base64.b64encode(value).decode("utf-8") if value else ""


def encode_int64(value):
    """
    Encode 64 bit integers as strings.
    Required for int64, uint64, fixed64, sfixed64 and sint64 per Proto3 JSON spec.

    Args:
        value: The integer to encode.
    Returns:
        String representation of the input integer.
    """
    return str(value)


def encode_float(value):
    """
    Encode float/double values.

    Args:
        value: The float to encode.
    Returns:
        The input value, or a string for special float values (NaN, Infinity).
    """
    if math.isnan(value):
        return "NaN"
    if math.isinf(value):
        return "Infinity" if value > 0 else "-Infinity"
    return value


def encode_repeated(
    values,
    map_fn
):
    """
    Helper to serialize repeated fields with a mapping function.

    Args:
        values: The list of values to encode.
        map_fn: A function that takes a single value and returns its encoded form.
    Returns:
        A list of encoded values, or an empty list if input is None or empty.
    """
    return [map_fn(v) for v in values] if values else []


def decode_hex(value, field_name):
    """
    Decode hex string to bytes.

    Args:
        value: The hex string to decode.
        field_name: The name of the field being decoded (for error messages).
    Returns:
        The decoded bytes, or empty bytes if input is None or empty.
    """
    if not value:
        return b""
    validate_type(value, str, field_name)
    try:
        return bytes.fromhex(value)
    except ValueError as error:
        raise ValueError(
            "Invalid hex string for field '{}': {}".format(field_name, error)
        )


def decode_base64(value, field_name):
    """
    Decode base64 string to bytes.

    Args:
        value: The base64 string to decode.
        field_name: The name of the field being decoded (for error messages).
    Returns:
        The decoded bytes, or empty bytes if input is None or empty.
    """
    if not value:
        return b""
    validate_type(value, str, field_name)
    try:
        return base64.b64decode(value)
    except Exception as error:
        raise ValueError(
            "Invalid base64 string for field '{}': {}".format(field_name, error)
        )


def decode_int64(
    value, field_name
):
    """
    Parse int64 from number or string.

    Args:
        value: The value to decode, which can be an int, a string, or None
        field_name: The name of the field being decoded (for error messages).
    Returns:
        The decoded integer, or 0 if input is None.
    """
    if value is None:
        return 0
    validate_type(value, (int, str), field_name)
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(
            "Invalid int64 value for field '{}': {}".format(field_name, value)
        )


def decode_float(
    value, field_name
):
    """
    Parse float/double from number or string, handling special values.

    Args:
        value: The value to decode, which can be a float, int, string, or None
        field_name: The name of the field being decoded (for error messages).
    Returns:
        The decoded float, or 0.0 if input is None.
    """
    if value is None:
        return 0.0
    validate_type(value, (float, int, str), field_name)
    if value == "NaN":
        return math.nan
    if value == "Infinity":
        return math.inf
    if value == "-Infinity":
        return -math.inf
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(
            "Invalid float value for field '{}': {}".format(field_name, value)
        )


def decode_repeated(
    values,
    item_parser,
    field_name
):
    """
    Parse a list of values using the provided item parser function.

    Args:
        values: The list of values to decode, or None.
        item_parser: A function that takes a single value and returns the parsed form.
        field_name: The name of the field being decoded (for error messages).
    Returns:
        A list of parsed values, or an empty list if input is None.
    """
    if values is None:
        return []
    validate_type(values, list, field_name)
    return [item_parser(v) for v in values]


def validate_type(
    value,
    expected_types,
    field_name
):
    """
    Validate that a value is of the expected type(s).
    Raises TypeError if validation fails.

    Args:
        value: The value to validate.
        expected_types: A type or tuple of types that the value is expected to be.
        field_name: The name of the field being validated (for error messages).
    """
    if not isinstance(value, expected_types):
        raise TypeError(
            "Field '{}' expected {}, ".format(field_name, expected_types) +
            "got {}".format(type(value).__name__)
        )

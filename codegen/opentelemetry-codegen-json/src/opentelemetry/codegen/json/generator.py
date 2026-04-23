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

# pylint =no-member,invalid-name,too-many-lines

import logging
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path
from typing import Callable, Final, Optional, Set

from google.protobuf import descriptor_pb2 as descriptor
from google.protobuf.compiler import plugin_pb2 as plugin

from opentelemetry.codegen.json.types import (
    get_default_value,
    get_json_allowed_types,
    get_python_type,
    is_bytes_type,
    is_hex_encoded_field,
    is_int64_type,
    to_json_field_name,
)
from opentelemetry.codegen.json.version import __version__ as GENERATOR_VERSION
from opentelemetry.codegen.json.writer import CodeWriter

_logger = logging.getLogger(__name__)

CODEC_MODULE_NAME = "_json_codec"


class OtlpJsonGenerator:
    """
    Generates Python dataclasses and JSON serialization/deserialization code
    from protobuf descriptors.
    """

    def __init__(
        self,
        request,
        package_transform,
        version
    ):
        """
        Initialize the generator.

        Args:
            request: Protobuf compiler plugin request
            package_transform: A callable that transforms the proto file path.
            version: Version string for the generated code.
        """
        self._request = request
        self._package_transform = package_transform
        self._version = version
        self._generated_files = {}
        self._common_root = ""
        self._file_to_proto = {
            f.name: f for f in request.proto_file
        }
        self._fqn_to_file = {}
        self._fqn_to_class_path = {}
        self._file_dependencies = {
            f.name: list(f.dependency) for f in request.proto_file
        }

        for proto_file in request.proto_file:
            self._index_file(proto_file)

    def generate_all(self):
        """
        Generate Python code for all proto files and support modules.

        Returns:
            Dictionary mapping output file paths to generated code
        """
        files_to_generate = self._request.file_to_generate
        file_to_output = {
            proto_file: self._transform_proto_path(proto_file)
            for proto_file in files_to_generate
        }

        if not file_to_output:
            return {}

        self._common_root = _find_common_root(file_to_output.values())

        for proto_file in files_to_generate:
            file_desc = self._file_to_proto
            code = self._generate_file(file_desc)
            output_path = file_to_output
            self._generated_files = code

        codec_path = "{}/{}.py".format(self._common_root, CODEC_MODULE_NAME)
        self._generated_files = _load_codec_source()

        version_init_path = "{}/version/__init__.py".format(self._common_root)
        version_writer = CodeWriter(indent_size=4)
        self._generate_header(version_writer)
        version_writer.writemany('__version__ = "{}"'.format(self._version), "")
        self._generated_files = version_writer.to_string()

        self._ensure_init_files()

        return self._generated_files

    def _index_file(self, file_desc):
        """
        Index all messages and enums in the file for usage during generation.

        Args:
            file_desc: File descriptor to index
        """
        package = file_desc.package
        for enum_desc in file_desc.enum_type:
            fqn = "{}.{}".format(package, enum_desc.name) if package else enum_desc.name
            self._fqn_to_file = file_desc.name
            self._fqn_to_class_path = enum_desc.name
        for msg_desc in file_desc.message_type:
            self._index_message(msg_desc, package, file_desc.name, None)

    def _index_message(
        self,
        msg_desc,
        package,
        file_name,
        parent_path
    ):
        """
        Recursively index a message and its nested types.

        Args:
            msg_desc: Message descriptor to index
            package: Protobuf package name for the message
            file_name: Proto file where the message is defined
            parent_path: Full parent class path for nested messages
        """
        current_path = (
            "{}.{}".format(parent_path, msg_desc.name) if parent_path else msg_desc.name
        )
        fqn = "{}.{}".format(package, current_path) if package else current_path
        self._fqn_to_file = file_name
        self._fqn_to_class_path = current_path

        for enum_desc in msg_desc.enum_type:
            enum_fqn = "{}.{}".format(fqn, enum_desc.name)
            self._fqn_to_file = file_name
            self._fqn_to_class_path = (
                "{}.{}".format(current_path, enum_desc.name)
            )

        for nested_msg in msg_desc.nested_type:
            if not nested_msg.options.map_entry:
                self._index_message(
                    nested_msg, package, file_name, current_path
                )

    def _ensure_init_files(self):
        """
        Ensure that every directory in the output path contains an __init__.py file.
        """
        dirs = set()
        for path in self._generated_files:
            p = Path(path)
            for parent in p.parents:
                parent_str = str(parent)
                # Skip '.', root, and the 'opentelemetry' namespace directory
                if parent_str in (".", "/", "opentelemetry"):
                    continue
                dirs.add(parent_str)

        for d in dirs:
            init_path = "{}/__init__.py".format(d)
            if init_path not in self._generated_files:
                self._generated_files = ""

    def _get_codec_module_path(self):
        """
        Get the absolute module path for the codec module.

        Returns:
            Absolute module path as a string
        """
        return (
            "{}.{}".format(self._common_root.replace('/', '.'), CODEC_MODULE_NAME)
            if self._common_root
            else CODEC_MODULE_NAME
        )

    def _transform_proto_path(self, proto_path):
        """
        Transform proto file path to output Python file path.

        Example: 'opentelemetry/proto/trace/v1/trace.proto'
              -> 'opentelemetry/proto_json/trace/v1/trace.py'

        Args:
            proto_path: Original .proto file path

        Returns:
            Transformed .py file path
        """
        transformed = self._package_transform(proto_path)
        if transformed.endswith(".proto"):
            transformed = transformed + ".py"
        return transformed

    def _get_module_path(self, proto_file):
        """
        Convert a proto file path to its transformed Python module path.

        Example: 'opentelemetry/proto/common/v1/common.proto'
              -> 'opentelemetry.proto_json.common.v1.common'

        Args:
            proto_file: Original .proto file path

        Returns:
            Python module path (dot-separated)
        """
        transformed = self._transform_proto_path(proto_file)
        if transformed.endswith(".py"):
            transformed = transformed
        return transformed.replace("/", ".")

    def _generate_file(self, file_desc):
        """
        Generate complete Python file for a proto file.

        Args:
            file_desc: File descriptor

        Returns:
            Generated Python code as string
        """
        writer = CodeWriter(indent_size=4)
        proto_file = file_desc.name

        self._generate_header(writer, proto_file)
        self._generate_imports(
            writer, proto_file, self._file_has_enums(file_desc)
        )
        self._generate_enums_for_file(writer, file_desc.enum_type)
        self._generate_messages_for_file(
            writer, proto_file, file_desc.message_type
        )
        writer.blank_line()

        return writer.to_string()

    def _file_has_enums(
        self, file_desc
    ):
        """
        Check if the file or any of its messages (recursively) contain enums.

        Args:
            file_desc: File descriptor to check
        Returns:
            True if any enums are found, False otherwise
        """
        if file_desc.enum_type:
            return True
        for msg in file_desc.message_type:
            if self._msg_has_enums(msg):
                return True
        return False

    def _msg_has_enums(self, msg_desc):
        """
        Recursively check if the message or any of its nested messages contain enums.

        Args:
            msg_desc: Message descriptor to check
        Returns:
            True if any enums are found, False otherwise
        """
        if msg_desc.enum_type:
            return True
        for nested in msg_desc.nested_type:
            if self._msg_has_enums(nested):
                return True
        return False

    @classmethod
    def _generate_header(
        cls, writer, proto_file = ""
    ):
        """
        Generate file header with license and metadata.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path (optional)
        """
        writer.comment(
            [
                "Copyright The OpenTelemetry Authors",
                "",
                'Licensed under the Apache License, Version 2.0 (the "License");',
                "you may not use this file except in compliance with the License.",
                "You may obtain a copy of the License at",
                "",
                "    http://www.apache.org/licenses/LICENSE-2.0",
                "",
                "Unless required by applicable law or agreed to in writing, software",
                'distributed under the License is distributed on an "AS IS" BASIS,',
                "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.",
                "See the License for the specific language governing permissions and",
                "limitations under the License.",
            ]
        )
        writer.blank_line()
        if proto_file:
            writer.comment('AUTO-GENERATED from "{}"'.format(proto_file))
            writer.comment("DO NOT EDIT MANUALLY")
            writer.blank_line()

    def _generate_imports(
        self,
        writer,
        proto_file,
        include_enum
    ):
        """
        Generate all necessary import statements.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            include_enum: Whether to include the enum module import
        """
        writer.import_("__future__", "annotations")
        writer.blank_line()

        std_imports = [
            "builtins",
            "dataclasses",
            "functools",
            "sys",
            "typing",
        ]
        if include_enum:
            std_imports.append("enum")

        for module in sorted(std_imports):
            writer.import_(module)

        writer.blank_line()

        # TODO: Remove after dropping support for Python 3.9
        with writer.if_("sys.version_info >= (3, 10)"):
            writer.assignment(
                "_dataclass",
                "functools.partial(dataclasses.dataclass, slots=True)",
            )
        with writer.else_():
            writer.assignment("_dataclass", "dataclasses.dataclass")
        writer.blank_line()

        # Collect all imports needed
        imports = self._collect_imports(proto_file)
        imports.add("import {}".format(self._get_codec_module_path()))

        # Generate cross file imports
        if imports:
            for import_info in sorted(imports):
                writer.writeln(import_info)
            writer.blank_line()
        writer.blank_line()

    def _collect_imports(self, proto_file):
        """
        Collect all import statements needed for cross file references.

        Args:
            proto_file: Current proto file path

        Returns:
            Set of import statement strings
        """
        return set(
            "import " + self._get_module_path(dep_file)
            for dep_file in self._file_dependencies.get(proto_file, [])
        )

    def _generate_enums_for_file(
        self,
        writer,
        enum_descs
    ):
        """
        Generate all enums for a file (top level and nested).

        Args:
            writer: Code writer instance
            enum_descs: List of top level enums
        """
        for enum_desc in enum_descs:
            self._generate_enum_class(writer, enum_desc)
            writer.blank_line()

    def _generate_messages_for_file(
        self,
        writer,
        proto_file,
        msg_descs
    ):
        """
        Generate all message classes for a file.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            msg_descs: List of top level messages
        """
        for i, message in enumerate(msg_descs):
            if i:
                writer.blank_line(2)

            self._generate_message_class(writer, proto_file, message)

    def _generate_message_class(
        self,
        writer,
        proto_file,
        msg_desc,
        parent_path = None
    ):
        """
        Generate a complete dataclass for a protobuf message.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            msg_desc: Message descriptor
            parent_path: Full parent class path for nested messages
        """
        current_path = (
            "{}.{}".format(parent_path, msg_desc.name) if parent_path else msg_desc.name
        )
        codec = self._get_codec_module_path()
        with writer.dataclass(
            msg_desc.name,
            bases=("{}.JsonMessage".format(codec),),
            decorators=("typing.final",),
            decorator_name="_dataclass",
        ):
            if msg_desc.field or msg_desc.nested_type or msg_desc.enum_type:
                writer.docstring(
                    ["Generated from protobuf message {}".format(msg_desc.name)]
                )
                writer.blank_line()

            for enum_desc in msg_desc.enum_type:
                self._generate_enum_class(writer, enum_desc)
                writer.blank_line()

            for nested_desc in msg_desc.nested_type:
                if not nested_desc.options.map_entry:
                    self._generate_message_class(
                        writer, proto_file, nested_desc, current_path
                    )
                    writer.blank_line()

            if msg_desc.field:
                for field_desc in msg_desc.field:
                    self._generate_field(writer, proto_file, field_desc)
            else:
                writer.pass_()

            writer.blank_line()
            self._generate_to_dict(writer, msg_desc)
            writer.blank_line()
            self._generate_from_dict(
                writer, proto_file, msg_desc, current_path
            )

    @classmethod
    def _generate_enum_class(
        cls, writer, enum_desc
    ):
        """
        Generate an IntEnum class for a protobuf enum.

        Args:
            writer: Code writer instance
            enum_desc: Enum descriptor
        """
        with writer.enum(
            enum_desc.name,
            enum_type="enum.IntEnum",
            decorators=("typing.final",),
        ):
            writer.docstring(
                ["Generated from protobuf enum {}".format(enum_desc.name)]
            )
            writer.blank_line()

            if enum_desc.value:
                for val_desc in enum_desc.value:
                    writer.enum_member(val_desc.name, val_desc.number)
            else:
                writer.pass_()

    def _generate_field(
        self,
        writer,
        proto_file,
        field_desc
    ):
        """
        Generate a dataclass field.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            field_desc: Field descriptor
        """
        type_hint = self._get_field_type_hint(proto_file, field_desc)
        writer.field(
            field_desc.name,
            type_hint,
            default=self._get_field_default(field_desc),
        )

    def _generate_to_dict(
        self,
        writer,
        msg_desc
    ):
        """
        Generate a to_dict() method that converts the dataclass instance to a dictionary

        Args:
            writer: Code writer instance
            msg_desc: Message descriptor for the class being generated
        """
        with writer.method(
            "to_dict",
            ["self"],
            return_type="builtins.dict",
        ):
            writer.docstring(
                [
                    "Convert this message to a dictionary with lowerCamelCase keys.",
                    "",
                    "Returns:",
                    "    Dictionary representation following OTLP JSON encoding",
                ]
            )
            writer.assignment("_result", "{}")

            # Separate fields into oneof groups and standalone fields
            oneof_groups = (
                defaultdict(list)
            )
            standalone_fields = []

            for field in msg_desc.field:
                if field.HasField("oneof_index") and not field.proto3_optional:
                    oneof_groups.append(field)
                else:
                    standalone_fields.append(field)

            for field in standalone_fields:
                with writer.if_(
                    "self.{} is not None".format(field.name)
                    if field.proto3_optional
                    else "self.{}".format(field.name)
                ):
                    self._generate_serialization_statements(
                        writer, field, "_result"
                    )

            for group_index in sorted(oneof_groups.keys()):
                group_fields = oneof_groups
                for i, field in enumerate(reversed(group_fields)):
                    condition = "self.{} is not None".format(field.name)
                    context = (
                        writer.elif_(condition) if i else writer.if_(condition)
                    )

                    with context:
                        self._generate_serialization_statements(
                            writer, field, "_result"
                        )

            writer.return_("_result")

    def _generate_from_dict(
        self,
        writer,
        proto_file,
        msg_desc,
        current_path
    ):
        """
        Generate a from_dict() class method that creates an instance from a dictionary.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            msg_desc: Message descriptor for the class being generated
            current_path: Full class path for type hints and return type
        """
        with writer.method(
            "from_dict",
            ["cls", "data: builtins.dict"],
            decorators=["builtins.classmethod"],
            return_type='"{}"'.format(current_path),
        ):
            writer.docstring(
                [
                    "Create from a dictionary with lowerCamelCase keys.",
                    "",
                    "Args:",
                    "    data: Dictionary representation following OTLP JSON encoding",
                    "",
                    "Returns:",
                    "    {} instance".format(msg_desc.name),
                ]
            )
            codec = self._get_codec_module_path()
            writer.writeln(
                '{}.validate_type(data, builtins.dict, "data")'.format(codec)
            )
            writer.assignment("_args", "{}")
            writer.blank_line()

            # Separate fields into oneof groups and standalone fields
            oneof_groups = (
                defaultdict(list)
            )
            standalone_fields = []

            for field in msg_desc.field:
                if field.HasField("oneof_index") and not field.proto3_optional:
                    oneof_groups.append(field)
                else:
                    standalone_fields.append(field)

            # Handle standalone fields
            for field in standalone_fields:
                json_name = (
                    field.json_name
                    if field.json_name
                    else to_json_field_name(field.name)
                )
                with writer.if_(
                    '(_value := data.get("{}")) is not None'.format(json_name)
                ):
                    self._generate_deserialization_statements(
                        writer, proto_file, field, "_value", "_args"
                    )

            # Handle oneof groups
            for group_index in sorted(oneof_groups.keys()):
                group_fields = oneof_groups
                for i, field in enumerate(reversed(group_fields)):
                    json_name = (
                        field.json_name
                        if field.json_name
                        else to_json_field_name(field.name)
                    )
                    condition = (
                        '(_value := data.get("{}")) is not None'.format(json_name)
                    )
                    context = (
                        writer.elif_(condition) if i else writer.if_(condition)
                    )

                    with context:
                        self._generate_deserialization_statements(
                            writer, proto_file, field, "_value", "_args"
                        )

            writer.blank_line()
            writer.return_("cls(**_args)")

    def _generate_serialization_statements(
        self,
        writer,
        field_desc,
        target_dict
    ):
        """
        Generate statements to serialize a field and assign it to the target dictionary.

        Args:
            writer: Code writer instance
            field_desc: Field descriptor for the field being serialized
            target_dict: Name of the dictionary variable to assign the serialized value to
        """
        json_name = (
            field_desc.json_name
            if field_desc.json_name
            else to_json_field_name(field_desc.name)
        )
        if field_desc.label == descriptor.FieldDescriptorProto.LABEL_REPEATED:
            item_expr = self._get_serialization_expr(field_desc, "_v")
            if item_expr == "_v":
                writer.assignment(
                    '{}["{}"]'.format(target_dict, json_name), "self.{}".format(field_desc.name)
                )
            else:
                codec = self._get_codec_module_path()
                writer.assignment(
                    '{}["{}"]'.format(target_dict, json_name),
                    "{}.encode_repeated(self.{}, lambda _v: {})".format(codec, field_desc.name, item_expr),
                )
        else:
            val_expr = self._get_serialization_expr(
                field_desc, "self.{}".format(field_desc.name)
            )
            writer.assignment('{}["{}"]'.format(target_dict, json_name), val_expr)

    # pylint: disable-next=too-many-return-statements
    def _get_serialization_expr(
        self, field_desc, var_name
    ):
        """
        Get the Python expression to serialize a value of a given type for JSON output.

        Args:
            field_desc: Field descriptor for the value being serialized
            var_name: Variable name representing the value to serialize
        """
        codec = self._get_codec_module_path()
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_MESSAGE:
            return "{}.to_dict()".format(var_name)
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            return "builtins.int({})".format(var_name)
        if is_hex_encoded_field(field_desc.name):
            return "{}.encode_hex({})".format(codec, var_name)
        if is_int64_type(field_desc.type):
            return "{}.encode_int64({})".format(codec, var_name)
        if is_bytes_type(field_desc.type):
            return "{}.encode_base64({})".format(codec, var_name)
        if field_desc.type in (
            descriptor.FieldDescriptorProto.TYPE_FLOAT,
            descriptor.FieldDescriptorProto.TYPE_DOUBLE,
        ):
            return "{}.encode_float({})".format(codec, var_name)

        return var_name

    def _generate_deserialization_statements(
        self,
        writer,
        proto_file,
        field_desc,
        var_name,
        target_dict
    ):
        """
        Generate statements to deserialize a field from a JSON value and assign it to the target dictionary.

        Args:
            writer: Code writer instance
            proto_file: Original proto file path
            field_desc: Field descriptor for the field being deserialized
            var_name: Variable name representing the JSON value to deserialize
            target_dict: Name of the dictionary variable to assign the deserialized value to
        """
        codec = self._get_codec_module_path()
        if field_desc.label == descriptor.FieldDescriptorProto.LABEL_REPEATED:
            item_expr = self._get_deserialization_expr(
                proto_file, field_desc, "_v"
            )
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                '{}.decode_repeated({}, lambda _v: {}, "{}")'.format(codec, var_name, item_expr, field_desc.name),
            )
            return

        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_MESSAGE:
            msg_type = self._resolve_message_type(
                field_desc.type_name, proto_file
            )
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                "{}.from_dict({})".format(msg_type, var_name),
            )
        elif field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            enum_type = self._resolve_enum_type(
                field_desc.type_name, proto_file
            )
            writer.writeln(
                '{}.validate_type({}, builtins.int, "{}")'.format(codec, var_name, field_desc.name)
            )
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                "{}({})".format(enum_type, var_name),
            )
        elif is_hex_encoded_field(field_desc.name):
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                '{}.decode_hex({}, "{}")'.format(codec, var_name, field_desc.name),
            )
        elif is_int64_type(field_desc.type):
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                '{}.decode_int64({}, "{}")'.format(codec, var_name, field_desc.name),
            )
        elif is_bytes_type(field_desc.type):
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                '{}.decode_base64({}, "{}")'.format(codec, var_name, field_desc.name),
            )
        elif field_desc.type in (
            descriptor.FieldDescriptorProto.TYPE_FLOAT,
            descriptor.FieldDescriptorProto.TYPE_DOUBLE,
        ):
            writer.assignment(
                '{}["{}"]'.format(target_dict, field_desc.name),
                '{}.decode_float({}, "{}")'.format(codec, var_name, field_desc.name),
            )
        else:
            allowed_types = get_json_allowed_types(
                field_desc.type, field_desc.name
            )
            writer.writeln(
                '{}.validate_type({}, {}, "{}")'.format(codec, var_name, allowed_types, field_desc.name)
            )
            writer.assignment('{}["{}"]'.format(target_dict, field_desc.name), var_name)

    # pylint: disable-next=too-many-return-statements
    def _get_deserialization_expr(
        self,
        proto_file,
        field_desc,
        var_name
    ):
        """
        Get the Python expression to deserialize a value of a given type for JSON input.

        Args:
            proto_file: Original proto file path
            field_desc: Field descriptor for the value being deserialized
            var_name: Variable name representing the JSON value to deserialize

        Returns:
            Python expression string to perform deserialization
        """
        codec = self._get_codec_module_path()
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_MESSAGE:
            msg_type = self._resolve_message_type(
                field_desc.type_name, proto_file
            )
            return "{}.from_dict({})".format(msg_type, var_name)
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            enum_type = self._resolve_enum_type(
                field_desc.type_name, proto_file
            )
            return "{}({})".format(enum_type, var_name)
        if is_hex_encoded_field(field_desc.name):
            return '{}.decode_hex({}, "{}")'.format(codec, var_name, field_desc.name)
        if is_int64_type(field_desc.type):
            return '{}.decode_int64({}, "{}")'.format(codec, var_name, field_desc.name)
        if is_bytes_type(field_desc.type):
            return '{}.decode_base64({}, "{}")'.format(codec, var_name, field_desc.name)
        if field_desc.type in (
            descriptor.FieldDescriptorProto.TYPE_FLOAT,
            descriptor.FieldDescriptorProto.TYPE_DOUBLE,
        ):
            return '{}.decode_float({}, "{}")'.format(codec, var_name, field_desc.name)

        return var_name

    def _get_field_type_hint(
        self, proto_file, field_desc
    ):
        """
        Get the Python type hint for a field.

        Args:
            proto_file: Original proto file path
            field_desc: Field descriptor

        Returns:
            Python type hint string
        """
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_MESSAGE:
            base_type = self._resolve_message_type(
                field_desc.type_name, proto_file
            )
        elif field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            base_type = self._resolve_enum_type(
                field_desc.type_name, proto_file
            )
        else:
            base_type = get_python_type(field_desc.type)

        if field_desc.label == descriptor.FieldDescriptorProto.LABEL_REPEATED:
            return "builtins.list".format(base_type)
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            return "typing.Union".format(base_type)
        return "typing.Optional".format(base_type)

    def _resolve_message_type(self, type_name, proto_file):
        """
        Resolve a message type name to its Python class path.

        Args:
            type_name: Fully qualified proto name
            proto_file: Current proto file path

        Returns:
            Python class reference
        """
        fqn = type_name.lstrip(".")
        target_file = self._fqn_to_file.get(fqn)

        if not target_file:
            _logger.warning("Could not resolve message type: %s", type_name)
            return "typing.Any"

        class_path = self._fqn_to_class_path

        # If in same file, use relative class path
        if target_file == proto_file:
            return class_path
        # Cross file reference - use fully qualified module + class path
        module_path = self._get_module_path(target_file)
        return "{}.{}".format(module_path, class_path)

    def _resolve_enum_type(self, type_name, proto_file):
        """
        Resolve an enum type name to its Python class path.

        Args:
            type_name: Fully qualified proto name
            proto_file: Current proto file path

        Returns:
            Python class reference
        """
        fqn = type_name.lstrip(".")
        target_file = self._fqn_to_file.get(fqn)

        if not target_file:
            _logger.warning("Could not resolve enum type: %s", type_name)
            return "builtins.int"

        class_path = self._fqn_to_class_path

        # If in same file, use relative class path
        if target_file == proto_file:
            return class_path
        # Cross file reference - use fully qualified module + class path
        module_path = self._get_module_path(target_file)
        return "{}.{}".format(module_path, class_path)

    @classmethod
    def _get_field_default(
        cls, field_desc
    ):
        """
        Get the default value for a field.

        Args:
            field_desc: Field descriptor

        Returns:
            Default value string or None
        """
        # Repeated fields default to empty list
        if field_desc.label == descriptor.FieldDescriptorProto.LABEL_REPEATED:
            return "dataclasses.field(default_factory=builtins.list)"

        # Optional fields, Message types, and oneof members default to None
        if (
            field_desc.type == descriptor.FieldDescriptorProto.TYPE_MESSAGE
            or field_desc.HasField("oneof_index")
            or field_desc.proto3_optional
        ):
            return "None"

        # Enum types default to 0
        if field_desc.type == descriptor.FieldDescriptorProto.TYPE_ENUM:
            return "0"

        # Primitive types use proto defaults
        return get_default_value(field_desc.type)


def _load_codec_source():
    """
    Load the source code for the codec module from its source file.

    Returns:
        Source code as a string
    """
    codec_src_path = Path(__file__).parent / "runtime" / "json_codec.py"
    try:
        return codec_src_path.read_text(encoding="utf-8")
    except Exception as e:
        _logger.error(
            "Failed to load codec module source from %s: %s",
            codec_src_path,
            e,
        )
        raise RuntimeError(
            "Failed to load codec module source from {}".format(codec_src_path)
        )
def _find_common_root(paths):
    """
    Find the longest common directory prefix among the given paths.

    Args:
        paths: Iterable of file paths to analyze
    Returns:
        Common directory prefix as a string
    """
    if not paths:
        return ""

    # Split paths into components
    split_paths = [p.split("/")[:-1] for p in paths]
    if not split_paths:
        return ""

    # Find common prefix among components
    common = []
    for parts in zip(*split_paths):
        if all(p == parts for p in parts):
            common.append(parts)
        else:
            break

    return "/".join(common)


def generate_code(
    request,
    package_transform = lambda p: p.replace(
        "opentelemetry/proto/", "opentelemetry/proto_json/"
    ),
):
    """
    Main entry point for code generation.

    Args:
        request: Protobuf compiler plugin request
        package_transform: Package transformation string or callable

    Returns:
        Dictionary mapping output file paths to generated code
    """
    generator = OtlpJsonGenerator(
        request, package_transform, version=GENERATOR_VERSION
    )
    return generator.generate_all()


def generate_plugin_response(
    request,
    package_transform = lambda p: p.replace(
        "opentelemetry/proto/", "opentelemetry/proto_json/"
    ),
):
    """
    Generate plugin response with all generated files.

    Args:
        request: Protobuf compiler plugin request
        package_transform: Package transformation string

    Returns:
        Plugin response with generated files
    """
    response = plugin.CodeGeneratorResponse()

    # Declare support for optional proto3 fields
    response.supported_features |= (
        plugin.CodeGeneratorResponse.FEATURE_PROTO3_OPTIONAL
    )
    response.supported_features |= (
        plugin.CodeGeneratorResponse.FEATURE_SUPPORTS_EDITIONS
    )

    response.minimum_edition = descriptor.EDITION_LEGACY
    response.maximum_edition = descriptor.EDITION_2024

    # Generate code
    generated_files = generate_code(request, package_transform)

    # Create response files
    for output_path, code in generated_files.items():
        file_response = response.file.add()
        file_response.name = output_path
        file_response.content = code

    return response

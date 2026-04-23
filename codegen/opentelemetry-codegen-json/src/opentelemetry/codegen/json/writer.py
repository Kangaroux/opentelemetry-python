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

from collections.abc import Iterable
from contextlib import contextmanager
from typing import Any, Generator, Optional, Union


# pylint: disable-next=too-many-public-methods
class CodeWriter:
    def __init__(self, indent_size = 4):
        """
        Initializes a new CodeWriter instance.

        Args:
            indent_size: Number of spaces for each indentation level (default: 4)
        """
        self._lines = []
        self._indent_level = 0
        self._indent_size = indent_size

    @contextmanager
    def indent(self):
        """
        Context manager to increase indentation level for a block of code.
        """
        self._indent_level += 1
        try:
            yield self
        finally:
            self._indent_level -= 1

    def writeln(self, line = ""):
        """
        Writes a line of code with proper indentation. If the line is empty, it writes a blank line.

        Args:
            line: The line of code to write (default: empty string for a blank line)
        Returns:
            The CodeWriter instance
        """
        if not line:
            self._lines.append("")
            return self
        indent = " " * (self._indent_level * self._indent_size)
        self._lines.append("{}{}".format(indent, line))
        return self

    def writemany(self, *lines):
        """
        Writes multiple lines of code with proper indentation.

        Args:
            *lines: Variable number of lines to write
        Returns:
            The CodeWriter instance
        """
        for line in lines:
            self.writeln(line)
        return self

    def comment(self, content):
        """
        Writes a comment line or block. If content is a string, it writes a single comment line.

        Args:
            content: A string for a single comment line or an iterable of strings for multiple comment lines
        Returns:
            The CodeWriter instance
        """
        if isinstance(content, str):
            self.writeln("# {}".format(content) if content else "#")
            return self
        for line in content:
            self.writeln("# {}".format(line) if line else "#")
        return self

    def docstring(self, content):
        """
        Writes a docstring. If content is a string, it writes a single-line docstring. If content is an iterable of strings, it writes a multi-line docstring.

        Args:
            content: A string for a single-line docstring or an iterable of strings for a multi line docstring
        Returns:
            The CodeWriter instance
        """
        if isinstance(content, str):
            self.writeln('"""{}"""'.format(content))
            return self
        self.writeln('"""')
        for line in content:
            self.writeln(line)
        self.writeln('"""')
        return self

    def import_(self, module, *items):
        """
        Writes an import statement. If items are provided, it writes a from-import statement.
        Otherwise, it writes a regular import statement.

        Args:
            module: The module to import
            *items: Optional items to import from the module (if empty, imports the whole module)
        Returns:
            The CodeWriter instance
        """
        if items:
            self.writeln("from {} import {}".format(module, ', '.join(items)))
        else:
            self.writeln("import {}".format(module))
        return self

    @contextmanager
    def block(self, header):
        """
        Create a generic code block with a header (e.g. if, for, while, try, etc.)

        Args:
            header: The header line for the code block
        """
        self.writeln(header)
        with self.indent():
            yield self

    @contextmanager
    def class_(
        self,
        name,
        bases = None,
        decorators = None
    ):
        """
        Generate a class definition with optional base classes and decorators.

        Args:
            name: The name of the class
            bases: Optional iterable of base class names
            decorators: Optional iterable of decorator names
        """
        if decorators is not None:
            for dec in decorators:
                self.writeln("@{}".format(dec))

        bases_str = "({})".format(', '.join(bases)) if bases else ""
        self.writeln("class {}{}:".format(name, bases_str))

        with self.indent():
            yield self

    @contextmanager
    def dataclass(
        self,
        name,
        bases = None,
        decorators = None,
        frozen = False,
        slots = False,
        decorator_name = "dataclasses.dataclass"
    ):
        """
        Generate a dataclass definition with optional base classes, decorators and dataclass parameters.

        Args:
            name: The name of the dataclass
            bases: Optional iterable of base class names
            decorators: Optional iterable of additional decorator names
            frozen: Whether to set frozen=True in the dataclass decorator
            slots: Whether to set slots=True in the dataclass decorator
            decorator_name: The full name of the dataclass decorator to use
        """
        dc_params = []
        if frozen:
            dc_params.append("frozen=True")
        if slots:
            dc_params.append("slots=True")

        dc_decorator = (
            "{}({})".format(decorator_name, ', '.join(dc_params))
            if dc_params
            else decorator_name
        )

        all_decorators = []
        if decorators is not None:
            all_decorators.extend(decorators)
        all_decorators.append(dc_decorator)

        for dec in all_decorators:
            self.writeln("@{}".format(dec))

        bases_str = "({})".format(', '.join(bases)) if bases else ""
        self.writeln("class {}{}:".format(name, bases_str))

        with self.indent():
            yield self

    @contextmanager
    def enum(
        self,
        name,
        enum_type = "enum.Enum",
        bases = None,
        decorators = None
    ):
        """
        Generate an enum definition with optional base classes and decorators.

        Args:
            name: The name of the enum
            enum_type: The base enum type to inherit from (default)
            bases: Optional iterable of additional base class names
            decorators: Optional iterable of decorator names
        """
        if decorators is not None:
            for dec in decorators:
                self.writeln("@{}".format(dec))

        all_bases = [enum_type]
        if bases is not None:
            all_bases.extend(bases)

        bases_str = ", ".join(all_bases)
        self.writeln("class {}({}):".format(name, bases_str))

        with self.indent():
            yield self

    def field(
        self,
        name,
        type_hint,
        default = None,
        default_factory = None
    ):
        """
        Write a dataclass field with optional default value or default factory.

        Args:
            name: The name of the field
            type_hint: The type hint for the field
            default: Optional default value for the field
            default_factory: Optional default factory for the field
        """
        if default_factory:
            self.writeln(
                "{}: {} = dataclasses.field(default_factory={})".format(name, type_hint, default_factory)
            )
        elif default is not None:
            self.writeln("{}: {} = {}".format(name, type_hint, default))
        else:
            self.writeln("{}: {}".format(name, type_hint))
        return self

    def enum_member(self, name, value):
        """
        Write an enum member with a specific value.

        Args:
            name: The name of the enum member
            value: The value of the enum member
        """
        self.writeln("{} = {}".format(name, value))
        return self

    @contextmanager
    def function(
        self,
        name,
        params,
        decorators = None,
        return_type = None
    ):
        """
        Create a function definition with optional decorators and return type.

        Args:
            name: The name of the function
            params: An iterable of parameter strings or a single string for the parameter list
            decorators: Optional iterable of decorator names
            return_type: Optional return type hint for the function
        """
        if decorators is not None:
            for dec in decorators:
                self.writeln("@{}".format(dec))

        params_str = params if isinstance(params, str) else ", ".join(params)
        return_annotation = " -> {}".format(return_type) if return_type else ""
        self.writeln("def {}({}){}:".format(name, params_str, return_annotation))

        with self.indent():
            yield self

    @contextmanager
    def method(
        self,
        name,
        params,
        decorators = None,
        return_type = None
    ):
        """
        Create a method definition within a class with optional decorators and return type.

        Args:
            name: The name of the method
            params: An iterable of parameter strings or a single string for the parameter list
            decorators: Optional iterable of decorator names
            return_type: Optional return type hint for the method
        """
        with self.function(
            name, params, decorators=decorators, return_type=return_type
        ):
            yield self

    @contextmanager
    def if_(self, condition):
        """
        Create an if block

        Args:
            condition: The condition for the if statement
        """
        self.writeln("if {}:".format(condition))
        with self.indent():
            yield self

    @contextmanager
    def elif_(self, condition):
        """
        Create an elif block

        Args:
            condition: The condition for the elif statement
        """
        self.writeln("elif {}:".format(condition))
        with self.indent():
            yield self

    @contextmanager
    def else_(self):
        """
        Create an else block
        """
        self.writeln("else:")
        with self.indent():
            yield self

    @contextmanager
    def for_(
        self, var, iterable
    ):
        """
        Create a for loop

        Args:
            var: The loop variable
            iterable: The iterable to loop over
        """
        self.writeln("for {} in {}:".format(var, iterable))
        with self.indent():
            yield self

    @contextmanager
    def while_(self, condition):
        """
        Create a while loop

        Args:
            condition: The condition for the while loop
        """
        self.writeln("while {}:".format(condition))
        with self.indent():
            yield self

    def assignment(
        self, var, value, type_hint = None
    ):
        """
        Write a variable assignment with optional type hint

        Args:
            var: The variable name
            value: The value to assign to the variable
            type_hint: Optional type hint for the variable
        Returns:
            The CodeWriter instance
        """
        if type_hint:
            self.writeln("{}: {} = {}".format(var, type_hint, value))
        else:
            self.writeln("{} = {}".format(var, value))
        return self

    def return_(self, value = None):
        """
        Write a return statement with an optional return value

        Args:
            value: The value to return (if None, writes a bare return statement)
        Returns:
            The CodeWriter instance
        """
        if value:
            self.writeln("return {}".format(value))
        else:
            self.writeln("return")
        return self

    def pass_(self):
        """
        Write a pass statement

        Returns:
            The CodeWriter instance
        """
        self.writeln("pass")
        return self

    def blank_line(self, count = 1):
        """
        Write one or more blank lines

        Args:
            count: The number of blank lines to write
        Returns:
            The CodeWriter instance
        """
        self._lines.extend([""] * count)
        return self

    def to_string(self):
        """
        Get the generated code as a single string with newline characters separating lines.

        Returns:
            A string containing the entire generated code.
        """
        return "\n".join(self._lines)

    def to_lines(self):
        """
        Get the generated code as a list of lines

        Returns:
            A list of strings, where each string is a line of generated code.
        """
        return self._lines

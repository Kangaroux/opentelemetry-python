#!/usr/bin/env python
"""
Python 2.7 compatibility refactoring script.

This script refactors Python files to be Python 2.7 compatible by:
1. Removing 'from __future__ import annotations' imports
2. Replacing f-strings with .format() calls
3. Removing type hints from function signatures
4. Removing @dataclass decorators
5. Removing TypeAlias usage (Python 3.10+ feature)
"""

import codecs
import re
import sys


def remove_future_annotations(content):
    """Remove 'from __future__ import annotations' imports."""
    pattern = r"^from __future__ import annotations\s*\n"
    content = re.sub(pattern, "", content, flags=re.MULTILINE)
    return content


def replace_fstrings(content):
    """Replace f-strings with .format() calls."""

    def convert_fstring_to_format(fstring):
        """Convert a single f-string to .format() call."""
        quote = '"' if fstring.startswith('f"') else "'"
        inner = fstring[2:-1]

        exprs = []

        result = ""
        i = 0
        while i < len(inner):
            if inner[i] == "{" and i + 1 < len(inner) and inner[i + 1] == "{":
                result += "{{"
                i += 2
            elif (
                inner[i] == "}" and i + 1 < len(inner) and inner[i + 1] == "}"
            ):
                result += "}}"
                i += 2
            elif inner[i] == "{":
                j = i + 1
                depth = 1
                while j < len(inner) and depth > 0:
                    if inner[j] == "{":
                        depth += 1
                    elif inner[j] == "}":
                        depth -= 1
                    j += 1
                expr = inner[i + 1 : j - 1]
                expr = expr.strip()
                if ":" in expr:
                    expr = expr.split(":")[0].strip()
                if "!" in expr:
                    expr = expr.rsplit("!", 1)[0].strip()
                exprs.append(expr)
                result += "{}"
                i = j
            else:
                result += inner[i]
                i += 1

        if not exprs:
            return quote + result + quote

        return quote + result + quote + ".format(" + ", ".join(exprs) + ")"

    lines = content.split("\n")
    result = []

    for line in lines:
        new_line = line

        while True:
            match = re.search(r'f"([^"\\]*(?:\\.[^"\\]*)*)"', new_line)
            if not match:
                match = re.search(r"f'([^'\\]*(?:\\.[^'\\]*)*)'", new_line)

            if not match:
                break

            fstring = match.group(0)
            converted = convert_fstring_to_format(fstring)
            new_line = (
                new_line[: match.start()] + converted + new_line[match.end() :]
            )

        result.append(new_line)

    content = "\n".join(result)

    lines = content.split("\n")
    result = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Only add + for f-string continuation, not for docstrings
        # Check if this line contains an f-string that was converted
        if stripped.endswith(")"):
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_stripped = next_line.lstrip()
                # Only add + if the next line looks like a string continuation
                # (starts with quote and the current line has .format() which indicates f-string conversion)
                if (
                    next_stripped.startswith('"')
                    or next_stripped.startswith("'")
                ) and ".format(" in line:
                    indent = line[: len(line) - len(stripped)]
                    result.append(stripped + " +")
                    i += 1
                    continue

        result.append(line)
        i += 1

    return "\n".join(result)


def remove_type_hints(content):
    """Remove type hints from function signatures and class attributes.

    Conservative approach: only remove hints from known patterns to avoid
    breaking valid Python 2.7 syntax.
    """
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this starts a function definition
        if re.search(r"\bdef\s+\w+\s*\(", line):
            # Collect all lines of the function signature
            sig_lines = []
            paren_count = line.count("(") - line.count(")")
            sig_lines.append(line)
            i += 1

            # Continue until we find the closing paren and colon
            while paren_count > 0 and i < len(lines):
                sig_lines.append(lines[i])
                paren_count += lines[i].count("(") - lines[i].count(")")
                i += 1

            # Also add the line with the colon if not already included
            if i < len(lines) and lines[i].strip().startswith(":"):
                sig_lines.append(lines[i])
                i += 1

            # Process each line of the signature separately
            processed_lines = []
            idx = 0
            while idx < len(sig_lines):
                sig_line = sig_lines[idx]

                # Check if this line starts a multi-line type annotation (param: Type[)
                # where the closing bracket is on a subsequent line
                multi_line_match = re.search(r"(\w+)\s*:\s*\w+\[", sig_line)
                if multi_line_match:
                    # Check if this line has a matching closing bracket
                    bracket_count = sig_line.count("[") - sig_line.count("]")
                    if bracket_count > 0:
                        # This is a multi-line type annotation
                        # Collect all lines until the bracket is closed
                        type_lines = [sig_line]
                        j = idx + 1
                        while bracket_count > 0 and j < len(sig_lines):
                            type_lines.append(sig_lines[j])
                            bracket_count += sig_lines[j].count(
                                "["
                            ) - sig_lines[j].count("]")
                            j += 1

                        # The type annotation is from "param: Type[" to the closing "]"
                        # We need to remove everything from ":" to the closing "]" (and comma)
                        param_name = multi_line_match.group(1)

                        # Find the position of the closing bracket in the last line
                        last_line = type_lines[-1]
                        # Match ] followed by optional = value and optional comma
                        bracket_match = re.search(r"\]", last_line)
                        if bracket_match:
                            after_bracket = last_line[bracket_match.end() :]
                            # Check for = value
                            eq_match = re.search(
                                r"\s*=\s*(\S+)", after_bracket
                            )
                            default_value = ""
                            if eq_match:
                                default_value = " = " + eq_match.group(1)
                                # Check for trailing comma after the value
                                after_value = after_bracket[eq_match.end() :]
                                comma_match = re.search(r",\s*$", after_value)
                                suffix = "," if comma_match else ""
                            else:
                                # No = value, check for trailing comma directly
                                comma_match = re.search(
                                    r",\s*$", after_bracket
                                )
                                suffix = "," if comma_match else ""
                        else:
                            default_value = ""
                            suffix = ""

                        # Reconstruct the line with just the parameter name
                        indent = len(sig_line) - len(sig_line.lstrip())
                        processed_lines.append(
                            " " * indent + param_name + default_value + suffix
                        )
                        idx = j
                        continue

                # First pass: replace Type[...] with just "Type" to simplify parsing
                # Use bracket-matching to properly handle nested brackets
                changed = True
                while changed:
                    changed = False
                    # Find the rightmost [ that we can match
                    for match in re.finditer(r"\w+\[", sig_line):
                        start = match.end() - 1
                        # Find matching ]
                        depth = 1
                        pos = start + 1
                        while pos < len(sig_line) and depth > 0:
                            if sig_line[pos] == "[":
                                depth += 1
                            elif sig_line[pos] == "]":
                                depth -= 1
                            pos += 1
                        if depth == 0:
                            # Found matching brackets, replace the whole thing
                            name = sig_line[match.start() : match.end() - 1]
                            sig_line = (
                                sig_line[: match.start()]
                                + name
                                + sig_line[pos:]
                            )
                            changed = True
                            break

                # Remove parameter type hints: param: Type followed by comma
                # Type can be simple name or dotted name like types.AttributeValue
                sig_line = re.sub(
                    r"(\w+)\s*:\s*\w+(?:\.\w+)*,",
                    r"\1,",
                    sig_line,
                )

                # Remove parameter type hints followed by default value (e.g., param: Optional = None)
                sig_line = re.sub(
                    r"(\w+)\s*:\s*\w+(?:\.\w+)*\s*=",
                    r"\1 =",
                    sig_line,
                )

                # Check if this is the last line (has closing paren and colon)
                if idx == len(sig_lines) - 1 or ")" in sig_line:
                    # Remove trailing parameter hints before closing paren
                    sig_line = re.sub(
                        r"(\w+)\s*:\s*\w+(?:\.\w+)*\s*(\))",
                        r"\1\2",
                        sig_line,
                    )
                    # Remove trailing comma before closing paren (left after type hint removal)
                    sig_line = re.sub(r",\s*(\))", r"\1", sig_line)
                    # Remove return type hints: ) -> Type:
                    # Simply remove everything from -> to the final : (but not inside comments)
                    sig_line = re.sub(r"\)\s*->[^:#]*:", "):", sig_line)
                else:
                    # Remove trailing parameter hints at end of line (no comma, no paren)
                    sig_line = re.sub(
                        r"(\w+)\s*:\s*\w+(?:\.\w+)*$",
                        r"\1",
                        sig_line,
                    )
                    # Remove trailing comma at end of line only if next line starts with )
                    # This handles cases where ) is on its own line after type hint removal
                    if idx + 1 < len(sig_lines):
                        next_sig_line = sig_lines[idx + 1].strip()
                        if next_sig_line.startswith(
                            ")"
                        ) or next_sig_line.startswith("):"):
                            sig_line = re.sub(r",\s*$", "", sig_line)
                    # Remove keyword-only argument separator (*,) - Python 2.7 doesn't support it
                    if sig_line.strip() == "*," or sig_line.strip() == "*":
                        # Skip this line entirely
                        processed_lines.append("")
                        idx += 1
                        continue
                    # Also remove *, from the middle of a line (e.g., "self, *, param")
                    sig_line = re.sub(r",\s*\*\s*,", ",,", sig_line)
                    # Clean up double commas
                    sig_line = re.sub(r",\s*,", ",", sig_line)

                processed_lines.append(sig_line)
                idx += 1

            # Add processed signature lines back
            result.extend(processed_lines)
            continue

        result.append(line)
        i += 1

    content = "\n".join(result)

    # Remove Generic[type] from class definitions
    content = re.sub(r",\s*Generic\s*\[[^\]]+\]", "", content)

    # Remove class attribute type annotations (e.g., self._dict: Union[...] = {})
    # Handle multi-line type annotations
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip if line contains dictionary access like self[key] or dict[key]
        # But not type annotations like Getter[Type]
        # Only skip if it looks like actual dictionary access (variable[...]) not type annotation (name: Type[...])
        if re.search(r"\b(self|dict_|carrier)\s*\[", line) and not re.search(
            r":\s*\w+\s*\[", line
        ):
            result.append(line)
            i += 1
            continue

        # Check if this starts a type annotation with brackets (e.g., name: Type[...] = value)
        if re.search(r":\s*\w+\[", line):
            # Check if there's an assignment (=) on this line or subsequent lines
            has_assignment = "=" in line
            if not has_assignment:
                # Look ahead for assignment
                j = i + 1
                while j < len(lines) and "=" not in lines[j]:
                    j += 1
                has_assignment = j < len(lines)

            if has_assignment:
                # Collect all lines of the type annotation
                type_lines = [line]
                bracket_count = line.count("[") - line.count("]")
                j = i + 1
                while bracket_count > 0 and j < len(lines):
                    type_lines.append(lines[j])
                    bracket_count += lines[j].count("[") - lines[j].count("]")
                    j += 1

                # Reconstruct without type annotation
                if j > i + 1:
                    # Multi-line annotation
                    # First line: remove ": Type[..." up to and including the opening bracket
                    first_line = re.sub(r":\s*\w+\[.*$", "", type_lines[0])
                    # Last line: remove "] =" and keep " ="
                    last_line = type_lines[-1]
                    last_line = re.sub(r"\]\s*=", "=", last_line)
                    # Remove trailing whitespace from first line
                    first_line = first_line.rstrip()
                    # Join first line with last line
                    combined = first_line + last_line
                    result.append(combined)
                    i = j
                else:
                    # Single-line annotation - use bracket-matching to properly handle nested brackets
                    # Find the colon and the type annotation that follows
                    colon_match = re.search(r":\s*\w+\[", line)
                    if colon_match:
                        start = colon_match.start()
                        # Find the matching closing bracket using bracket counting
                        bracket_start = colon_match.end() - 1
                        depth = 1
                        pos = bracket_start + 1
                        while pos < len(line) and depth > 0:
                            if line[pos] == "[":
                                depth += 1
                            elif line[pos] == "]":
                                depth -= 1
                            pos += 1
                        if depth == 0:
                            # Found matching brackets, remove from colon to end of type
                            line = line[:start] + line[pos:]
                    result.append(line)
                    i += 1
                continue

        # Simplify nested brackets for single-line annotations
        # Use iterative approach to handle nested brackets
        changed = True
        while changed:
            changed = False
            # Find the rightmost [ that has a matching ]
            for match in re.finditer(r"\w+\[", line):
                start = match.end() - 1
                # Find matching ]
                depth = 1
                pos = start + 1
                while pos < len(line) and depth > 0:
                    if line[pos] == "[":
                        depth += 1
                    elif line[pos] == "]":
                        depth -= 1
                    pos += 1
                if depth == 0:
                    # Found matching brackets, replace the whole thing
                    name = line[match.start() : match.end() - 1]
                    line = line[: match.start()] + name + line[pos:]
                    changed = True
                    break
        # Remove type annotation: name: Type = value
        line = re.sub(r"(\w+)\s*:\s*\w+(?:\.\w+)*\s*=", r"\1 =", line)
        # Remove class attribute type annotations without assignment (e.g., _threshold: int)
        # Only do this if the line is just a type annotation (possibly with leading whitespace)
        if re.match(r"^\s*\w+\s*:\s*\w+(?:\.\w+)*\s*$", line):
            # Extract just the variable name
            match = re.match(r"^\s*(\w+)\s*:\s*\w+(?:\.\w+)*\s*$", line)
            if match:
                indent = len(line) - len(line.lstrip())
                line = " " * indent + match.group(1)
        result.append(line)
        i += 1
    content = "\n".join(result)

    return content


def remove_async_await(content):
    """Remove async/await keywords for Python 2.7 compatibility."""
    # Remove 'async def' -> 'def'
    content = re.sub(r"async\s+def", "def", content)
    # Remove 'await ' keyword
    content = re.sub(r"\bawait\s+", "", content)
    return content


def replace_dict_unpacking(content):
    """Replace dictionary unpacking **expr with dict.update() pattern."""
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if this line starts a dictionary assignment
        if re.search(r"(\w+)\s*=\s*\{", line):
            # Find the matching closing brace
            brace_count = line.count("{") - line.count("}")
            dict_lines = [line]
            j = i + 1
            while brace_count > 0 and j < len(lines):
                dict_lines.append(lines[j])
                brace_count += lines[j].count("{") - lines[j].count("}")
                j += 1

            # Process the dictionary
            combined = "\n".join(dict_lines)

            # Find all ** unpacking expressions
            unpacking_vars = re.findall(r"\*\*(\w+)", combined)

            if unpacking_vars:
                # Get the variable being assigned to
                assign_match = re.search(r"(\w+)\s*=\s*\{", line)
                if assign_match:
                    assign_var = assign_match.group(1)
                    indent = line[: len(line) - len(line.lstrip())]

                    # Get the first unpacking variable
                    first_var = unpacking_vars[0]

                    # Build replacement lines
                    replacement_lines = [
                        indent + assign_var + " = " + first_var
                    ]

                    # Check if there are more items in the dictionary
                    # Remove ** unpacking and braces to see what's left
                    temp = re.sub(r"\s*\*\*\w+\s*,?\s*", "", combined)
                    # Remove the assignment part and opening brace
                    temp = re.sub(r".*=\s*\{", "", temp)
                    # Remove trailing brace and whitespace
                    temp = re.sub(r"\}\s*$", "", temp, flags=re.MULTILINE)

                    if temp.strip():
                        # There are additional items - use update()
                        replacement_lines.append(
                            indent
                            + assign_var
                            + ".update({"
                            + temp.strip()
                            + "})"
                        )

                    result.extend(replacement_lines)
                    i = j
                    continue

        result.append(line)
        i += 1

    content = "\n".join(result)
    return content


def remove_walrus_operators(content):
    """Replace walrus operators (:=) with traditional assignments."""

    # Pattern: if (var := expr):
    # Convert to: var = expr\nif var:
    def replace_walrus(match):
        before = match.group(1)
        var = match.group(2)
        expr = match.group(3)
        return before + var + " = " + expr + "\n" + before + var + ":"

    content = re.sub(
        r"(if\s+)\((\w+)\s*:=\s*([^)]+)\)", replace_walrus, content
    )
    return content


def remove_typealias(content):
    """Remove TypeAlias usage (Python 3.10+ feature)."""
    # Remove import line
    content = re.sub(
        r"^from typing_extensions import TypeAlias\s*\n",
        "",
        content,
        flags=re.MULTILINE,
    )
    # Replace "name: TypeAlias = value" with "name = value"
    content = re.sub(
        r"^(\w+):\s*TypeAlias\s*=\s*(.+)$",
        r"\1 = \2",
        content,
        flags=re.MULTILINE,
    )
    return content


def remove_forward_references(content):
    """Remove forward reference strings in function signatures."""
    lines = content.split("\n")
    result = []
    for line in lines:
        # Only remove quoted strings in type contexts
        # Forward refs look like: "TypeName" or "Callable[...]"
        # The quoted string should contain only type names (alphanumeric, dots, brackets, commas)
        # Not arbitrary content like "0x{...}" or dictionary values
        # Pattern: param: "Type[Name]" or param: "TypeName"
        # But not: "key": "value" (dictionary)
        if re.search(r"\w+\s*:\s*\"", line):
            # Replace ": "Type..." with empty string (removes both colon and forward ref)
            # Only match if the quoted string looks like a type name
            line = re.sub(
                r"(\w+)\s*:\s*\"[A-Za-z_][A-Za-z0-9_\[\],\s\.]*\"", r"\1", line
            )
        result.append(line)
    content = "\n".join(result)
    return content


def remove_dataclass_decorators(content):
    """Remove @dataclass decorators."""
    content = re.sub(
        r"^@dataclass(\([^)]*\))?\s*\n", "", content, flags=re.MULTILINE
    )
    return content


def replace_union_syntax(content):
    """Replace Python 3.10+ union syntax (X | Y) with Union[X, Y]."""

    def replace_union(match):
        left = match.group(1).strip()
        right = match.group(2).strip()
        if right == "None":
            return "Optional[{}]".format(left)
        return "Union[{}, {}]".format(left, right)

    # First, handle multi-line unions by joining lines that end with | or start with |
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if line ends with | (multi-line union)
        if re.search(r"\|\s*$", line):
            # Collect all lines of the union
            union_lines = [line.rstrip().rstrip("|").rstrip()]
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith("|"):
                    # Remove leading | and whitespace
                    union_lines.append(next_line.lstrip("|").lstrip())
                    j += 1
                else:
                    break
            # Join the union into a single line with | separators
            joined = " | ".join(union_lines)
            # Add the rest of the last line if there was more content
            if j > i + 1:
                last_full_line = lines[j - 1]
                after_pipe = last_full_line[
                    len(lines[j - 1].strip().lstrip("|")) :
                ]
                joined += after_pipe
            result.append(joined)
            i = j
            continue
        # Check if next line starts with | (multi-line union starting on this line)
        if i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            # Collect all lines of the union
            union_lines = [line.rstrip()]
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith("|"):
                    # Remove leading | and whitespace
                    union_lines.append(next_line.lstrip("|").lstrip())
                    j += 1
                else:
                    break
            # Join the union into a single line with | separators
            joined = " | ".join(union_lines)
            result.append(joined)
            i = j
            continue
        result.append(line)
        i += 1
    content = "\n".join(result)

    # Match type | type where type can include brackets (e.g., Sequence[Link] | None)
    # This pattern handles nested brackets by matching non-greedy content
    pattern = r"([^|\s]+\[[^\]]*\]|[\w.]+)\s*\|\s*([\w.]+)"
    content = re.sub(pattern, replace_union, content)
    return content


def replace_dataclasses(content):
    """Remove @dataclass decorators (simple approach)."""
    content = re.sub(r"@dataclass[^)]*\)\s*\n", "", content)
    content = re.sub(r"@dataclass\s*\n", "", content)
    return content


def replace_raise_from(content):
    """Replace 'raise ... from ...' syntax with Python 2.7 compatible syntax."""
    content = re.sub(r"raise\s+([^\n]+)\s+from\s+[^\n]+", r"raise \1", content)
    return content


def replace_ellipsis_with_pass(content):
    """Replace bare ellipsis (...) with pass for Python 2.7 compatibility."""
    # Replace "): ..." with "): pass"
    content = re.sub(r"\):\s*\.\.\.", "): pass", content)
    # Replace "; ..." with "; pass"
    content = re.sub(r";\s*\.\.\.", "; pass", content)
    # Replace "...  # comment" with "pass  # comment" - preserve indentation
    content = re.sub(
        r"^(\s*)\.\.\.\s*(#.*)?$", r"\1pass \2", content, flags=re.MULTILINE
    )
    return content


def refactor_file(filepath):
    """Refactor a single Python file for Python 2.7 compatibility."""
    try:
        with codecs.open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Apply transformations in order
        content = remove_future_annotations(content)
        content = remove_typealias(content)
        content = replace_fstrings(content)
        content = replace_union_syntax(content)
        content = remove_forward_references(content)
        content = remove_type_hints(content)
        content = remove_async_await(content)
        content = replace_dict_unpacking(content)
        content = remove_walrus_operators(content)
        content = remove_dataclass_decorators(content)
        content = replace_raise_from(content)
        content = replace_ellipsis_with_pass(content)

        # Write back if changed
        if content != original_content:
            with codecs.open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print("Error processing {}: {}".format(filepath, e))
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python refactor_to_py27.py <file1.py> [file2.py ...]")
        sys.exit(1)

    modified = 0
    for filepath in sys.argv[1:]:
        if refactor_file(filepath):
            print("Refactored: {}".format(filepath))
            modified += 1

    print("\nModified {} files".format(modified))


if __name__ == "__main__":
    main()

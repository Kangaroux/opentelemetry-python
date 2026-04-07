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

    def replace_fstring(match):
        fstring = match.group(0)
        quote = '"' if fstring.startswith('f"') else "'"
        inner = fstring[2:-1]

        exprs = []
        result = inner

        def extract_expr(m):
            expr = m.group(1)
            expr = expr.strip()
            if ":" in expr:
                expr = expr.split(":")[0].strip()
            if "!" in expr:
                expr = expr.rsplit("!", 1)[0].strip()
            exprs.append(expr)
            return "{}"

        result = re.sub(r"\{([^}]*)\}", extract_expr, result)

        if not exprs:
            return quote + result + quote

        return quote + result + quote + ".format(" + ", ".join(exprs) + ")"

    content = re.sub(r'f"([^"\\]*(?:\\.[^"\\]*)*)"', replace_fstring, content)
    content = re.sub(r"f'([^'\\]*(?:\\.[^'\\]*)*)'", replace_fstring, content)

    return content


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

            # Join signature lines and process
            sig_text = "\n".join(sig_lines)

            # Remove return type hints (-> Type)
            sig_text = re.sub(r"\s*->\s*[^,)\n]+", "", sig_text)

            # Remove parameter type hints: param: Type
            # Only match patterns like "name: Type" where Type is a known type
            sig_text = re.sub(
                r"(\w+)\s*:\s*(Union|Optional|List|Dict|Tuple|Callable|Sequence|Iterable|Generator|TypeVar|Generic|Type|Any)[(,\s\n]",
                r"\1",
                sig_text,
            )
            sig_text = re.sub(
                r"(\w+)\s*:\s*[^,\)\n]+(?=[,)\n])",
                r"\1",
                sig_text,
            )

            # Add processed signature lines back
            result.extend(sig_text.split("\n"))
            continue

        result.append(line)
        i += 1

    content = "\n".join(result)

    # Remove Generic[type] from class definitions
    content = re.sub(r",\s*Generic\s*\[[^\]]+\]", "", content)

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
        if re.search(r":\s*\"", line):
            line = re.sub(r'"\w+"', "Type", line)
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
    # Replace type | None with Optional[type]
    content = re.sub(r"(\w+)\s*\|\s*None", r"Optional[\1]", content)
    # Replace type1 | type2 with Union[type1, type2]
    content = re.sub(r"(\w+)\s*\|\s*(\w+)", r"Union[\1, \2]", content)
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
        content = remove_type_hints(content)
        content = remove_walrus_operators(content)
        content = remove_forward_references(content)
        content = replace_union_syntax(content)
        content = replace_dataclass_decorators(content)
        content = replace_raise_from(content)

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

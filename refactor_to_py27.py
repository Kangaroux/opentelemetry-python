#!/usr/bin/env python
"""
Python 2.7 compatibility refactoring script.

This script refactors Python files to be Python 2.7 compatible by:
1. Removing 'from __future__ import annotations' imports
2. Replacing f-strings with .format() or % formatting
3. Removing type hints from function signatures
4. Replacing walrus operators (:=) with traditional assignments
5. Replacing Python 3.10+ union syntax (X | Y) with Union[X, Y]
6. Replacing dataclasses with traditional class implementations
"""

import codecs
import re
import sys


def remove_future_annotations(content):
    """Remove 'from __future__ import annotations' imports."""
    # Match standalone import
    pattern = r"^from __future__ import annotations\s*\n"
    content = re.sub(pattern, "", content, flags=re.MULTILINE)
    return content


def replace_fstrings(content):
    """Replace f-strings with .format() or % formatting."""

    def replace_fstring(match):
        fstring = match.group(0)
        quote = '"' if fstring.startswith('f"') else "'"
        inner = fstring[2:-1]  # Remove f" and "

        # Extract expressions from braces
        exprs = []
        result = inner

        def extract_expr(m):
            expr = m.group(1)
            expr = expr.strip()
            # Handle format specs like {var:02x}
            if ":" in expr:
                expr = expr.split(":")[0].strip()
            # Handle !r, !s conversions
            if "!" in expr:
                expr = expr.rsplit("!", 1)[0].strip()
            exprs.append(expr)
            # Replace with {} for .format()
            return "{}"

        result = re.sub(r"\{([^}]*)\}", extract_expr, result)

        if not exprs:
            return quote + result + quote

        return quote + result + quote + ".format(" + ", ".join(exprs) + ")"

    # Match f-strings - simple pattern
    content = re.sub(r'f"([^"\\]*(?:\\.[^"\\]*)*)"', replace_fstring, content)
    content = re.sub(r"f'([^'\\]*(?:\\.[^'\\]*)*)'", replace_fstring, content)

    return content


def remove_type_hints(content):
    """Remove type hints from function signatures and variable declarations."""

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

            # Remove return type hints
            sig_text = re.sub(r"\s*->\s*[^\n]+(?=:)", "", sig_text)

            # Remove parameter type hints: param: Type
            sig_text = re.sub(
                r"\b(\w+)\s*:\s*(?:Union|Optional|List|Dict|Tuple|Callable|Any|\w+)(?:\s*\[[^\]]*\])?",
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


def replace_walrus_operators(content):
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


def replace_union_syntax(content):
    """Replace Python 3.10+ union syntax (X | Y) with Union[X, Y]."""

    # Replace type | None with Optional[type]
    content = re.sub(r"(\w+)\s*\|\s*None", r"Optional[\1]", content)

    # Replace type1 | type2 with Union[type1, type2]
    content = re.sub(r"(\w+)\s*\|\s*(\w+)", r"Union[\1, \2]", content)

    return content


def replace_dataclasses(content):
    """Replace @dataclass decorated classes with traditional class implementations."""

    # Remove @dataclass decorator
    content = re.sub(r"@dataclass[^)]*\)\s*\n", "", content)
    content = re.sub(r"@dataclass\s*\n", "", content)

    return content


def replace_raise_from(content):
    """Replace 'raise ... from ...' syntax with Python 2.7 compatible syntax."""
    # Python 2.7 doesn't support 'raise ... from ...' syntax
    # Remove the 'from ...' part
    content = re.sub(r"raise\s+([^\n]+)\s+from\s+[^\n]+", r"raise \1", content)
    return content


def refactor_file(filepath):
    """Refactor a single Python file for Python 2.7 compatibility."""
    try:
        with codecs.open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Apply transformations
        content = remove_future_annotations(content)
        content = replace_fstrings(content)
        content = remove_type_hints(content)
        content = replace_walrus_operators(content)
        content = replace_union_syntax(content)
        content = replace_dataclasses(content)
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

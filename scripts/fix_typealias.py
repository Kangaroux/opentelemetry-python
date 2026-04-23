#!/usr/bin/env python3
"""Fix TypeAlias import in generated models.py for Python 3.9 compatibility."""

import re
import sys
from pathlib import Path


def fix_typealias_import(file_path):
    """Fix TypeAlias import for Python 3.9 compatibility.

    TypeAlias is only available in the typing module from Python 3.10+.
    For Python 3.9, it must be imported from typing_extensions.
    """
    path = Path(file_path)
    content = path.read_text()

    if "from typing import" not in content or "TypeAlias" not in content:
        print("No TypeAlias import found in {}".format(file_path))
        return

    # Find the typing import line
    pattern = r"from typing import ([^\n]+)"
    match = re.search(pattern, content)

    if not match or "TypeAlias" not in match.group(1):
        print("TypeAlias not in typing import in {}".format(file_path))
        return

    # Remove TypeAlias from typing import
    imports = [
        imp.strip()
        for imp in match.group(1).split(", ")
        if "TypeAlias" not in imp
    ]
    new_typing_import = "from typing import {}".format(', '.join(imports))

    # Replace the old import and add typing_extensions import
    old_import = match.group(0)
    new_imports = (
        "{}\n\nfrom typing_extensions import TypeAlias".format(new_typing_import)
    )

    content = content.replace(old_import, new_imports, 1)
    path.write_text(content)
    print("Fixed TypeAlias import for Python 3.9 in {}".format(file_path))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: fix_typealias.py <path_to_models.py>\n")
        sys.exit(1)

    fix_typealias_import(sys.argv)

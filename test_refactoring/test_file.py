# Test file for Python 2.7 refactoring validation
# This file uses various modern Python features

from __future__ import annotations


class DataProcessor:
    """A simple data processor class."""

    def __init__(self, name: str, max_size: int = 100) -> None:
        self.name = name
        self.max_size = max_size
        self.data: list[str] = []

    def add_item(self, item: str) -> bool:
        """Add an item to the data list."""
        if len(self.data) >= self.max_size:
            return False
        self.data.append(item)
        return True

    def get_summary(self) -> str:
        """Return a summary of the data."""
        count = len(self.data)
        return f"Processor '{self.name}' has {count} items"

    def format_item(self, index: int) -> str:
        """Format a single item with its index."""
        if index < len(self.data):
            item = self.data[index]
            return f"Item {index}: {item}"
        return f"Index {index} out of range"


def process_data(items: list[str], threshold: int) -> dict[str, int]:
    """Process a list of items and return counts."""
    result: dict[str, int] = {}

    for item in items:
        length = len(item)
        if length >= threshold:
            key = "long"
        else:
            key = "short"
        result[key] = result.get(key, 0) + 1

    return result


def find_match(pattern: str, text: str) -> Optional[str]:
    """Find a pattern in text."""
    if pattern in text:
        return f"Found '{pattern}' in text"
    return None


def calculate_value(x: int, y: int) -> int:
    """Calculate a simple value."""
    result: int = x + y
    return result


if __name__ == "__main__":
    processor = DataProcessor("test", 50)
    processor.add_item("hello")
    processor.add_item("world")

    summary = processor.get_summary()
    print(summary)

    items = ["a", "bb", "ccc", "dddd"]
    counts = process_data(items, 3)
    print(f"Counts: {counts}")

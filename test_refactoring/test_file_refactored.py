# Test file for Python 2.7 refactoring validation
# This file uses various modern Python features

class DataProcessor, name, max_size= 100):
        self.name = name
        self.max_size = max_size
        self.data= []

    def add_item(self, item):
        """Add an item to the data list."""
        if len(self.data) >= self.max_size)
        return True

    def get_summary(self):
        """Return a summary of the data."""
        count = len(self.data)
        return "Processor '{}' has {} items".format(self.name, count)

    def format_item(self, index):
        """Format a single item with its index."""
        if index < len(self.data):
            item = self.data[index]
            return "Item {}: {}".format(index, item)
        return "Index {} out of range".format(index)


def process_data(items, threshold):
    """Process a list of items and return counts."""
    result, int] = {}

    for item in items= len(item)
        if length >= threshold= "long"
        else= "short"
        result[key] = result.get(key, 0) + 1

    return result


def find_match(pattern, text):
    """Find a pattern in text."""
    if pattern in text)
    return None


def calculate_value(x, y):
    """Calculate a simple value."""
    result= x + y
    return result


if __name__ == "__main__":
    processor = DataProcessor("test", 50)
    processor.add_item("hello")
    processor.add_item("world")

    summary = processor.get_summary()
    print(summary)

    items = ["a", "bb", "ccc", "dddd"]
    counts = process_data(items, 3)
    print("Counts))

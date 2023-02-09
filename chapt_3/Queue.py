class Queue:
    """Queue implimentation as a list."""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)
    
    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)
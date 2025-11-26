class Cola:
    """Estructura FIFO para cola de reservas por libro."""

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def to_list(self):
        return list(self._items)

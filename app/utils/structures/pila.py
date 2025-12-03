# app/structures/pila.py

class Pila:
    """Estructura LIFO para historial de préstamos por usuario."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def to_list(self):
        return list(reversed(self._items))  # último préstamo primero

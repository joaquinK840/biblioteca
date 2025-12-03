"""Estructura de datos: Cola FIFO simple.

Clase Cola:
- Uso: almacenar elementos en orden FIFO.
- No impone tipos sobre los elementos almacenados.
- Métodos documentados indican valores de retorno y comportamiento en casos límite.
"""
class Cola:
    """Estructura FIFO para cola de reservas por libro.

    Métodos:
    - enqueue(item): Añade `item` al final de la cola. No devuelve nada.
    - dequeue() -> item|None: Extrae y devuelve el primer elemento de la cola.
      Devuelve None si la cola está vacía.
    - is_empty() -> bool: True si la cola está vacía.
    - __len__() -> int: Número de elementos en la cola.
    - to_list() -> list: Copia de la lista interna de elementos.
    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Añade un elemento al final de la cola.

        Parámetros:
        - item: cualquier objeto que se quiera encolar.

        Retorna:
        - None (efecto lateral: modifica la cola).
        """
        self._items.append(item)

    def dequeue(self):
        """Extrae el primer elemento de la cola.

        Retorna:
        - El primer elemento encolado o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        return self._items.pop(0)

    def is_empty(self) -> bool:
        """Indica si la cola está vacía.

        Retorna:
        - True si no hay elementos, False en caso contrario.
        """
        return len(self._items) == 0

    def __len__(self):
        """Número de elementos en la cola."""
        return len(self._items)

    def to_list(self):
        """Devuelve una copia de la lista interna (no la referencia).

        Útil para inspección o serialización sin modificar la cola.
        """
        return list(self._items)

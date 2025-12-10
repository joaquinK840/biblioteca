"""Data structure: Simple FIFO queue.

Queue class:
- Purpose: store elements in FIFO order.
- Does not enforce types on stored elements.
- Methods document return values and edge-case behavior.
"""

import json
import os

# Queue (FIFO): reservation queue per book
class Cola:
    """FIFO queue used for per-book reservations.

    Methods:
    - enqueue(item): Add item to the end of the queue.
    - dequeue() -> item|None: Remove and return the first element; None if empty.
    - is_empty() -> bool: True if the queue is empty.
    - __len__() -> int: Number of elements in the queue.
    - to_list() -> list: Copy of internal elements.
    - guardar_en_archivo(ruta_archivo): Save the queue to a JSON file.
    - cargar_desde_archivo(ruta_archivo): Load the queue from a JSON file.
    """
    # Constructor: start empty queue
    def __init__(self):
        self._items = []

    # Enqueue: add to queue tail
    def enqueue(self, item):
        """Add an element to the end of the queue.

        Parameters:
        - item: any object to be enqueued.

        Returns:
        - None (side effect: modifies the queue).
        """
        self._items.append(item)

    # Dequeue: remove and return the first element
    def dequeue(self):
        """Remove the first element of the queue.

        Returns:
        - The first enqueued element or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self._items.pop(0)

    # Indicates if the queue has no elements
    def is_empty(self) -> bool:
        """Indicate whether the queue is empty.

        Returns:
        - True if there are no elements, False otherwise.
        """
        return len(self._items) == 0

    # Current queue size
    def __len__(self):
        """Number of elements in the queue."""
        return len(self._items)

    # Shallow copy of elements (not original reference)
    def to_list(self):
        """Return a copy of the internal list (not a reference).

        Useful for inspection or serialization without modifying the queue.
        """
        return list(self._items)
    
    # Peek: view first element without removing it
    def peek(self):
        """Return the first element without removing it.
        
        Returns:
        - The first element of the queue or None if it's empty.
        """
        if self.is_empty():
            return None
        return self._items[0]

    # Serialize the queue to a JSON file
    def guardar_en_archivo(self, ruta_archivo):
        """Save the queue to a JSON file.
        
        Parameters:
        - ruta_archivo: str, path where to save the file (e.g., 'data/reservas.json')
        
        Returns:
        - None
        
        Example:
        >>> cola = Cola()
        >>> cola.enqueue({"isbn": "123", "usuario": "John"})
        >>> cola.guardar_en_archivo("data/reservas.json")
        """
        try:
            # Create directory if it doesn't exist
            directorio = os.path.dirname(ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
            
            # Save queue in JSON format
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, indent=2, ensure_ascii=False)
            
            print(f"Queue saved successfully to {ruta_archivo}")
        except Exception as e:
            print(f"Error saving queue: {e}")

    # Load the queue from an existing JSON file
    def cargar_desde_archivo(self, ruta_archivo):
        """Load the queue from a JSON file.
        
        Parameters:
        - ruta_archivo: str, path of the file to load
        
        Returns:
        - None (modifies internal queue state)
        
        Note: If the file does not exist, the queue remains empty.
        
        Example:
        >>> cola = Cola()
        >>> cola.cargar_desde_archivo("data/reservas.json")
        """
        try:
            if not os.path.exists(ruta_archivo):
                print(f"File {ruta_archivo} not found. Starting with an empty queue.")
                self._items = []
                return
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self._items = json.load(f)
            
            print(f"Queue loaded successfully from {ruta_archivo}. Elements: {len(self._items)}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Starting with an empty queue.")
            self._items = []
        except Exception as e:
            print(f"Error loading queue: {e}")
            self._items = []

    # Clear all queue elements
    def limpiar(self):
        """Completely clear the queue.
        
        Returns:
        - None
        """
        self._items = []
    
    def __repr__(self):
        """Queue representation for debugging."""
        return f"Queue({len(self._items)} elements)"
    
    def __str__(self):
        """Human-readable queue representation."""
        if self.is_empty():
            return "Empty queue"
        return f"Queue with {len(self._items)} elements: {self._items[:3]}{'...' if len(self._items) > 3 else ''}"
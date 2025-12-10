# app/structures/pila.py

"""Data structure: Simple LIFO stack.

Stack class:
- Purpose: store elements in LIFO order (Last In First Out).
- Used to maintain per-user loan history.
- Methods document return values and edge-case behavior.
"""

import json
import os

# Stack (LIFO): loan history per user
class Pila:
    """LIFO structure for per-user loan history.
    
    Methods:
    - push(item): Add an element to the top of the stack.
    - pop() -> item|None: Remove and return the top element. Returns None if empty.
    - peek() -> item|None: Return the top element without removing it.
    - is_empty() -> bool: True if the stack is empty.
    - __len__() -> int: Number of elements in the stack.
    - to_list() -> list: Return a list with the most recent loan first.
    - guardar_en_archivo(ruta_archivo): Save the stack to a JSON file.
    - cargar_desde_archivo(ruta_archivo): Load the stack from a JSON file.
    - limpiar(): Completely clear the stack.
    """

    # Constructor: start empty stack
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    # Push: add element on top
    def push(self, item):
        """Add an element to the top of the stack.
        
        Parameters:
        - item: any object to be pushed (e.g., dict with ISBN and date).
        
        Returns:
        - None (side effect: modifies the stack).
        
        Example:
        >>> pila = Pila()
        >>> pila.push({"isbn": "123", "fecha": "2025-01-15"})
        """
        self._items.append(item)

    # Pop: remove and return the top element
    def pop(self):
        """Remove and return the top element of the stack.
        
        Returns:
        - The most recently added element, or None if the stack is empty.
        
        Example:
        >>> pila = Pila()
        >>> pila.push("element1")
        >>> pila.pop()
        'element1'
        """
        if self.is_empty():
            return None
        return self._items.pop()

    # Peek: view the top element without removing it
    def peek(self):
        """Return the top element without removing it.
        
        Returns:
        - The most recent element, or None if the stack is empty.
        
        Example:
        >>> pila = Pila()
        >>> pila.push("element1")
        >>> pila.peek()
        'element1'
        >>> len(pila)
        1
        """
        if self.is_empty():
            return None
        return self._items[-1]

    # Indicates whether the stack has no elements
    def is_empty(self) -> bool:
        """Check if the stack is empty.
        
        Returns:
        - True if there are no elements, False otherwise.
        """
        return len(self._items) == 0

    # Current stack size
    def __len__(self):
        """Return the number of elements in the stack.
        
        Returns:
        - int: number of elements.
        """
        return len(self._items)

    # Copy of elements in LIFO order (most recent first)
    def to_list(self):
        """Return a copy of the stack as a list (most recent first).
        
        Returns:
        - list: list with elements in reverse order (LIFO).
        
        Useful for inspection or serialization without modifying the stack.
        """
        return list(reversed(self._items))
    
    # Serialize the stack to a JSON file
    def guardar_en_archivo(self, ruta_archivo):
        """Save the stack to a JSON file.
        
        Parameters:
        - ruta_archivo: str, path where to save the file (e.g., 'data/historial_usuario123.json')
        
        Returns:
        - None
        
        Example:
        >>> pila = Pila()
        >>> pila.push({"isbn": "123", "fecha": "2025-01-15"})
        >>> pila.guardar_en_archivo("data/historial_juan.json")
        """
        try:
            # Create directory if it doesn't exist
            directorio = os.path.dirname(ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
            
            # Save stack in JSON format
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, indent=2, ensure_ascii=False)
            
            print(f"Stack saved successfully to {ruta_archivo}")
        except Exception as e:
            print(f"Error saving stack: {e}")
    
    # Load the stack from an existing JSON file
    def cargar_desde_archivo(self, ruta_archivo):
        """Load the stack from a JSON file.
        
        Parameters:
        - ruta_archivo: str, path of the file to load
        
        Returns:
        - None (modifies internal stack state)
        
        Note: If the file does not exist, the stack remains empty.
        
        Example:
        >>> pila = Pila()
        >>> pila.cargar_desde_archivo("data/historial_juan.json")
        """
        try:
            if not os.path.exists(ruta_archivo):
                print(f"File {ruta_archivo} not found. Starting with an empty stack.")
                self._items = []
                return
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self._items = json.load(f)
            
            print(f"Stack loaded successfully from {ruta_archivo}. Elements: {len(self._items)}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Starting with an empty stack.")
            self._items = []
        except Exception as e:
            print(f"Error loading stack: {e}")
            self._items = []

    # Clear all stack elements
    def limpiar(self):
        """Completely clear the stack.
        
        Returns:
        - None
        
        Example:
        >>> pila = Pila()
        >>> pila.push("element")
        >>> pila.limpiar()
        >>> pila.is_empty()
        True
        """
        self._items = []
    
    def __repr__(self):
        """Stack representation for debugging."""
        return f"Stack({len(self._items)} elements)"
    
    def __str__(self):
        """Human-readable stack representation."""
        if self.is_empty():
            return "Empty stack"
        return f"Stack with {len(self._items)} elements. Top: {self._items[-1]}"
"""Estructura de datos: Cola FIFO simple.

Clase Cola:
- Uso: almacenar elementos en orden FIFO.
- No impone tipos sobre los elementos almacenados.
- Métodos documentados indican valores de retorno y comportamiento en casos límite.
"""

import json
import os

class Cola:
    """Estructura FIFO para cola de reservas por libro.

    Métodos:
    - enqueue(item): Añade `item` al final de la cola. No devuelve nada.
    - dequeue() -> item|None: Extrae y devuelve el primer elemento de la cola.
      Devuelve None si la cola está vacía.
    - is_empty() -> bool: True si la cola está vacía.
    - __len__() -> int: Número de elementos en la cola.
    - to_list() -> list: Copia de la lista interna de elementos.
    - guardar_en_archivo(ruta_archivo): Guarda la cola en un archivo JSON.
    - cargar_desde_archivo(ruta_archivo): Carga la cola desde un archivo JSON.
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
    
    def peek(self):
        """Devuelve el primer elemento de la cola sin quitarlo.
        
        Retorna:
        - El primer elemento de la cola o None si está vacía.
        """
        if self.is_empty():
            return None
        return self._items[0]

    def guardar_en_archivo(self, ruta_archivo):
        """Guarda la cola en un archivo JSON.
        
        Parámetros:
        - ruta_archivo: str, ruta donde guardar el archivo (ej: 'data/reservas.json')
        
        Retorna:
        - None
        
        Ejemplo de uso:
        >>> cola = Cola()
        >>> cola.enqueue({"isbn": "123", "usuario": "Juan"})
        >>> cola.guardar_en_archivo("data/reservas.json")
        """
        try:
            # Crear el directorio si no existe
            directorio = os.path.dirname(ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
            
            # Guardar la cola en formato JSON
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, indent=2, ensure_ascii=False)
            
            print(f"Cola guardada exitosamente en {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar la cola: {e}")

    def cargar_desde_archivo(self, ruta_archivo):
        """Carga la cola desde un archivo JSON.
        
        Parámetros:
        - ruta_archivo: str, ruta del archivo a cargar
        
        Retorna:
        - None (modifica el estado interno de la cola)
        
        Nota: Si el archivo no existe, la cola permanece vacía.
        
        Ejemplo de uso:
        >>> cola = Cola()
        >>> cola.cargar_desde_archivo("data/reservas.json")
        """
        try:
            if not os.path.exists(ruta_archivo):
                print(f"Archivo {ruta_archivo} no encontrado. Iniciando con cola vacía.")
                self._items = []
                return
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self._items = json.load(f)
            
            print(f"Cola cargada exitosamente desde {ruta_archivo}. Elementos: {len(self._items)}")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}. Iniciando con cola vacía.")
            self._items = []
        except Exception as e:
            print(f"Error al cargar la cola: {e}")
            self._items = []

    def limpiar(self):
        """Vacía completamente la cola.
        
        Retorna:
        - None
        """
        self._items = []
    
    def __repr__(self):
        """Representación de la cola para debugging."""
        return f"Cola({len(self._items)} elementos)"
    
    def __str__(self):
        """Representación legible de la cola."""
        if self.is_empty():
            return "Cola vacía"
        return f"Cola con {len(self._items)} elementos: {self._items[:3]}{'...' if len(self._items) > 3 else ''}"
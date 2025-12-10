# app/structures/pila.py

"""Estructura de datos: Pila LIFO simple.

Clase Pila:
- Uso: almacenar elementos en orden LIFO (Last In First Out).
- Se utiliza para mantener el historial de préstamos por usuario.
- Métodos documentados indican valores de retorno y comportamiento en casos límite.
"""

import json
import os

# Clase Pila (LIFO): historial de préstamos por usuario
class Pila:
    """Estructura LIFO para historial de préstamos por usuario.
    
    Métodos:
    - push(item): Añade un elemento al tope de la pila.
    - pop() -> item|None: Extrae y devuelve el elemento del tope. Devuelve None si está vacía.
    - peek() -> item|None: Devuelve el elemento del tope sin quitarlo.
    - is_empty() -> bool: True si la pila está vacía.
    - __len__() -> int: Número de elementos en la pila.
    - to_list() -> list: Devuelve una lista con el préstamo más reciente primero.
    - guardar_en_archivo(ruta_archivo): Guarda la pila en un archivo JSON.
    - cargar_desde_archivo(ruta_archivo): Carga la pila desde un archivo JSON.
    - limpiar(): Vacía completamente la pila.
    """

    # Constructor: inicia la pila vacía
    def __init__(self):
        """Inicializa una pila vacía."""
        self._items = []

    # Apila un elemento arriba del todo
    def push(self, item):
        """Añade un elemento al tope de la pila.
        
        Parámetros:
        - item: cualquier objeto que se quiera apilar (ej: diccionario con ISBN y fecha).
        
        Retorna:
        - None (efecto lateral: modifica la pila).
        
        Ejemplo:
        >>> pila = Pila()
        >>> pila.push({"isbn": "123", "fecha": "2025-01-15"})
        """
        self._items.append(item)

    # Desapila y devuelve el elemento superior
    def pop(self):
        """Extrae y devuelve el elemento del tope de la pila.
        
        Retorna:
        - El elemento más recientemente añadido, o None si la pila está vacía.
        
        Ejemplo:
        >>> pila = Pila()
        >>> pila.push("elemento1")
        >>> pila.pop()
        'elemento1'
        """
        if self.is_empty():
            return None
        return self._items.pop()

    # Consulta el elemento superior sin quitarlo
    def peek(self):
        """Devuelve el elemento del tope sin quitarlo de la pila.
        
        Retorna:
        - El elemento más reciente, o None si la pila está vacía.
        
        Ejemplo:
        >>> pila = Pila()
        >>> pila.push("elemento1")
        >>> pila.peek()
        'elemento1'
        >>> len(pila)
        1
        """
        if self.is_empty():
            return None
        return self._items[-1]

    # Indica si la pila no tiene elementos
    def is_empty(self) -> bool:
        """Verifica si la pila está vacía.
        
        Retorna:
        - True si no hay elementos, False en caso contrario.
        """
        return len(self._items) == 0

    # Tamaño actual de la pila
    def __len__(self):
        """Devuelve el número de elementos en la pila.
        
        Retorna:
        - int: cantidad de elementos.
        """
        return len(self._items)

    # Copia de elementos en orden LIFO (más reciente primero)
    def to_list(self):
        """Devuelve una copia de la pila como lista (más reciente primero).
        
        Retorna:
        - list: lista con los elementos en orden inverso (LIFO).
        
        Útil para inspección o serialización sin modificar la pila.
        """
        return list(reversed(self._items))
    
    # Serializa la pila a un archivo JSON
    def guardar_en_archivo(self, ruta_archivo):
        """Guarda la pila en un archivo JSON.
        
        Parámetros:
        - ruta_archivo: str, ruta donde guardar el archivo (ej: 'data/historial_usuario123.json')
        
        Retorna:
        - None
        
        Ejemplo de uso:
        >>> pila = Pila()
        >>> pila.push({"isbn": "123", "fecha": "2025-01-15"})
        >>> pila.guardar_en_archivo("data/historial_juan.json")
        """
        try:
            # Crear el directorio si no existe
            directorio = os.path.dirname(ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
            
            # Guardar la pila en formato JSON
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, indent=2, ensure_ascii=False)
            
            print(f"Pila guardada exitosamente en {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar la pila: {e}")
    
    # Carga la pila desde un archivo JSON existente
    def cargar_desde_archivo(self, ruta_archivo):
        """Carga la pila desde un archivo JSON.
        
        Parámetros:
        - ruta_archivo: str, ruta del archivo a cargar
        
        Retorna:
        - None (modifica el estado interno de la pila)
        
        Nota: Si el archivo no existe, la pila permanece vacía.
        
        Ejemplo de uso:
        >>> pila = Pila()
        >>> pila.cargar_desde_archivo("data/historial_juan.json")
        """
        try:
            if not os.path.exists(ruta_archivo):
                print(f"Archivo {ruta_archivo} no encontrado. Iniciando con pila vacía.")
                self._items = []
                return
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self._items = json.load(f)
            
            print(f"Pila cargada exitosamente desde {ruta_archivo}. Elementos: {len(self._items)}")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}. Iniciando con pila vacía.")
            self._items = []
        except Exception as e:
            print(f"Error al cargar la pila: {e}")
            self._items = []

    # Vacía todos los elementos de la pila
    def limpiar(self):
        """Vacía completamente la pila.
        
        Retorna:
        - None
        
        Ejemplo:
        >>> pila = Pila()
        >>> pila.push("elemento")
        >>> pila.limpiar()
        >>> pila.is_empty()
        True
        """
        self._items = []
    
    def __repr__(self):
        """Representación de la pila para debugging."""
        return f"Pila({len(self._items)} elementos)"
    
    def __str__(self):
        """Representación legible de la pila."""
        if self.is_empty():
            return "Pila vacía"
        return f"Pila con {len(self._items)} elementos. Tope: {self._items[-1]}"
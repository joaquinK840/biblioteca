from app.models.libro_model import Libro
from typing import List

class Inventario:
    """
    Manages:
    - General Inventory (unsorted)
    - Inventory Ordered by ISBN (always ordered via Insertion)

    Project requirement:
    - Unsorted list for linear searches
    - Sorted list for binary searches
    """

    def __init__(self):
        self.inventario_general: List[Libro] = []
        self.inventario_ordenado: List[Libro] = []

    # ---------------------------
    # ADD BOOK
    # ---------------------------
    def agregar_libro(self, libro: Libro):
        # 1. General list → just append
        self.inventario_general.append(libro)

        # 2. Sorted list → insert via insertion
        self._insertar_ordenado_isbn(libro)

    # ---------------------------
    # ORDERED INSERTION BY ISBN (O(n))
    # ---------------------------
    def _insertar_ordenado_isbn(self, libro: Libro):
        i = 0
        while i < len(self.inventario_ordenado) and \
            self.inventario_ordenado[i].isbn < libro.isbn:
            i += 1
        self.inventario_ordenado.insert(i, libro)

    # ---------------------------
    # LINEAR SEARCH BY TITLE OR AUTHOR
    # ---------------------------
    def buscar_lineal(self, texto: str) -> List[Libro]:
        texto = texto.lower()
        return [
            libro for libro in self.inventario_general
            if texto in libro.titulo.lower() or texto in libro.autor.lower()
        ]

    # ---------------------------
    # BINARY SEARCH BY ISBN
    # ---------------------------
    def buscar_binaria(self, isbn: str):
        low = 0
        high = len(self.inventario_ordenado) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.inventario_ordenado[mid].isbn == isbn:
                return self.inventario_ordenado[mid]
            elif self.inventario_ordenado[mid].isbn < isbn:
                low = mid + 1
            else:
                high = mid - 1
        return None

    # ---------------------------
    # FOR GLOBAL REPORT WITH MERGE SORT
    # ---------------------------
    def get_libros_para_ordenar_por_valor(self):
        return list(self.inventario_general)

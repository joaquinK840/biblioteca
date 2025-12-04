from app.models.libro_model import Libro
from typing import List

class Inventario:
    """
    Maneja:
    - Inventario General (desordenado)
    - Inventario Ordenado por ISBN (siempre ordenado con Inserción)

    Requisito del proyecto:
    - Lista desordenada para búsquedas lineales
    - Lista ordenada para búsquedas binarias
    """

    def __init__(self):
        self.inventario_general: List[Libro] = []
        self.inventario_ordenado: List[Libro] = []

    # ---------------------------
    # AGREGAR LIBRO
    # ---------------------------
    def agregar_libro(self, libro: Libro):
        # 1. Lista general → solo agregar
        self.inventario_general.append(libro)

        # 2. Lista ordenada → insertar con inserción
        self._insertar_ordenado_isbn(libro)

    # ---------------------------
    # INSERCIÓN ORDENADA POR ISBN (O(n))
    # ---------------------------
    def _insertar_ordenado_isbn(self, libro: Libro):
        i = 0
        while i < len(self.inventario_ordenado) and \
            self.inventario_ordenado[i].isbn < libro.isbn:
            i += 1
        self.inventario_ordenado.insert(i, libro)

    # ---------------------------
    # BUSQUEDA LINEAL POR TÍTULO O AUTOR
    # ---------------------------
    def buscar_lineal(self, texto: str) -> List[Libro]:
        texto = texto.lower()
        return [
            libro for libro in self.inventario_general
            if texto in libro.titulo.lower() or texto in libro.autor.lower()
        ]

    # ---------------------------
    # BUSQUEDA BINARIA POR ISBN
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
    # PARA REPORTE GLOBAL CON MERGE SORT
    # ---------------------------
    def get_libros_para_ordenar_por_valor(self):
        return list(self.inventario_general)

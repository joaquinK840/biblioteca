# app/services/libro_service.py
import csv
import os
from typing import List, Optional

from app.models.libro_model import Libro
from app.utils.libros.adaptador_estanteria import adaptar_estanterias_optimas
from app.utils.libros.estanteria_backtracking import estanteria_backtracking
from app.utils.libros.estanterias_fuerzaBruta import estanterias_fuerzaBruta
from app.utils.libros.librosOrdenados import libros_ordenados_isbn
from app.utils.libros.libroSort import ordenar_libros_por_precio
from app.utils.libros.recursion_cola import peso_promedio_tail_con_libros
from app.utils.libros.recursion_pila import valor_total_recursivo_con_libros
from app.utils.libros.inventario import Inventario

CSV_PATH = "app/db/data/libros.csv"

# Servicio de libros: lectura CSV, CRUD y utilidades/algoritmos
class LibroService:

    @staticmethod
    # Lee todos los libros del CSV y retorna la lista
    def cargar_libros() -> List[Libro]:
        """Leer todos los libros desde el CSV y devolver una lista de Libro.

        Parámetros: ninguno.
        Retorna: List[Libro] (puede estar vacía).
        """
        libros = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                libros.append(Libro(**row))
        return libros

    @staticmethod
    # Sobrescribe el CSV con la lista proporcionada
    def guardar_libros(libros: List[Libro]):
        """Sobrescribir el CSV con la lista de libros dada.

        Parámetros:
        - libros: List[Libro] a guardar.
        Retorna: None (efecto lateral: escribe archivo).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["isbn", "titulo", "autor", "peso", "valor", "stock", "paginas", "editorial", "idioma"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for libro in libros:
                writer.writerow(libro.__dict__)

    @staticmethod
    # Busca un libro por su ISBN, o None si no existe
    def obtener_por_isbn(isbn: str) -> Optional[Libro]:
        """Buscar un libro por su ISBN.

        Parámetros:
        - isbn: str
        Retorna: Libro si existe, otherwise None.
        """
        for libro in LibroService.cargar_libros():
            if libro.isbn == isbn:
                return libro
        return None

    @staticmethod
    # Crea un libro si no hay duplicado de ISBN
    def crear(libro: Libro):
        """Crear un nuevo libro si no existe otro con el mismo ISBN.

        Parámetros:
        - libro: instancia Libro a crear.
        Retorna: Libro creado o None si ya existe duplicado.
        """
        libros = LibroService.cargar_libros()

        # evitar duplicados
        if any(l.isbn == libro.isbn for l in libros):
            return None

        libros.append(libro)
        LibroService.guardar_libros(libros)
        return libro

    @staticmethod
    # Actualiza el libro con ese ISBN usando los datos dados
    def actualizar(isbn: str, data: Libro):
        """Actualizar los datos de un libro identificado por ISBN.

        Parámetros:
        - isbn: str del libro a actualizar.
        - data: instancia Libro con nuevos datos.
        Retorna: Libro actualizado o None si no existe.
        """
        libros = LibroService.cargar_libros()
        for i, l in enumerate(libros):
            if l.isbn == isbn:
                libros[i] = data
                LibroService.guardar_libros(libros)
                return data
        return None

    @staticmethod
    # Elimina por ISBN; retorna True si lo encontró y borró
    def eliminar(isbn: str):
        """Eliminar un libro por ISBN.

        Parámetros:
        - isbn: str
        Retorna: True si se eliminó, False si no se encontró.
        """
        libros = LibroService.cargar_libros()
        nuevos = [l for l in libros if l.isbn != isbn]
        if len(nuevos) == len(libros):
            return False
        LibroService.guardar_libros(nuevos)
        return True

    @staticmethod
    # Devuelve la lista ordenada por ISBN (insertion sort)
    def ordernar_por_isbn() -> List[Libro]:
        """Devolver lista de libros ordenada por ISBN (insertion sort).

        Parámetros: ninguno.
        Retorna: List[Libro] ordenada ascendentemente por ISBN.
        """
        libros = LibroService.cargar_libros()
        ordedanados = libros_ordenados_isbn(libros)
        return ordedanados
    
    @staticmethod
    # Devuelve la lista ordenada por precio/valor (merge sort)
    def obtener_por_precio():
        """Devolver lista de libros ordenada por precio/valor (merge sort).

        Parámetros: ninguno.
        Retorna: lista ordenada por atributo `valor`.
        """
        libros= LibroService.cargar_libros()
        ordenados=ordenar_libros_por_precio(libros)
        return ordenados

    @staticmethod
    # Búsqueda lineal por título/autor en inventario general
    def buscar_lineal(texto: str) -> List[Libro]:
        """Buscar por título o autor sobre el inventario general (lista desordenada).

        Parámetros:
        - texto: str a buscar (case-insensitive) en título o autor.
        Retorna:
        - List[Libro] con coincidencias.
        """
        # Cargar inventario y realizar búsqueda lineal
        

        inventario = Inventario()
        libros = LibroService.cargar_libros()
        for l in libros:
            inventario.agregar_libro(l)
        return inventario.buscar_lineal(texto)
    
    @staticmethod
    # Detecta combinaciones deficientes por fuerza bruta (peso>8)
    def estanteria_deficiente():
        """Detectar combinaciones deficientes por fuerza bruta (peso>8).

        Parámetros: ninguno.
        Retorna: lista de diccionarios con combinaciones que superan el umbral.
        """
        libros = LibroService.cargar_libros()
        deficientes = estanterias_fuerzaBruta(libros)
        return deficientes
    


    @staticmethod
    # Calcula estanterías óptimas (backtracking) y adapta al schema
    def estanteria_optima():
        """Calcular estanterías óptimas mediante backtracking y adaptar el resultado.

        Parámetros: ninguno.
        Retorna: EstanteriasOptimasResponse (schema) con la asignación óptima.
        """
        libros = LibroService.cargar_libros()
        salida = estanteria_backtracking(libros)
        return adaptar_estanterias_optimas(salida)
    
    @staticmethod
    # Suma de valor de libros de un autor (recursión tipo pila)
    def valor_total_por_autor(autor: str):
        """Calcular el valor total de libros de un autor usando recursión (pila).

        Parámetros:
        - autor: nombre del autor (str).
        Retorna: dict {'valor_total': float, 'libros': [titulos]} o None si no hay libros.
        """
        libros = [l for l in LibroService.cargar_libros() if l.autor == autor]
        if not libros:
            return None

        total, titulos = valor_total_recursivo_con_libros(libros, len(libros) - 1)
        return {"valor_total": total, "libros": titulos}


    @staticmethod
    # Promedio de peso de libros de un autor (tail recursion)
    def peso_promedio_por_autor(autor: str):
        """Calcular el peso promedio de libros de un autor usando recursión tail.

        Parámetros:
        - autor: str
        Retorna: dict {'peso_promedio': float, 'libros': [titulos]} o None si no hay libros.
        """
        libros = [l for l in LibroService.cargar_libros() if l.autor == autor]
        if not libros:
            return None

        promedio, titulos = peso_promedio_tail_con_libros(libros)
        return {"peso_promedio": promedio, "libros": titulos}




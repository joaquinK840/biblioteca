import csv
from app.models.libro_model import Libro
from typing import List, Optional
import os
from app.utils.libros.librosOrdenados import libros_ordenados_isbn
from app.utils.libros.libroSort import ordenar_libros_por_precio
from app.utils.libros.estanterias_fuerzaBruta import estanterias_fuerzaBruta
from app.utils.libros.estanteria_backtracking import estanteria_backtracking
CSV_PATH = "app/db/data/libros.csv"

class LibroService:

    @staticmethod
    def cargar_libros() -> List[Libro]:
        libros = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                libros.append(Libro(**row))
        return libros

    @staticmethod
    def guardar_libros(libros: List[Libro]):
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["isbn", "titulo", "autor", "peso", "valor", "stock", "paginas", "editorial", "idioma"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for libro in libros:
                writer.writerow(libro.__dict__)

    @staticmethod
    def obtener_por_isbn(isbn: str) -> Optional[Libro]:
        for libro in LibroService.cargar_libros():
            if libro.isbn == isbn:
                return libro
        return None

    @staticmethod
    def crear(libro: Libro):
        libros = LibroService.cargar_libros()

        # evitar duplicados
        if any(l.isbn == libro.isbn for l in libros):
            return None

        libros.append(libro)
        LibroService.guardar_libros(libros)
        return libro

    @staticmethod
    def actualizar(isbn: str, data: Libro):
        libros = LibroService.cargar_libros()
        for i, l in enumerate(libros):
            if l.isbn == isbn:
                libros[i] = data
                LibroService.guardar_libros(libros)
                return data
        return None

    @staticmethod
    def eliminar(isbn: str):
        libros = LibroService.cargar_libros()
        nuevos = [l for l in libros if l.isbn != isbn]
        if len(nuevos) == len(libros):
            return False
        LibroService.guardar_libros(nuevos)
        return True

    @staticmethod
    def ordernar_por_isbn() -> List[Libro]:
        libros = LibroService.cargar_libros()
        ordedanados = libros_ordenados_isbn(libros)
        return ordedanados
    
    @staticmethod
    def obtener_por_precio():
        libros= LibroService.cargar_libros()
        ordenados=ordenar_libros_por_precio(libros)
        return ordenados
    
    @staticmethod
    def estanteria_deficiente():
        libros = LibroService.cargar_libros()
        deficientes = estanterias_fuerzaBruta(libros)
        return deficientes
    
    @staticmethod
    def estanteria_optima():
        libros = LibroService.cargar_libros()
        optimas = estanteria_backtracking(libros)  # Aquí iría la llamada al algoritmo óptimo
        return optimas

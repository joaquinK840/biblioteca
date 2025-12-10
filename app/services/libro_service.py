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

# Book service: CSV IO, CRUD, and utilities/algorithms
class LibroService:

    @staticmethod
    # Read all books from CSV and return the list
    def cargar_libros() -> List[Libro]:
        """Read all books from the CSV and return a list of `Libro`.

        Parameters: none.
        Returns: List[Libro] (may be empty).
        """
        libros = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                libros.append(Libro(**row))
        return libros

    @staticmethod
    # Overwrite the CSV with the provided list
    def guardar_libros(libros: List[Libro]):
        """Overwrite the CSV with the provided list of books.

        Parameters:
        - libros: List[Libro] to persist.
        Returns: None (side effect: writes file).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["isbn", "titulo", "autor", "peso", "valor", "stock", "paginas", "editorial", "idioma"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for libro in libros:
                writer.writerow(libro.__dict__)

    @staticmethod
    # Find a book by its ISBN, or None if it doesn't exist
    def obtener_por_isbn(isbn: str) -> Optional[Libro]:
        """Find a book by its ISBN.

        Parameters:
        - isbn: str
        Returns: Libro if found, otherwise None.
        """
        for libro in LibroService.cargar_libros():
            if libro.isbn == isbn:
                return libro
        return None

    @staticmethod
    # Create a book if there's no duplicate ISBN
    def crear(libro: Libro):
        """Create a new book if there is no other with the same ISBN.

        Parameters:
        - libro: Libro instance to create.
        Returns: Created Libro or None if a duplicate already exists.
        """
        libros = LibroService.cargar_libros()

        # avoid duplicates
        if any(l.isbn == libro.isbn for l in libros):
            return None

        libros.append(libro)
        LibroService.guardar_libros(libros)
        return libro

    @staticmethod
    # Update the book with that ISBN using provided data
    def actualizar(isbn: str, data: Libro):
        """Update the data of a book identified by ISBN.

        Parameters:
        - isbn: str of the book to update.
        - data: Libro instance with new data.
        Returns: Updated Libro or None if it does not exist.
        """
        libros = LibroService.cargar_libros()
        for i, l in enumerate(libros):
            if l.isbn == isbn:
                libros[i] = data
                LibroService.guardar_libros(libros)
                return data
        return None

    @staticmethod
    # Delete by ISBN; returns True if found and removed
    def eliminar(isbn: str):
        """Delete a book by ISBN.

        Parameters:
        - isbn: str
        Returns: True if deleted, False if not found.
        """
        libros = LibroService.cargar_libros()
        nuevos = [l for l in libros if l.isbn != isbn]
        if len(nuevos) == len(libros):
            return False
        LibroService.guardar_libros(nuevos)
        return True

    @staticmethod
    # Return the list ordered by ISBN (Insertion Sort)
    def ordernar_por_isbn() -> List[Libro]:
        """Return list of books sorted by ISBN (insertion sort).

        Parameters: none.
        Returns: List[Libro] sorted ascending by ISBN.
        """
        libros = LibroService.cargar_libros()
        ordedanados = libros_ordenados_isbn(libros)
        return ordedanados
    
    @staticmethod
    # Return the list ordered by price/value (Merge Sort)
    def obtener_por_precio():
        """Return list of books sorted by price/value (merge sort).

        Parameters: none.
        Returns: list sorted by attribute `valor`.
        """
        libros= LibroService.cargar_libros()
        ordenados=ordenar_libros_por_precio(libros)
        return ordenados

    @staticmethod
    # Linear search by title/author in general inventory
    def buscar_lineal(texto: str) -> List[Libro]:
        """Search by title or author over the general inventory (unsorted list).

        Parameters:
        - texto: str to search (case-insensitive) in title or author.
        Returns:
        - List[Libro] with matches.
        """
        # Load inventory and perform linear search
        

        inventario = Inventario()
        libros = LibroService.cargar_libros()
        for l in libros:
            inventario.agregar_libro(l)
        return inventario.buscar_lineal(texto)
    
    @staticmethod
    # Detect deficient combinations via brute force (weight > 8)
    def estanteria_deficiente():
        """Detect deficient combinations via brute force (weight > 8).

        Parameters: none.
        Returns: list of dictionaries with combinations that exceed the threshold.
        """
        libros = LibroService.cargar_libros()
        deficientes = estanterias_fuerzaBruta(libros)
        return deficientes
    


    @staticmethod
    # Compute optimal shelves (backtracking) and adapt to schema
    def estanteria_optima():
        """Compute optimal shelves via backtracking and adapt the result.

        Parameters: none.
        Returns: EstanteriasOptimasResponse (schema) with the optimal assignment.
        """
        libros = LibroService.cargar_libros()
        salida = estanteria_backtracking(libros)
        return adaptar_estanterias_optimas(salida)
    
    @staticmethod
    # Sum of book values for an author (stack-style recursion)
    def valor_total_por_autor(autor: str):
        """Calculate the total value of an author's books using recursion (stack-style).

        Parameters:
        - autor: author name (str).
        Returns: dict {'valor_total': float, 'libros': [titles]} or None if no books.
        """
        libros = [l for l in LibroService.cargar_libros() if l.autor == autor]
        if not libros:
            return None

        total, titulos = valor_total_recursivo_con_libros(libros, len(libros) - 1)
        return {"valor_total": total, "libros": titulos}


    @staticmethod
    # Average weight of books for an author (tail recursion)
    def peso_promedio_por_autor(autor: str):
        """Calculate the average weight of an author's books using tail recursion.

        Parameters:
        - autor: str
        Returns: dict {'peso_promedio': float, 'libros': [titles]} or None if no books.
        """
        libros = [l for l in LibroService.cargar_libros() if l.autor == autor]
        if not libros:
            return None

        promedio, titulos = peso_promedio_tail_con_libros(libros)
        return {"peso_promedio": promedio, "libros": titulos}




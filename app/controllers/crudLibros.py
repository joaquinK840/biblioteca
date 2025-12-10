# app/controllers/crudLibros.py
from fastapi import HTTPException

from app.models.libro_model import Libro
from app.schemas.libro_schema import LibroCreate, LibroOut, LibroUpdate
from app.services.libro_service import LibroService


# Books controller: orchestrates LibroService calls and validates responses
class LibroController:

    @staticmethod
    # List all available books
    def listar_libros():
        """List all books.

        Parameters: none.
        Returns: List[Libro].
        """
        return LibroService.cargar_libros()

    @staticmethod
    # Get a book by ISBN or raise 404 if not found
    def obtener_libro(isbn: str):
        """Get a book by ISBN.

        Parameters:
        - isbn: str
        Returns: Libro if it exists.
        Raises: HTTPException 404 if not found.
        """
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            raise HTTPException(status_code=404, detail="Book not found")
        return libro

    @staticmethod
    # Create a new book from the input schema
    def crear_libro(data: LibroCreate):
        """Create a new book.

        Parameters:
        - data: LibroCreate
        Returns: Created Libro.
        Raises: HTTPException 400 if the ISBN already exists.
        """
        libro = Libro(**data.dict())
        nuevo = LibroService.crear(libro)
        if not nuevo:
            raise HTTPException(status_code=400, detail="ISBN already exists")
        return nuevo

    @staticmethod
    # Update a book by ISBN using schema data
    def actualizar_libro(isbn: str, data: LibroUpdate):
        """Update a book by ISBN.

        Parameters:
        - isbn: str
        - data: LibroUpdate
        Returns: Updated Libro.
        Raises: HTTPException 404 if not found.
        """
        libro_actualizado = Libro(
            isbn=isbn,
            **data.dict()
        )
        actualizado = LibroService.actualizar(isbn, libro_actualizado)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Book not found")
        return actualizado

    @staticmethod
    # Delete a book by ISBN; return success message
    def eliminar_libro(isbn: str):
        """Delete a book by ISBN.

        Parameters:
        - isbn: str
        Returns: dict with success message.
        Raises: HTTPException 404 if not found.
        """
        eliminado = LibroService.eliminar(isbn)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "Book deleted"}
    
    @staticmethod
    # Return books sorted by ISBN (Insertion Sort)
    def libros_ordenados_isbn():
        """Return books sorted by ISBN.

        Parameters: none.
        Returns: sorted list or HTTPException 404 if no books.
        """
        libros = LibroService.ordernar_por_isbn()
        if not libros:
            raise HTTPException(status_code=404, detail="No books to sort")
        return libros
    
    @staticmethod
    # Return books sorted by price/value (Merge Sort)
    def libros_ordenados_precio():
        """Return books sorted by price/value.

        Parameters: none.
        Returns: sorted list or HTTPException 404 if no books.
        """
        libros = LibroService.obtener_por_precio()
        if not libros:
            raise HTTPException(status_code=404, detail="No books to sort")
        return libros
    
    @staticmethod
    # Return deficient combinations (brute force)
    def estanteria_deficiente():
        """Detect deficient combinations (brute force).

        Parameters: none.
        Returns: list of combinations or HTTPException 404 if no data.
        """
        libros = LibroService.estanteria_deficiente()
        if not libros:
            raise HTTPException(status_code=404, detail="No books to organize")
        return libros
    
    @staticmethod
    # Return optimal shelves (backtracking) adapted to schema
    def estanteria_optima():    
        """Compute and return optimal shelves (backtracking).

        Parameters: none.
        Returns: EstanteriasOptimasResponse or HTTPException 404 if no data.
        """
        libros = LibroService.estanteria_optima()
        if not libros:
            raise HTTPException(status_code=404, detail="No books to organize")
        return libros
    
    @staticmethod
    # Sum of book values by author (stack-style recursion)
    def valor_total_autor(autor: str):
        """Calculate total value of books by an author.

        Parameters:
        - autor: str
        Returns: dict with 'autor', 'valor_total' and 'libros' or HTTPException 404 if no matches.
        """
        resultado = LibroService.valor_total_por_autor(autor)
        if resultado is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return {"autor": autor, **resultado}

    @staticmethod
    # Average weight of books by author (tail recursion)
    def peso_promedio_autor(autor: str):
        """Calculate average weight of books by an author.

        Parameters:
        - autor: str
        Returns: dict with 'autor', 'peso_promedio' and 'libros' or HTTPException 404 if no matches.
        """
        resultado = LibroService.peso_promedio_por_autor(autor)
        if resultado is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return {"autor": autor, **resultado}

    @staticmethod
    # Linear search of books by title/author in general inventory
    def buscar_lineal(texto: str):
        """Linear search by title or author in general inventory.

        Parameters:
        - texto: str (query)
        Returns: List[Libro] or HTTPException 404 if no matches.
        """
        resultados = LibroService.buscar_lineal(texto)
        if not resultados:
            raise HTTPException(status_code=404, detail="No matches for the search")
        return resultados

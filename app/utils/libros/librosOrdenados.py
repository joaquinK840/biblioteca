
def libros_ordenados_isbn(libros):
    """
    Sorting by ISBN using Insertion Sort.

Function:
- libros_ordenados_isbn(libros)
  - Receives:
    * libros: list of objects with `isbn` attribute.
  - Returns:
    * new list sorted ascending by `isbn`.
  - Implementation:
    * Iterative insertion building a new sorted list.
    
    Sorts the list of books by `isbn` using the Insertion Sort algorithm.

    The function receives a list of `Libro` objects and returns a
    new list sorted by `isbn` in ascending order.
    """
    # List we will build already sorted
    lista_ordenada = []

    for libro_a_insertar in libros:
        # Convert ISBN to string for safe comparisons
        isbn_a_insertar = str(libro_a_insertar.isbn)

        # Start by finding the correct position from the end
        indice = len(lista_ordenada) - 1

        # Shift left while current ISBN is less than the ISBN in lista_ordenada
        while indice >= 0 and str(lista_ordenada[indice].isbn) > isbn_a_insertar:
            indice -= 1
            

        # Insert the book in the correct position (indice+1)
        lista_ordenada.insert(indice + 1, libro_a_insertar)

    return lista_ordenada
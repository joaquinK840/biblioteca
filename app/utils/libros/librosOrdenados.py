
def libros_ordenados_isbn(libros):
    """
    Ordenamiento por ISBN usando Insertion Sort.

Función:
- libros_ordenados_isbn(libros)
  - Recibe:
    * libros: lista de objetos con atributo `isbn`.
  - Devuelve:
    * nueva lista ordenada ascendentemente por `isbn`.
  - Implementación:
    * Inserción iterativa construyendo una lista ordenada nueva.
    
    Ordena la lista de libros por `isbn` usando el algoritmo
    de Ordenamiento por Inserción (Insertion Sort).

    La función recibe una lista de objetos `Libro` y devuelve una
    nueva lista ordenada por `isbn` en orden ascendente. Se usan
    nombres de variables en español claros para mejorar la lectura.
    """
    # Lista que iremos construyendo ya ordenada
    lista_ordenada = []

    for libro_a_insertar in libros:
        # Convertimos el ISBN a cadena para comparaciones seguras
        isbn_a_insertar = str(libro_a_insertar.isbn)

        # Empezamos buscando la posición correcta desde el final
        indice = len(lista_ordenada) - 1

        # Desplazamos hacia la izquierda mientras el ISBN actual sea
        # menor que el ISBN del elemento en lista_ordenada
        while indice >= 0 and str(lista_ordenada[indice].isbn) > isbn_a_insertar:
            indice -= 1
            

        # Insertamos el libro en la posición correcta (indice+1)
        lista_ordenada.insert(indice + 1, libro_a_insertar)

    return lista_ordenada
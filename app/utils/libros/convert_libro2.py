
# app/utils/libros/convert_libro2.py

from app.models.libro2_model import Libro2


def convertir_a_libros2(lista_libros):
    """Convert book-like objects to `Libro2` instances.

Function:
- convertir_a_libros2(lista_libros)
  - Receives:
    * lista_libros: iterable of objects with attributes: isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma
  - Returns:
    * list of `Libro2` instances with mapped fields.
  - Note:
    * Does not validate types; assumes attributes exist on input objects.
"""
    nueva = []
    for l in lista_libros:
        nueva.append(
            Libro2(
                isbn=l.isbn,
                titulo=l.titulo,
                autor=l.autor,
                peso=l.peso,
                valor=l.valor,
                stock=l.stock,
                paginas=l.paginas,
                editorial=l.editorial,
                idioma=l.idioma
            )
        )
    return nueva

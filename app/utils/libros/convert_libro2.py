
# app/utils/libros/convert_libro2.py

from app.models.libro2_model import Libro2


def convertir_a_libros2(lista_libros):
    """Conversión de objetos libro a instancias de Libro2.

Función:
- convertir_a_libros2(lista_libros)
  - Recibe:
    * lista_libros: iterable de objetos que contienen atributos: isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma
  - Devuelve:
    * lista de instancias Libro2 con los campos mapeados.
  - Nota:
    * No valida tipos; asume que los atributos existen en los objetos de entrada.
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

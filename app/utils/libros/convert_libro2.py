# app/utils/libros/convert_libro2.py

from app.models.libro2_model import Libro2

def convertir_a_libros2(lista_libros):
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

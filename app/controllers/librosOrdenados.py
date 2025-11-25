def lista_ordenada_isbn(libros):
    

    return sorted(libros, key=lambda libro: libro.isbn)

def lista_ordenada_precio(libros):
    return sorted(libros, key=lambda libro: libro.precio)
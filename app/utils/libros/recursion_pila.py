def valor_total_recursivo_con_libros(libros, index):
    """Recursión de pila: suma los valores y devuelve la lista de títulos."""
    if index < 0:
        return 0, []
    
    subtotal, titulos = valor_total_recursivo_con_libros(libros, index - 1)
    titulos.append(libros[index].titulo)
    return subtotal + float(libros[index].valor), titulos

def peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None):
    """Recursión de cola: calcula peso promedio mostrando los libros y traza por consola."""
    if titulos is None:
        titulos = []

    if index == len(libros):
        promedio = acumulado / contador if contador > 0 else 0
        return promedio, titulos

    titulos.append(libros[index].titulo)
    print(f"[TAIL] index={index}, acumulado={acumulado}, contador={contador}, libro={libros[index].titulo}")
    return peso_promedio_tail_con_libros(
        libros,
        index + 1,
        acumulado + float(libros[index].peso),
        contador + 1,
        titulos
    )

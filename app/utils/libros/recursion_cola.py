# Average weight using tail recursion
def peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None):
    """Tail recursion to calculate average weight of books.

Function:
- peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None)
  - Receives:
    * libros: list of objects with 'titulo' and 'peso' attributes.
    * index: current index (starts at 0).
    * acumulado: accumulated sum of weights (float).
    * contador: number of processed elements (int).
    * titulos: accumulated list of titles (internal; initialized if None).
  - Returns:
    * (promedio: float, titulos: list[str])
      - promedio: average weight (0 if contador==0).
      - titulos: list of titles in traversal order.
  - Behavior:
    * Prints traces to console on each call for debugging.
    * Performs tail recursion; Python has no tail recursion optimization,
      so very long lists may overflow the call stack.
"""
    # Initialize titles list if not provided
    if titulos is None:
        titulos = []

    # Base case: reached end of list
    if index == len(libros):
        promedio = acumulado / contador if contador > 0 else 0
        return promedio, titulos

    # Constant step before recursion (characteristic of tail recursion)
    titulos.append(libros[index].titulo)
    print(f"[TAIL] index={index}, acumulado={acumulado}, contador={contador}, libro={libros[index].titulo}")
    return peso_promedio_tail_con_libros(
        libros,
        index + 1,
        acumulado + float(libros[index].peso),
        contador + 1,
        titulos
    )

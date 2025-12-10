# Sum of values using stack-style recursion (post-order)
def valor_total_recursivo_con_libros(libros, index):
    """Stack-style recursion (post-order) to process book lists.

Function:
- valor_total_recursivo_con_libros(libros, index)
  - Receives: 
    * libros: list of objects with at least 'titulo' and 'valor' attributes.
    * index: integer indicating current position (usually called with len(libros)-1).
  - Returns:
    * (subtotal: float, titulos: list[str])
      - subtotal: sum of `valor` fields from 0 to index inclusive.
      - titulos: list of titles accumulated in recursive extraction order.
  - Behavior:
    * Works recursively descending until index < 0 as base case.
    * Converts `valor` to float when summing.
"""
    # Base case: negative index → no more elements
    if index < 0:
        return 0, []
    
    # Recurse first, then process the current element (post-order)
    subtotal, titulos = valor_total_recursivo_con_libros(libros, index - 1)
    titulos.append(libros[index].titulo)
    return subtotal + float(libros[index].valor), titulos

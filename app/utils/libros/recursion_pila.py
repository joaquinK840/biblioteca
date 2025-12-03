
def valor_total_recursivo_con_libros(libros, index):
    """Recursión tipo pila (post-order) para procesar listas de libros.

Función:
- valor_total_recursivo_con_libros(libros, index)
  - Recibe: 
    * libros: lista de objetos con atributos al menos 'titulo' y 'valor'.
    * index: índice entero que indica la posición actual (se suele llamar con len(libros)-1).
  - Devuelve:
    * (subtotal: float, titulos: list[str])
      - subtotal: suma de los campos `valor` desde 0 hasta index inclusive.
      - titulos: lista de títulos acumulada en orden de extracción recursiva.
  - Comportamiento:
    * Funciona recursivamente descendiendo hasta index < 0 como caso base.
    * Convierte `valor` a float al sumar.
"""
    if index < 0:
        return 0, []
    
    subtotal, titulos = valor_total_recursivo_con_libros(libros, index - 1)
    titulos.append(libros[index].titulo)
    return subtotal + float(libros[index].valor), titulos

# Promedio de peso con recursión de cola (tail recursion)
def peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None):
    """Recursión de cola (tail recursion) para calcular promedio de peso de libros.

Función:
- peso_promedio_tail_con_libros(libros, index=0, acumulado=0, contador=0, titulos=None)
  - Recibe:
    * libros: lista de objetos con atributos 'titulo' y 'peso'.
    * index: índice actual (inicia en 0).
    * acumulado: suma acumulada de pesos (float).
    * contador: número de elementos procesados (int).
    * titulos: lista acumulada de títulos (interna; se inicializa si es None).
  - Devuelve:
    * (promedio: float, titulos: list[str])
      - promedio: promedio de peso (0 si contador==0).
      - titulos: lista de títulos en orden de recorrido.
  - Comportamiento:
    * Imprime trazas por consola en cada llamada para debugging.
    * Realiza tail recursion; en Python no hay optimización de tail recursion,
      por lo que para listas muy largas puede desbordar la pila.
"""
    # Inicializa lista de títulos si no se pasa
    if titulos is None:
        titulos = []

    # Caso base: llegamos al final de la lista
    if index == len(libros):
        promedio = acumulado / contador if contador > 0 else 0
        return promedio, titulos

    # Paso constante antes de la recursión (característico de tail recursion)
    titulos.append(libros[index].titulo)
    print(f"[TAIL] index={index}, acumulado={acumulado}, contador={contador}, libro={libros[index].titulo}")
    return peso_promedio_tail_con_libros(
        libros,
        index + 1,
        acumulado + float(libros[index].peso),
        contador + 1,
        titulos
    )

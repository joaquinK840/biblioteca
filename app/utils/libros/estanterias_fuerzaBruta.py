
def estanterias_fuerzaBruta(libros):
    """Búsqueda por fuerza bruta de combinaciones de 4 libros cuyo peso supera un umbral.

Función:
- estanterias_fuerzaBruta(libros)
  - Recibe:
    * libros: lista de objetos con atributo `peso` y `titulo`.
  - Devuelve:
    * lista de diccionarios con claves:
      - "libros": lista de títulos de la combinación
      - "peso_total": suma de los pesos de los 4 libros
  - Comportamiento:
    * Recorre todas las combinaciones de 4 elementos sin repetición (O(n^4)).
    * Añade a resultado las combinaciones cuyo peso_total > 8.
"""
    resultado = []
    n = len(libros)

    # Recorremos todas las combinaciones posibles de 4 libros sin repetir
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):

                    # Obtener los 4 libros
                    combo = [libros[i], libros[j], libros[k], libros[l]]

                    # Calcular el peso total
                    peso_total = (
                        combo[0].peso +
                        combo[1].peso +
                        combo[2].peso +
                        combo[3].peso
                    )

                    # Verificar si superan el umbral de riesgo
                    if peso_total > 8:
                        resultado.append({
                            "libros": [libro.titulo for libro in combo],
                            "peso_total": peso_total
                        })

    return resultado

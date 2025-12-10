
def estanterias_fuerzaBruta(libros):
        """Brute-force search for 4-book combinations whose total weight exceeds a threshold.

Function:
- estanterias_fuerzaBruta(libros)
    - Receives:
        * libros: list of objects with `peso` and `titulo` attributes.
    - Returns:
        * list of dictionaries with keys:
            - "libros": list of titles in the combination
            - "peso_total": sum of the weights of the 4 books
    - Behavior:
        * Iterates all 4-element combinations without repetition (O(n^4)).
        * Adds to result the combinations whose peso_total > 8.
"""
    resultado = []
    n = len(libros)

    # Iterate all possible 4-book combinations without repetition
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):

                    # Get the 4 books
                    combo = [libros[i], libros[j], libros[k], libros[l]]

                    # Calculate total weight
                    peso_total = (
                        combo[0].peso +
                        combo[1].peso +
                        combo[2].peso +
                        combo[3].peso
                    )

                    # Check if they exceed the risk threshold
                    if peso_total > 8:
                        resultado.append({
                            "libros": [libro.titulo for libro in combo],
                            "peso_total": peso_total
                        })

    return resultado

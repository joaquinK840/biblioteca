from itertools import combinations

PESO_MAX = 8  # 8 Kg maximum allowed


# ============================================================
#   1) BRUTE FORCE - Combinations of 4 books exceeding 8 kg
# ============================================================

def combinaciones_peligrosas(libros):
    """
    Returns ALL possible combinations of 4 books
    whose total weight exceeds 8 kg (true brute force).
    """

    peligrosas = []

    # all combinations of 4 books
    for combo in combinations(libros, 4):
        peso_total = sum([libro.peso for libro in combo])

        if peso_total > PESO_MAX:
            peligrosas.append({
                "libros": combo,
                "peso_total": peso_total
            })

    return peligrosas


# ============================================================
#   2) BACKTRACKING - Maximize VALUE without exceeding 8 kg
# ============================================================

def estanteria_optima(libros):
    """
    Uses backtracking to find the combination of books
    that yields the HIGHEST possible value without exceeding 8 kg.
    """

    mejor_valor = 0
    mejor_combinacion = []
    exploracion = []  # list of visited states (to show the reasoning)

    def backtracking(indice, peso_actual, valor_actual, seleccion):
        nonlocal mejor_valor, mejor_combinacion

        # Track exploration (OPTIONAL: you can print it)
        exploracion.append({
            "indice": indice,
            "peso": peso_actual,
            "valor": valor_actual,
            "seleccion": [libro.titulo for libro in seleccion]
        })

        # Base case: weight exceeded → backtrack
        if peso_actual > PESO_MAX:
            return

        # Base case: no more books
        if indice == len(libros):
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_combinacion = seleccion.copy()
            return

        libro = libros[indice]

        # -----------------------
        # 1. Include current book
        # -----------------------
        backtracking(
            indice + 1,
            peso_actual + libro.peso,
            valor_actual + libro.valor,
            seleccion + [libro]
        )

        # -----------------------
        # 2. Exclude current book
        # -----------------------
        backtracking(
            indice + 1,
            peso_actual,
            valor_actual,
            seleccion
        )

    # Call algorithm starting at index 0
    backtracking(0, 0, 0, [])

    return {
        "mejor_valor": mejor_valor,
        "mejor_combinacion": mejor_combinacion,
        "exploracion": exploracion
    }

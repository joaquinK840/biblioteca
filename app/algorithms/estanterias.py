from itertools import combinations

PESO_MAX = 8  # 8 Kg máximo permitido


# ============================================================
#   1) FUERZA BRUTA - Combinaciones de 4 libros que superen 8kg
# ============================================================

def combinaciones_peligrosas(libros):
    """
    Retorna TODAS las combinaciones posibles de 4 libros 
    cuyo peso total supera 8 Kg (fuerza bruta real).
    """

    peligrosas = []

    # todas las combinaciones de 4 libros
    for combo in combinations(libros, 4):
        peso_total = sum([libro.peso for libro in combo])

        if peso_total > PESO_MAX:
            peligrosas.append({
                "libros": combo,
                "peso_total": peso_total
            })

    return peligrosas


# ============================================================
#   2) BACKTRACKING - Maximizar VALOR sin exceder 8 Kg
# ============================================================

def estanteria_optima(libros):
    """
    Usa backtracking para encontrar la combinación de libros
    que produce el MAYOR valor posible sin exceder 8 Kg.
    """

    mejor_valor = 0
    mejor_combinacion = []
    exploracion = []  # lista de estados visitados (para mostrar la lógica)

    def backtracking(indice, peso_actual, valor_actual, seleccion):
        nonlocal mejor_valor, mejor_combinacion

        # Registrar exploración (OPCIONAL: puedes imprimirlo)
        exploracion.append({
            "indice": indice,
            "peso": peso_actual,
            "valor": valor_actual,
            "seleccion": [libro.titulo for libro in seleccion]
        })

        # Caso base: peso excedido → retroceder
        if peso_actual > PESO_MAX:
            return

        # Caso base: sin más libros
        if indice == len(libros):
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_combinacion = seleccion.copy()
            return

        libro = libros[indice]

        # -----------------------
        # 1. Incluir libro actual
        # -----------------------
        backtracking(
            indice + 1,
            peso_actual + libro.peso,
            valor_actual + libro.valor,
            seleccion + [libro]
        )

        # -----------------------
        # 2. Excluir libro actual
        # -----------------------
        backtracking(
            indice + 1,
            peso_actual,
            valor_actual,
            seleccion
        )

    # Llamar algoritmo iniciando en 0
    backtracking(0, 0, 0, [])

    return {
        "mejor_valor": mejor_valor,
        "mejor_combinacion": mejor_combinacion,
        "exploracion": exploracion
    }

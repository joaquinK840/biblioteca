def estanteria_backtracking(libros, peso_max=8.0):
    def backtrack(indice, peso_actual, valor_actual, combinacion):
        nonlocal mejor_valor, mejor_comb

        # Si ya excede peso, cortar rama
        if peso_actual > peso_max:
            return
        
        # Si llegamos al final, evaluar solución
        if indice == n:
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_comb = combinacion.copy()
            return

        libro = libros[indice]

        # OPCIÓN 1: Incluir libro si no pasa el límite
        if peso_actual + libro.peso <= peso_max:
            combinacion.append(libro)
            backtrack(
                indice + 1,
                peso_actual + libro.peso,
                valor_actual + libro.valor,
                combinacion
            )
            combinacion.pop()

        # OPCIÓN 2: NO incluir libro
        backtrack(indice + 1, peso_actual, valor_actual, combinacion)

    mejor_valor = 0
    mejor_comb = []
    n = len(libros)
    # Llamar al backtracking
    backtrack(0, 0, 0, [])

    return {
        "libros": [l.titulo for l in mejor_comb],
        "peso_total": sum(l.peso for l in mejor_comb),
        "precio_total": sum(l.valor for l in mejor_comb)
    }

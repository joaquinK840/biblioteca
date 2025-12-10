
# Optimal shelf selection (backtracking with pruning)
def estanteria_backtracking(libros, peso_max=8.0):
    """Backtracking algorithm to assign shelves maximizing value without exceeding weight.

    Function:
    - estanteria_backtracking(libros, peso_max=8.0)
        - Receives:
            * libros: list of objects with at least 'titulo', 'peso', 'valor'.
            * peso_max: weight limit per shelf (float).
        - Returns:
            * dict {"resultado": [ { "estanteria": int, "libros": [titles], "peso_total": float, "precio_total": float }, ... ] }
        - Side effects:
            * Adds/sets attribute `estanteria` on each book object to indicate assigned shelf (0 = unassigned).
        - Note:
            * Attempts to pack books into shelves maximizing value without exceeding `peso_max`, with up to 4 books per shelf.
    """
    # Step 1: initialize all books with no shelf assigned
    for libro in libros:
        setattr(libro, "estanteria", 0)

    # Step 2: estimate number of shelves needed (max 4 per shelf)
    total_libros = len(libros)
    num_estanterias = (total_libros // 4) + 1

    resultado_final = []

    # Step 3: iterate over shelves and solve via backtracking
    for num_est in range(1, num_estanterias + 1):
        # Filtrar solo libros sin estantería asignada
        disponibles = [l for l in libros if l.estanteria == 0]

        # Si ya no quedan libros → salir
        if not disponibles:
            break

        # ======== BACKTRACKING PARA ESTA ESTANTERÍA =========
        mejor_valor = 0
        mejor_comb = []

        n = len(disponibles)

        # Backtracking: decide per book to take it or not, with constraints
        def backtrack(indice, peso_actual, valor_actual, seleccion):
            nonlocal mejor_valor, mejor_comb

            # Prune: no more than 4 books per shelf
            if len(seleccion) > 4:
                return

            # Prune: do not exceed max weight
            if peso_actual > peso_max:
                return

            # fin del árbol
            if indice == n:
                if valor_actual > mejor_valor:
                    mejor_valor = valor_actual
                    mejor_comb = seleccion.copy()
                return

            libro = disponibles[indice]

            # Option 1: take the book if it fits weight
            if peso_actual + float(libro.peso) <= peso_max:
                seleccion.append(libro)
                backtrack(
                    indice + 1,
                    peso_actual + float(libro.peso),
                    valor_actual + float(libro.valor),
                    seleccion
                )
                seleccion.pop()

            # Option 2: skip the book and continue
            backtrack(indice + 1, peso_actual, valor_actual, seleccion)

        # Run the search for this shelf
        backtrack(0, 0, 0, [])

        # If no valid combination found, stop
        if not mejor_comb:
            break

        # Assign shelf number to best combination
        for libro in mejor_comb:
            libro.estanteria = num_est

        # Persist structured result for the response
        resultado_final.append({
            "estanteria": num_est,
            "libros": [l.titulo for l in mejor_comb],
            "peso_total": sum(float(l.peso) for l in mejor_comb),
            "precio_total": sum(float(l.valor) for l in mejor_comb)
        })

    return {"resultado": resultado_final}

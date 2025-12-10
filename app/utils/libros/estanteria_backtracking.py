
# Selección óptima de libros por estantería (backtracking con poda)
def estanteria_backtracking(libros, peso_max=8.0):
    """Algoritmo de backtracking para asignar estanterías optimizando valor sin superar peso.

Función:
- estanteria_backtracking(libros, peso_max=8.0)
  - Recibe:
    * libros: lista de objetos con atributos al menos 'titulo', 'peso', 'valor'.
    * peso_max: límite de peso por estantería (float).
  - Devuelve:
    * dict {"resultado": [ { "estanteria": int, "libros": [titulos], "peso_total": float, "precio_total": float }, ... ] }
  - Efectos secundarios:
    * Añade/establece el atributo `estanteria` en cada objeto libro para indicar la estantería asignada (0 = sin asignar).
  - Nota:
    * Intenta empaquetar libros en estanterías maximizando valor sin exceder `peso_max`, con hasta 4 libros por estantería.
"""
    # Paso 1: inicializar todos los libros sin estantería
    for libro in libros:
        setattr(libro, "estanteria", 0)

    # Paso 2: estimar cuántas estanterías se necesitarán (máx 4 por est.)
    total_libros = len(libros)
    num_estanterias = (total_libros // 4) + 1

    resultado_final = []

    # Paso 3: iterar por cada estantería y resolver con backtracking
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

        # Backtracking: decide por libro tomarlo o no, con restricciones
        def backtrack(indice, peso_actual, valor_actual, seleccion):
            nonlocal mejor_valor, mejor_comb

            # Poda: no más de 4 libros por estantería
            if len(seleccion) > 4:
                return

            # Poda: no exceder el peso máximo
            if peso_actual > peso_max:
                return

            # fin del árbol
            if indice == n:
                if valor_actual > mejor_valor:
                    mejor_valor = valor_actual
                    mejor_comb = seleccion.copy()
                return

            libro = disponibles[indice]

            # Opción 1: tomar el libro si cabe en peso
            if peso_actual + float(libro.peso) <= peso_max:
                seleccion.append(libro)
                backtrack(
                    indice + 1,
                    peso_actual + float(libro.peso),
                    valor_actual + float(libro.valor),
                    seleccion
                )
                seleccion.pop()

            # Opción 2: no tomar el libro y continuar
            backtrack(indice + 1, peso_actual, valor_actual, seleccion)

        # Ejecutar la búsqueda para esta estantería
        backtrack(0, 0, 0, [])

        # Si no se encuentra combinación válida, terminar
        if not mejor_comb:
            break

        # Asignar número de estantería a la mejor combinación
        for libro in mejor_comb:
            libro.estanteria = num_est

        # Guardar el resultado estructurado para la respuesta
        resultado_final.append({
            "estanteria": num_est,
            "libros": [l.titulo for l in mejor_comb],
            "peso_total": sum(float(l.peso) for l in mejor_comb),
            "precio_total": sum(float(l.valor) for l in mejor_comb)
        })

    return {"resultado": resultado_final}

def estanterias_fuerzaBruta(libros):
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

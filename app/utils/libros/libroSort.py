def ordenar_libros_por_precio(libros):
    # Merge Sort completo y recursivo
    def merge_sort(lista):
        # Caso base
        if len(lista) <= 1:
            return lista
        medio = len(lista) // 2
        izquierda = merge_sort(lista[:medio])
        derecha = merge_sort(lista[medio:])
        return merge(izquierda, derecha)

    def merge(izq, der):
        resultado = []
        i = j = 0

        # Comparación basada en el atributo valor
        while i < len(izq) and j < len(der):
            if izq[i].valor <= der[j].valor:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        # Agregar cualquier sobrante
        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado
    # Ejecutar merge sort
    lista_ordenada = merge_sort(libros)
    return lista_ordenada

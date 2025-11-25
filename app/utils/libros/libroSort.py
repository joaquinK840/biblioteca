def ordenar_libros_por_precio(libros):

    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        
        mid = len(lista) // 2
        left = merge_sort(lista[:mid])
        right = merge_sort(lista[mid:])
        return merge(left, right)

    def merge(left, right):
        resultado = []
        i = j = 0

        # Mezclar ordenado por valor (int)
        while i < len(left) and j < len(right):
            if left[i].valor <= right[j].valor:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1

        # Agregar lo que sobra
        while i < len(left):
            resultado.append(left[i])
            i += 1

        while j < len(right):
            resultado.append(right[j])
            j += 1

        return resultado

    # IMPORTANTE: ¡retornar el resultado!
    lista_ordenada = merge_sort(libros)
    return lista_ordenada

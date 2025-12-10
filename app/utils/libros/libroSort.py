
def ordenar_libros_por_precio(libros):
        """Sort books by price/value using merge sort.

Public function:
- ordenar_libros_por_precio(libros)
    - Receives:
        * libros: list of objects with at least attribute `valor` (numeric or convertible to float).
    - Returns:
        * list sorted ascending by attribute `valor`.
    - Note:
        * Does not modify the original list (creates and returns a new list).
"""

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

        # Merge sorted by value (int)
        while i < len(left) and j < len(right):
            if left[i].valor <= right[j].valor:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1

        # Add remaining items
        while i < len(left):
            resultado.append(left[i])
            i += 1

        while j < len(right):
            resultado.append(right[j])
            j += 1

        return resultado

    # IMPORTANT: return the result!
    lista_ordenada = merge_sort(libros)
    return lista_ordenada

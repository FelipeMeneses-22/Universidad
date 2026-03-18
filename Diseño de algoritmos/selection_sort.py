def selection_sort(lista):
    n = len(lista)

    # Recorremos toda la lista
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el mínimo
        indice_minimo = i

        # Buscamos el elemento más pequeño en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiamos el mínimo encontrado con el elemento de la posición i
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista


# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
print(f"Lista original: {numeros}")

lista_ordenada = selection_sort(numeros)
print(f"Lista ordenada: {lista_ordenada}")
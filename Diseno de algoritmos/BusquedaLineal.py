def busqueda_lineal(lista, objetivo):
    """
    Busca un objetivo en una lista usando el algoritmo lineal.
    Retorna el índice del objetivo o -1 si no se encuentra.
    """

    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # ¡Encontrado! Retorna el índice.
    return -1  # No se encontró el objetivo.

# Ejemplo de uso
numeros = [2, 15, 7, 20, 10, 8, 3]
buscado = 10
indice = busqueda_lineal(numeros, buscado)

if indice != -1:
    print(f"El número {buscado} se encuentra en el índice {indice}.")
else:
    print(f"El número {buscado} no se encuentra en la lista.")

# Salida esperada:
# El número 10 se encuentra en el índice 4.
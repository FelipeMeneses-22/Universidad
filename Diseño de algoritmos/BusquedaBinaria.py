def busqueda_binaria(lista, objetivo):
    """
    Busca un objetivo en una lista ordenada usando el algoritmo binario.
    Retorna el índice del objetivo o -1 si no se encuentra.
    """
    
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        # Encontramos el índice del medio
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio  # ¡Encontrado!
        elif valor_medio < objetivo:
            # El objetivo está en la mitad derecha
            izquierda = medio + 1
        else:
            # El objetivo está en la mitad izquierda
            derecha = medio - 1
            
    return -1  # No se encontró el objetivo

# Ejemplo de uso
numeros_ordenados = [5, 8, 12, 16, 20, 25, 30]
buscado = 20
indice = busqueda_binaria(numeros_ordenados, buscado)

if indice != -1:
    print(f"El número {buscado} se encuentra en el índice {indice}.")
else:
    print(f"El número {buscado} no se encuentra en la lista.")
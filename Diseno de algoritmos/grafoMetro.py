from collections import deque

metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Portal Norte", "Calle 142"],
    "Calle 142":      ["Toberín", "Calle 127"],
    "Calle 127":      ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Calle 127", "Niza"],
    "Alcalá":         ["Calle 127", "Calle 100"],
    "Niza":           ["Pepe Sierra", "Calle 100"],
    "Calle 100":      ["Alcalá", "Niza", "Virrey"],
    "Virrey":         ["Calle 100", "Centro"],
    "Centro":         ["Virrey", "Portal Sur"],
    "Portal Sur":     ["Centro"],
}

def ruta_minima(grafo, origen, destino):
    # Si el origen o destino no existen
    if origen not in grafo or destino not in grafo:
        return None

    # Cola con caminos (listas)
    cola = deque([[origen]])
    
    # Visitados para no repetir nodos
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        # Si llegamos al destino
        if nodo_actual == destino:
            return camino

        # Si no lo hemos visitado
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explorar vecinos
            for vecino in grafo[nodo_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    # Si no hay camino
    return None

# Prueba:
print(ruta_minima(metro, "Portal Norte", "Centro"))
# Esperado: ['Portal Norte', 'Toberín', 'Calle 142',
#            'Calle 127', 'Alcalá', 'Calle 100', 'Virrey', 'Centro']
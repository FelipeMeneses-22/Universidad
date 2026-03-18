from collections import deque  # Cola eficiente


grafo = {
    "A": ["B", "C"],  # A conecta con B y C
    "B": ["D", "E"],  # B conecta con D y E
    "C": ["F", "G"],  # C conecta con F y G
    "D": [],          # Nodos sin hijos
    "E": [],
    "F": [],
    "G": []
}

#------------------------------------------------------------------
def busqueda_ancho(grafo, inicio):
    visitados = set()          # Guarda nodos ya visitados
    cola = deque([inicio])     # Cola (FIFO), empieza con el nodo inicial

    while cola:                # Mientras haya nodos en la cola
        nodo = cola.popleft()  # Sacamos el primero (FIFO)

        if nodo not in visitados:  # Si no lo hemos visitado
            print(nodo, end=" ")   # Lo mostramos
            visitados.add(nodo)   # Lo marcamos como visitado

            # Agregamos sus vecinos a la cola
            cola.extend(grafo[nodo])

# Ejecutar
busqueda_ancho(grafo, "A")

#------------------------------------------------------------------
def busqueda_profundidad(grafo, nodo, visitados=None):
    # Si es la primera vez, creamos el conjunto
    if visitados is None:
        visitados = set()

    # Si el nodo no ha sido visitado
    if nodo not in visitados:
        print(nodo, end=" ")   # Lo mostramos
        visitados.add(nodo)    # Lo marcamos

        # Recorremos cada vecino (recursión)
        for vecino in grafo[nodo]:
            busqueda_profundidad(grafo, vecino, visitados)

# Ejecutar
busqueda_profundidad(grafo, "A")

#------------------------------------------------------------------
def busqueda_vertical(grafo, inicio):
    # Simplemente reutiliza la búsqueda en profundidad
    return busqueda_profundidad(grafo, inicio)

# Ejecutar
busqueda_vertical(grafo, "A")

#------------------------------------------------------------------
def busqueda_horizontal(grafo, inicio):
    # Reutiliza la búsqueda en ancho
    return busqueda_ancho(grafo, inicio)

# Ejecutar
busqueda_horizontal(grafo, "A")
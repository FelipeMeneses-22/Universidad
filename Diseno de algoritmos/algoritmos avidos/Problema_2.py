import heapq  # Librería para manejar colas de prioridad (min-heaps)

# Definición de la estructura del árbol de Huffman
class Nodo:
    def __init__(self, freq, simbolo=None, izq=None, der=None):
        self.freq = freq        # Frecuencia de aparición del símbolo
        self.simbolo = simbolo  # El carácter o palabra (ej: "INFO")
        self.izq = izq          # Hijo izquierdo
        self.der = der          # Hijo derecho

    # Método para comparar nodos; necesario para que heapq sepa cuál es menor
    def __lt__(self, otro):
        return self.freq < otro.freq


def construir_huffman(frecuencias):
    """
    Crea el árbol binario de Huffman a partir de un diccionario de frecuencias.
    """
    # 1. Crear una lista de objetos Nodo y convertirla en una cola de prioridad (heap)
    heap = [Nodo(freq, simbolo) for simbolo, freq in frecuencias.items()]
    heapq.heapify(heap)

    # 2. Mientras queden más de un nodo en el heap, seguimos uniendo los más pequeños
    while len(heap) > 1:
        # Extraemos los dos nodos con las frecuencias más bajas
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)

        # Creamos un nuevo nodo "padre" cuya frecuencia es la suma de sus hijos
        # Los hijos son n1 (izquierda) y n2 (derecha)
        nuevo = Nodo(n1.freq + n2.freq, None, n1, n2)
        
        # Insertamos el nuevo nodo de vuelta en la cola
        heapq.heappush(heap, nuevo)

    # El último nodo que queda es la raíz del árbol completo
    return heap[0]


def generar_codigos(nodo, prefijo="", codigos={}):
    """
    Recorre el árbol de forma recursiva para asignar ceros y unos.
    """
    # Si el nodo tiene un símbolo, es una "hoja", guardamos su código binario
    if nodo.simbolo:
        codigos[nodo.simbolo] = prefijo
    else:
        # Si no es hoja, vamos a la izquierda (añadimos '0') 
        # y a la derecha (añadimos '1')
        generar_codigos(nodo.izq, prefijo + "0", codigos)
        generar_codigos(nodo.der, prefijo + "1", codigos)
    return codigos


# --- Datos de prueba (Niveles de logs) ---
frecuencias = {
    "ERROR": 45,
    "INFO": 120,
    "WARN": 30,
    "DEBUG": 80,
    "TRACE": 15
}

# Ejecución:
arbol = construir_huffman(frecuencias)
codigos = generar_codigos(arbol)

print("Códigos Huffman:", codigos)
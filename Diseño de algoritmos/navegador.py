# Simulamos el historial como una PILA (stack)
# El último elemento es la página actual

def retroceder(historial, pasos):
    # Caso base 1: no hay más pasos o historial vacío
    if pasos == 0 or len(historial) == 0:
        return historial
    
    # Sacamos la última página (como una pila: pop)
    pagina = historial.pop()
    print(f"Retrocediendo desde: {pagina}")
    
    # Caso base 2: si encontramos error 404, detener todo
    if pagina == "Error 404":
        print("Se encontró un Error 404. Deteniendo retroceso.")
        return historial
    
    # Llamada recursiva (seguimos retrocediendo)
    return retroceder(historial, pasos - 1)


# ===== PRUEBA =====
historial = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "Error 404",
    "github.com",
    "chat.openai.com"
]

pasos = 4

print("Historial inicial:", historial)
historial_final = retroceder(historial, pasos)
print("Historial final:", historial_final)
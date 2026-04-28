def cajero_greedy(monto, billetes):
    """
    Simulación de un cajero automático que entrega el menor número 
    de billetes posible usando una estrategia voraz.
    """
    # Diccionario para almacenar cuántos billetes de cada denominación se entregan
    resultado = {}
    
    # El algoritmo asume que 'billetes' está ordenado de mayor a menor
    for billete in billetes:
        # Calculamos cuántas veces cabe el billete actual en el monto restante
        # Usamos // para obtener la división entera
        cantidad = monto // billete  
        
        if cantidad > 0:
            # Guardamos en el diccionario: denominación -> cantidad entregada
            resultado[billete] = cantidad
            # Actualizamos el monto restante restando lo que ya vamos a entregar
            monto -= cantidad * billete  
    
    # Retornamos el desglose y lo que no se pudo entregar (si sobra algo)
    return resultado, monto


# --- Configuración de datos ---

# Es vital que la lista esté en orden descendente para que la lógica greedy funcione
billetes = [50000, 20000, 10000, 5000, 1000]
monto = 87500

# Llamada a la función
resultado, resto = cajero_greedy(monto, billetes)

# --- Salida de resultados ---
print("Distribución de billetes:", resultado)
# En este caso: {50000: 1, 20000: 1, 10000: 1, 5000: 1, 1000: 2}
print("Resto:", resto) 
# El resto será 500 porque no hay billetes menores a 1000
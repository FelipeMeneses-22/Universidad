def knapsack(costos, valores, capacidad, nombres):
    n = len(valores)
    # 1. CREACIÓN DE LA TABLA DP
    # Filas: representan los proyectos disponibles (del 0 al n)
    # Columnas: representan la capacidad de presupuesto (de 0 a 'capacidad')
    dp = [[0]*(capacidad+1) for _ in range(n+1)]

    # 2. LLENADO DE LA TABLA (Construcción de la solución óptima)
    for i in range(1, n+1):
        for w in range(capacidad+1):
            # Si el costo del proyecto actual cabe en el presupuesto actual 'w'
            if costos[i-1] <= w:
                # Decidimos: ¿Qué da más valor?
                # A) No incluir el proyecto: dp[i-1][w]
                # B) Incluir el proyecto: valor actual + el mejor valor posible con el resto del dinero
                dp[i][w] = max(
                    dp[i-1][w],
                    valores[i-1] + dp[i-1][w-costos[i-1]]
                )
            else:
                # Si el costo supera 'w', no podemos elegirlo; heredamos el valor anterior
                dp[i][w] = dp[i-1][w]

    # 3. BACKTRACKING (Identificar qué proyectos se eligieron)
    w = capacidad
    seleccion = []

    # Recorremos la tabla desde el final hacia el principio
    for i in range(n, 0, -1):
        # Si el valor cambió respecto a la fila anterior, significa que incluimos este proyecto
        if dp[i][w] != dp[i-1][w]:
            seleccion.append(nombres[i-1])
            # Restamos el costo del proyecto elegido al presupuesto disponible
            w -= costos[i-1]

    # Retornamos la tabla completa y la lista de proyectos (invertida para que se lea en orden)
    return dp, seleccion[::-1]


# --- Datos de Inversión ---
nombres = ["HealthTech", "AI Startup", "GreenTech", "Fintech"]
costos = [3, 5, 2, 4]  # Ejemplo: Millones de dólares
valores = [7, 9, 4, 6] # Ejemplo: Retorno esperado
capacidad = 10         # Presupuesto total disponible

tabla, seleccion = knapsack(costos, valores, capacidad, nombres)

print("ROI máximo:", tabla[-1][-1])  # El último valor de la tabla es la solución óptima
print("Proyectos elegidos:", seleccion)
def lcs(X, Y):
    # m y n son las longitudes de las cadenas v1 y v2
    m, n = len(X), len(Y)
    
    # 1. CREACIÓN DE LA MATRIZ DP (Dynamic Programming)
    # Creamos una tabla de (m+1) x (n+1) llena de ceros.
    # El +1 es para manejar el caso de una cadena vacía.
    dp = [[0]*(n+1) for _ in range(m+1)]

    # 2. LLENADO DE LA TABLA
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Si los caracteres actuales coinciden:
            if X[i-1] == Y[j-1]:
                # Tomamos el valor de la diagonal (arriba-izquierda) y sumamos 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Si no coinciden, heredamos el valor máximo entre:
                # El de arriba (dp[i-1][j]) o el de la izquierda (dp[i][j-1])
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 3. BACKTRACKING (Reconstrucción del resultado)
    # Al terminar el bucle, dp[m][n] tiene la longitud de la LCS.
    # Ahora recorremos la tabla hacia atrás para saber qué letras elegimos.
    i, j = m, n
    subsecuencia = ""

    while i > 0 and j > 0:
        # Si los caracteres son iguales, esta letra es parte de la LCS
        if X[i-1] == Y[j-1]:
            subsecuencia = X[i-1] + subsecuencia
            i -= 1
            j -= 1
        # Si no, nos movemos en la dirección del valor más grande en la tabla
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return dp, subsecuencia

# --- Ejemplo de uso ---
v1 = "DEPLOY-PROD-DB-01"
v2 = "DEVELOP-DEBUG-01"

tabla, lcs_resultado = lcs(v1, v2)

print("LCS:", lcs_resultado)
# Resultado esperado: "DE-D-01" (los caracteres comunes en orden)
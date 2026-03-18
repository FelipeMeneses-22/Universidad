def factorial(n):
    print(f"Entrando a factorial({n})")

    # CASO BASE
    if n == 1:
        print(f"Caso base alcanzado: factorial(1) = 1")
        return 1

    # PASO RECURSIVO
    else:
        print(f"Calculando: {n} * factorial({n-1})")

        resultado = n * factorial(n - 1)

        print(f"Resultado parcial: factorial({n}) = {resultado}")

        return resultado


# Programa principal
print("Iniciando cálculo del factorial\n")

resultado = factorial(5)

print("\nResultado final:")
print(f"El factorial de 5 es: {resultado}")
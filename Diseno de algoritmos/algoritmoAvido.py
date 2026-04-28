def cambio_greedy(monto, monedas):
    monedas.sort(reverse=True) # Ordenar de mayor a menor
    resultado = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)
    return resultado

# Uso:
print(cambio_greedy(1569, [500,100, 50, 20, 10, 5, 1]))
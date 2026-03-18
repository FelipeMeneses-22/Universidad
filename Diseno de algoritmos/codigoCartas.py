# Orden de valores
orden_valores = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13
}

# Orden de categorias
orden_categorias = {
    "Trebol": 1,
    "Diamante": 2,
    "Pica": 3,
    "Corazon": 4
}

# Función para convertir carta en valor comparable
def valor_carta(carta):
    valor, categoria = carta.split(" de ")
    return (orden_categorias[categoria], orden_valores[valor])


# Insertion Sort
def insertion_sort(cartas):
    for i in range(1, len(cartas)):
        actual = cartas[i]
        j = i - 1
        
        while j >= 0 and valor_carta(cartas[j]) > valor_carta(actual):
            cartas[j + 1] = cartas[j]
            j -= 1
        
        cartas[j + 1] = actual

# Lista desordenada de ejemplo
# Lista desordenada completa (52 cartas)
cartas = [
    "7 de Pica",
    "2 de Trebol",
    "K de Corazon",
    "2 de Diamante",
    "J de Trebol",
    "5 de Corazon",
    "A de Pica",
    "10 de Trebol",
    "3 de Diamante",
    "Q de Pica",
    "8 de Corazon",
    "4 de Trebol",
    "9 de Diamante",
    "6 de Pica",
    "A de Corazon",
    "K de Diamante",
    "J de Pica",
    "7 de Corazon",
    "3 de Trebol",
    "10 de Diamante",
    "5 de Pica",
    "Q de Corazon",
    "8 de Trebol",
    "4 de Diamante",
    "9 de Pica",
    "6 de Corazon",
    "A de Diamante",
    "K de Pica",
    "2 de Corazon",
    "J de Diamante",
    "7 de Trebol",
    "3 de Pica",
    "10 de Corazon",
    "5 de Diamante",
    "Q de Trebol",
    "8 de Pica",
    "4 de Corazon",
    "9 de Trebol",
    "6 de Diamante",
    "A de Trebol",
    "K de Trebol",
    "2 de Pica",
    "J de Corazon",
    "7 de Diamante",
    "3 de Corazon",
    "10 de Pica",
    "5 de Trebol",
    "Q de Diamante",
    "8 de Diamante",
    "4 de Pica",
    "9 de Corazon",
    "6 de Trebol"
]

print("Antes de ordenar:")
print(cartas)

insertion_sort(cartas)

print("\nDespués de ordenar:")
print(cartas)
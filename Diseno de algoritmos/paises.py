import requests

# URL de la API
URL = "https://restcountries.com/v3.1/region/europe"

# Obtener datos de la API
def obtener_paises():
    response = requests.get(URL)
    data = response.json()

    paises = []
    for pais in data:
        nombre = pais["name"]["common"]
        maps = pais["maps"]["googleMaps"]
        paises.append({"name": nombre, "map": maps})

    return paises


# BUSQUEDA LINEAL
def busqueda_lineal(paises, objetivo):
    for pais in paises:
        if pais["name"].lower() == objetivo.lower():
            return pais
    return None


# BUSQUEDA BINARIA
def busqueda_binaria(paises, objetivo):
    paises.sort(key=lambda x: x["name"].lower())

    izquierda = 0
    derecha = len(paises) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = paises[medio]["name"].lower()

        if nombre_medio == objetivo.lower():
            return paises[medio]

        elif nombre_medio < objetivo.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


def main():
    paises = obtener_paises()

    print("Seleccione tipo de búsqueda:")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")

    opcion = input("Opción: ")
    pais_buscar = input("Ingrese el nombre del país: ")

    if opcion == "1":
        resultado = busqueda_lineal(paises, pais_buscar)

    elif opcion == "2":
        resultado = busqueda_binaria(paises, pais_buscar)

    else:
        print("Opción inválida")
        return

    if resultado:
        print("\nPaís encontrado")
        print("Nombre:", resultado["name"])
        print("Google Maps:", resultado["map"])
    else:
        print("País no encontrado")


if __name__ == "__main__":
    main()
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://restcountries.com/v3.1/region/europe"

# Obtener paises desde la API
def obtener_paises():
    response = requests.get(API_URL)
    data = response.json()

    paises = []
    for p in data:
        paises.append({
            "nombre": p["name"]["common"].lower(),
            "mapa": p["maps"]["googleMaps"]
        })

    return paises


# BUSQUEDA LINEAL
def busqueda_lineal(paises, objetivo):
    for pais in paises:
        if pais["nombre"] == objetivo:
            return pais
    return None


# BUSQUEDA BINARIA
def busqueda_binaria(paises, objetivo):
    paises.sort(key=lambda x: x["nombre"])
    izquierda = 0
    derecha = len(paises) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre = paises[medio]["nombre"]

        if nombre == objetivo:
            return paises[medio]

        elif nombre < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        nombre_pais = request.form["pais"].lower()
        tipo_busqueda = request.form["tipo"]

        paises = obtener_paises()

        if tipo_busqueda == "lineal":
            resultado = busqueda_lineal(paises, nombre_pais)

        else:
            resultado = busqueda_binaria(paises, nombre_pais)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
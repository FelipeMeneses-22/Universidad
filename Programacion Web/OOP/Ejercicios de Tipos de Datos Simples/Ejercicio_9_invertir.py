# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidadInvertir = float(input("Ingrese cantidad a invertir = "))
anio = float(input("Ingrese el numero de años = "))
interes = float(input("Ingrese el interes porcentual anual = "))

total = round(cantidadInvertir * (interes / 100 + 1) ** anio, 2)

print(f"El capital es de = {total}")




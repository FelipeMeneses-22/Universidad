#----------------------------------------
#Enunciado:
#En esta aplicación vamos a calcular distintos índices corporales que nos permiten conocer algunos factores sobre nuestro estado de salud. Por ejemplo, nos pueden decir si tenemos algún tipo de sobrepeso o si estamos consumiendo más calorías al día de las que deberíamos. Los siguientes son los índices corporales que calcularemos en este proyecto:

#Tasa metabólica basal - TMB 
# ------ Formula ---------
#TMB = (10*peso (kg)) + (6.25*altura(cm)) - (5*edad(años)) + valor_genero

#----------------------------------------
#author : Juan Felipe Meneses Rodriguez
#Estudio: Semestre II / Ingenieria en sistemas
#Fecha creación : 13/10/2024
#----------------------------------------

# declaramos la funcion 
def calcular_IMC(peso: float, altura: float) -> float:
    imc = round(peso / (altura**2),2)
    return imc


print("-------- Calcular indice de masa corporal --------\n")
peso = float(input("Ingrese el peso de la persona en (kilogramos) = "))
altura = float(input("Ingrese la altura de la persona en (metros) = "))
# Formula redondeada para calcular el imc
retorno = calcular_IMC(peso,altura)

print(f"\npeso = {peso} \n\
altura = {altura} \n\
IMC = {retorno}")

# condicionales para mostrar que categoria esta el IMC de la persona
print("\n------------------ Tabla del IMC ------------------")
if retorno < 16:
    print(f"    Valor del IMC : {retorno} / Categoría: Delgadez severa")
elif 16 <= retorno <= 17:
    print(f"    Valor del IMC : {retorno} / Categoría: Delgadez moderada")
elif 17 <= retorno <= 18.49:
    print(f"    Valor del IMC : {retorno} / Categoría: Delgadez aceptable")
elif 18.5 <= retorno <= 24.99:
    print(f"    Valor del IMC : {retorno} / Categoría: Peso normal")
elif 25 <= retorno <= 29.99:
    print(f"    Valor del IMC : {retorno} / Categoría: Sobrepeso")
elif 30 <= retorno <= 34.99:
    print(f"    Valor del IMC : {retorno} / Categoría: Obesidad tipo I")
elif 35 <= retorno <= 39.99:
    print(f"    Valor del IMC : {retorno} / Categoría: Obesidad tipo II")
elif 40 <= retorno <= 49.99:
    print(f"    Valor del IMC : {retorno} / Categoría: Obesidad tipo III o mórbida")
else:
    print(f"    Valor del IMC : {retorno} / Categoría: Obesidad tipo IV o extrema")
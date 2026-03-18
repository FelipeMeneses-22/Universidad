##Porcentaje de grasa corporal - %GC
#El porcentaje de grasa corporal es una medida (porcentual) que permite establecer si una persona tiene un nivel adecuado o excesivo de grasa en su cuerpo. Este se calcula a partir del IMC, la edad y el género de la persona: 

# ------ Formula ---------
# %GC = 1.2 * IMC + 0.23 * edad(años) - 5.4 - valor_genero    

#Donde valor_genero es un valor que depende del género de la persona: en caso de ser masculino, el valor es 10.8. De lo contrario el valor es 0.

#----------------------------------------
#author : Juan Felipe Meneses Rodriguez
#Estudio: Semestre II / Ingenieria en sistemas
#Fecha creación : 13/10/2024
#----------------------------------------

#Importamos la funcion que calcula el imc
from calculadora_indices import calcular_IMC as calc_ind

# Formula para calcular el procentaje de grasa
def calcular_porcentaje_grasa(imc:float, edad ,valor_genero: float) -> float:
    return round(1.2* imc + (0.23 * edad) - 5.4 - valor_genero)

print("---------- Calcular porcentaje de grasa ----------\n")
try: # contralamos el error en caso de que ingresen un caracter no valido
    peso = float(input("Ingrese el peso de la persona en (kilogramos) = "))
    altura = float(input("Ingrese la altura de la persona en (metros) = "))
    edad = int(input("Ingrese la edad de la persona = "))
except ValueError:
    print("Caracter no valido.")
valor_genero = float(input("Ingrese el genero de la persona ( F(0) / M(10.8) ) = "))

#     Usamos la funcion que importamos para calcular el imc
imc = calc_ind(peso, altura)
#                  Usamos la funcion de calcular la grasa
porcentaje_grasa = calcular_porcentaje_grasa(imc, edad, valor_genero)

print("---------------------------------------")
print(f"\n\nEl peso de la persona es {peso}")
print(f"La altura de la persona es {altura}")
print(f"La edad de la persona es {edad}")
print(f"El indice de masa corporal es de : {imc}")
print(f"El porcentaje de grasa es de {porcentaje_grasa}%")

#En general, si las personas desean adelgazar deben reducir las calorías que ingieren a diario y/o deben aumentar el gasto calórico haciendo más deporte. Si se escoge la primera opción, se recomienda que las personas ingieran a diario entre un 15% a 20% menos calorías de las que arroja la TMB. Lo anterior sugiere que una persona que desee adelgazar debe consumir entre 80% y 85% de las calorías que representa la TMB.  

#  ------ Formula ---------
# 15% o 20% - TMB (formula general)
# 80% y 85% + TMB para adelgazar (formula para aplicar)

#----------------------------------------
#author : Juan Felipe Meneses Rodriguez
#Estudios: Semestre II / Ingenieria en sistemas
#Fecha creación : 13/10/2024
#----------------------------------------


def calculo_calorias_adelgazar(tmb:float) -> float:
    formula_adelgazar_inferior = round(tmb * 0.80,2) 
    formula_adelgazar_superior = round(tmb * 0.85,2)
    # devolvemos las tres formulas aplicando el descuento
    return formula_adelgazar_inferior, formula_adelgazar_superior

# Solicitar al usuario los datos
print("\n\n---------- Calcular calorias para adelgazar----------\n")
try: # contralamos el error en caso de que ingresen un caracter no valido
    peso = float(input("Ingrese el peso de la persona en (kilogramos) = "))
    altura = float(input("Ingrese la altura de la persona en (cm) = "))
    edad = int(input("Ingrese la edad de la persona = "))
except ValueError:
    print("Caracter no valido.")
valor_genero = float(input("Ingrese el genero de la persona ( F(0) / M(10.8) ) = "))

# pedimos la tasa metabolica
tmb = float(input("\nIngrese la Tasa Metabólica Basal (TMB) en calorías: "))

# ponemos dos variables donde le vamos a guardar el resultado de la funcion
formula_adelgazar_inferior, formula_adelgazar_superior = calculo_calorias_adelgazar(tmb)


print("\n---------------------------------------")
print(f"El peso de la persona es {peso}")
print(f"La altura de la persona es {altura}")
print(f"La edad de la persona es {edad}")
print(f"El valor del genero es = {valor_genero}")
print(f"Las calorias son {tmb} cal")
print(f"Lo anterior sugiere que una persona que desee adelgazar debe consumir entre {formula_adelgazar_inferior} y {formula_adelgazar_superior} de las calorías que representa la TMB")






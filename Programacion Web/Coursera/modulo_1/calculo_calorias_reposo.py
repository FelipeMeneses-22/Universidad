#La tasa metabólica basal es el mínimo de calorías necesarias para vivir, es decir el número de calorías que un ser humano quema al día estando en reposo. Estas calorías son utilizadas por el cuerpo para llevar a cabo funciones básicas como: bombear la sangre, hacer digestión, respirar, mantener el cerebro funcionando, etc. La TMB se calcula a través de la siguiente fórmula:   

#  ------ Formula ---------
#TMB = (10*peso (kg)) + (6.25*altura(cm)) - (5*edad(años)) + valor_genero

#Donde valor_genero es un valor que depende del género de la persona: en caso de ser masculino, el valor es 5, mientas que es -161 en caso de ser femenino.

#----------------------------------------
#author : Juan Felipe Meneses Rodriguez
#Estudios: Semestre II / Ingenieria en sistemas
#Fecha creación : 13/10/2024
#----------------------------------------

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:int) -> float:
    return round((10*peso) + (6.25*altura) - (5*edad) + valor_genero)

print("---------- Calcular calorias en reposo ----------\n")
try: # contralamos el error en caso de que ingresen un caracter no valido
    peso = float(input("Ingrese el peso de la persona en (kilogramos) = "))
    altura = float(input("Ingrese la altura de la persona en (cm) = "))
    edad = int(input("Ingrese la edad de la persona = "))
except ValueError:
    print("Caracter no valido.")
valor_genero = float(input("Ingrese el genero de la persona ( F(0) / M(10.8) ) = "))

#                 se usa la funcion que contiene la formula 
calorias_reposo = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)


print("---------------------------------------")
print(f"El peso de la persona es {peso}")
print(f"La altura de la persona es {altura}")
print(f"La edad de la persona es {edad}")
print(f"Las calorias que se queman en reposo es de {calorias_reposo} cal")
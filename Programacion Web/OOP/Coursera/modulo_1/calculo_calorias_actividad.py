#Dado que las personas realizamos actividad física en el día, el consumo de calorías diarias (el cual denominaremos TMB_(actividad_fisica)  ) es mayor al TMB. Para poder calcularlo es necesario multiplicar el TMB por un valor que depende de la actividad física semanal que realiza cada persona:

# ------ Formula ---------
# TMB_(actividad_fisica) = TMB * valor_actividad

# Donde valor_actividad es un valor que depende de la actividad física que lleva a cabo la persona semanalmente y toma los siguientes valores:

# 1.2: poco o ningún ejercicio

# 1.375: ejercicio ligero (1 a 3 días a la semana)

# 1.55: ejercicio moderado (3 a 5 días a la semana)

# 1.72: deportista (6 -7 días a la semana)

# 1.9: atleta (entrenamientos mañana y tarde.)

#----------------------------------------
#author : Juan Felipe Meneses Rodriguez
#Estudio: Semestre II / Ingenieria en sistemas
#Fecha creación : 13/10/2024
#----------------------------------------

#Importamos la funcion que calcula las calorias de reposo
from calculo_calorias_reposo import calcular_calorias_en_reposo as calc_rep

def calcular_calorias_actividad(tmb:float, valor_actividad:float):
    return round(tmb * valor_actividad, 2)

# Solicitar al usuario los datos
print("\n\n---------- Calcular calorias en actividad fisica ----------\n")
try: # contralamos el error en caso de que ingresen un caracter no valido
    peso = float(input("Ingrese el peso de la persona en (kilogramos) = "))
    altura = float(input("Ingrese la altura de la persona en (cm) = "))
    edad = int(input("Ingrese la edad de la persona = "))
except ValueError:
    print("Caracter no valido.")
valor_genero = float(input("Ingrese el genero de la persona ( F(0) / M(10.8) ) = "))

# hacemos los calculos con la funcion que importamos
calc_reposo = calc_rep(peso,altura,edad,valor_genero)
print(f"\nLa tasa metabolica basal es {calc_reposo} cal")

# Menu para que el uduario ingrese los datos
print("\nSeleccione su nivel de actividad física:")
print("1. Poco o ningún ejercicio (1.2)\n 2. Ejercicio ligero (1 a 3 días a la semana) (1.375)\n 3. Ejercicio moderado (3 a 5 días a la semana) (1.55)\n 4. Deportista (6 a 7 días a la semana) (1.725)\n 5. Atleta (entrenamientos mañana y tarde) (1.9)")

tmb = float(input("\nIngrese la Tasa Metabólica Basal (TMB) en calorías: "))

try:
    nivel_actividad = int(input("\nIngrese el número correspondiente a su nivel de actividad física: "))
except ValueError:
    print("Caracter no valido.")

# condicionales para saber el valor asignado 
if nivel_actividad == 1:
    valor_actividad = 1.2
elif nivel_actividad == 2:
    valor_actividad = 1.375
elif nivel_actividad == 3:
    valor_actividad = 1.55
elif nivel_actividad == 4:
    valor_actividad = 1.72
elif nivel_actividad == 5:
    valor_actividad = 1.9
else:
    print("Opción no válida.")
    exit()

# usamos la funcion donde calculamos el tmb
tmb_actividad_fisica = calcular_calorias_actividad(tmb, valor_actividad)

print("---------------------------------------")
print(f"El peso de la persona es {peso}")
print(f"La altura de la persona es {altura}")
print(f"La edad de la persona es {edad}")
print(f"El genero de la persona es {edad}")
print(f"\nEl consumo de calorías diarias ajustado por actividad física es: {tmb_actividad_fisica} cal")
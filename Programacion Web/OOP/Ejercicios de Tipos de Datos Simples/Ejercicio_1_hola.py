
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print( "¡Hola Mundo!" )

def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, 
                dia_actual: int, mes_actual: int, anio_actual: int) -> str:
    
    # Inicialmente calculamos los años, meses y días
    anios = anio_actual - anio_nacio
    meses = mes_actual - mes_nacio
    dias = dia_actual - dia_nacio
    
    # Ajuste si el día actual es menor que el día de nacimiento
    if dias < 0:
        dias += 30  # Suponiendo que todos los meses tienen 30 días
        meses -= 1

    # Ajuste si el mes actual es menor que el mes de nacimiento
    if meses < 0:
        meses += 12
        anios -= 1

    # Formateamos el resultado como "aa,MM,dd"
    return f"{anios},{meses},{dias}"

# Ejemplo de uso
edad = calcular_edad(5, 8, 2019, 15, 8, 2020)
print(f"La edad es: {edad}")
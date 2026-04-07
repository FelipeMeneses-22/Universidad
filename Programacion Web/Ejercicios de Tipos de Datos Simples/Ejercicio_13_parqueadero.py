#**********************************************************
#*Algoritmo que calcula el monto a pagar por servicio de
# parqueadero. Las horas de entrada y salida se dan en 
# formato militar
#
# Programo: FMR
# Fecha: 10/10/2024
# Cambios:  
#*********************************************************/


#/**********************************************************
# Presenta la pantalla principal con los mensajes correspondientes
# PARAMETRO:
# RETORNA:
# EXCEPCION:
#**********************************************************/
def mostrarInicio():
    print(" ")
    print("------------ SERVICIO DE PARQUEADERO -------------")
    print(" ")
    print("Ingrese las horas utilizando formato Militar(HHMM)")
    print(" ")

#/**********************************************************
# Ingresa la hora en formato militar
# Ingresa un entero validando el formato (HHMM)
# HH entre 0 y 23, MM entre 00 y 59
# PARAMETRO:
# RETORNA:  numero hora
# EXCEPCION:
#**********************************************************/
def ingresarHora(h):
    hora = 0
    valido = False
    while valido != True:
        valido = True
        hora = int(input("Ingrese la hora de {}: ".format(h)))
        
        if hora < 0:                #//numeros negativos
            valido = False
            
        if (hora // 100) > 23:       #//hora mayor a 23
            valido = False
            
        if (hora % 100) > 59:       #//minutos mayor a 59
            valido = False
            
        if valido == False:
            print("numero no valido...")
    return(hora)

#/**********************************************************
# pasar horas a minutos
# Calcula los minutos contenidos en un valor en formato militar
# PARAMETROS: entero hora
# RETORNA: entero minutos
# EXCEPCION:
#**********************************************************/
def pasarMinutos(hora):
    minutos = (hora // 100) * 60     #//parte de la hora
    minutos += (hora % 100)           #//parte de minutos
    return (minutos)
    
#/**********************************************************
# Calcula el tiempo transcurrido
# Calcula el tiempo transcurrido, en horas, la fraccion se aproxima
# a la siguiente hora
# PARAMETROS: entero hEntra, hSale: Horas de entrada y salida
# RETORNA: entero totTiempo en minutos
# EXCEPCION:
#**********************************************************/
def calcularTiempo(hEntra, hSale):
    horas = 0
    hEntra = pasarMinutos(hEntra)
    hSale = pasarMinutos(hSale)
    
    dif = hSale - hEntra
    if dif <= 0:
        dif += 1440     #Ajuste por cambio de día

    horas = dif // 60    #Cantidad de horas

    if dif % 60 > 0: 
        horas += 1      #Ajusta minutos restantes a otra hora
        
    return (horas)
#/**********************************************************
# Calcula el valor del servicio de parquedero

# Calcula el valor del parqueo, a partir de la hora de entrada
# y la hora de salida. La primera hora vale $1000,
# las demas a $600. Minutos adicionales se aproximan a la hora
# PARAMETROS: entero hEntra, hSale
# RETORNA: entero monto
# EXCEPCION:
#
#**********************************************************/    
def calcularMonto(hEntra, hSale):
    monto = 1000                                #//valor primera hora
    tiempo = calcularTiempo(hEntra, hSale)-1    #//menos hora inicial ya cobrada
    if tiempo > 0:
        monto += (tiempo * 600)                   #//valor Horas adicionales

    return monto


#/**********************************************************
#* PROGRAMA PRINCIPAL
#**********************************************************/
mostrarInicio()
horaEntrada = ingresarHora("entrada")
horaSalida = ingresarHora("salida")
monto = calcularMonto(horaEntrada, horaSalida)
print(" ")
print("El valor total del servicio es ${}".format(monto))
    
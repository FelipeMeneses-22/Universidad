#importamos el archivo cajero para poder llamar la variable saldo
import cajero

#defnimos la funcion 
def retirarDinero():
    try:
        print("-------------------------------")
        print("Eligio la opcion de retirar dinero")
        #Escribimos la cantidad que deseamos retirar 
        cantidad = float(input("Ingrese la cantidad que va a retirar = "))
        #Realizamos la operacion
        if cantidad > cajero.saldo:
            print("saldo insuficiente")
        else:
            #imprimimos que el retiro se realizo y mostramos el saldo que queda
            cajero.saldo -= cantidad
            print(f"Retiro exitoso \n Dinero retirado, Su saldo actual es {cajero.saldo}")
    except ValueError:
        print("Error : Por favor no escriba letras")
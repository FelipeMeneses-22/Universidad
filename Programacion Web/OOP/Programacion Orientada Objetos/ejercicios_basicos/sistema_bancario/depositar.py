#importamos el archivo cajero para poder llamar la variable saldo
import cajero

#defnimos la funcion 
def depositarDinero():
    print("-------------------------------")
    print("Eligio la opcion de depositar dinero")
    #Escribimos la cantidad que deseamos retirar 
    cantidad = float(input("Ingrese la cantidad que va a depositar = "))
    #Realizamos la operacion
    cajero.saldo += cantidad
    #imprimimos el resultado mas el saldo que queda
    print(f"Dinero depositado, Su saldo actual es {cajero.saldo}")
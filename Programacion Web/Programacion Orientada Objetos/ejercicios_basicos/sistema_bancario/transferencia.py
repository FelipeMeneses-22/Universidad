#llamamos el archivp cajero
import cajero

def transferenciaDinero():
    print("-------------------------------")
    #creamos un try en caso de que ponga letras
    try:
        cuenta_destino = int(input("Ingrese el numero de cuenta = "))
        cantidad = float(input("Ingrese la cantidad a transferir : "))
        print("Error : Las letras no son validas")
        #Creamos condicional donde el dinero si es menor o igual al saldo se ejecuta
        if cantidad <= cajero.saldo: #llamamos la variable saldo
            cajero.saldo -= cantidad #hacemos la ecuacion
            print(f"Transferencia exitosa \n Su saldo actual {cajero.saldo}")
        else:
            #en caso de que no alla un saldo suficiente
            print("Error saldo insufiente")
    except ValueError:
        print("Error : Ingrese unicamente numeros")
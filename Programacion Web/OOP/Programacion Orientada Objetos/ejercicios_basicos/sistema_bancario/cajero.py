import sesion, retiro, transferencia, depositar,consulta


# ddefinimos el saldo, usuario, contraseña de manera global
saldo = 100000


def cajero():
    
    # Si el usuario el correcto iniciamos una condicional
    if sesion.login():
        global saldo
        
        # Generamos un bucle
        while True:
            print("-------------------------------")
            # Menu del cajero
            print("Selecione lo que desea realizar : \n 1) Consultar saldo \n 2) transferencias \n 3) Retirar dinero \n 4) Depositar dinero \n 5) Salir")
            
            # Ingresamos la opcion
            try:
                opcion = int(input("Ingrese lo que va a realizar: "))
            except ValueError:
                print("Error: No ingrese letras solo numeros")
                
            # Mostramos el saldo
            if opcion == 1:
                consulta.consultaDinero()
            # llamos el la funcion del archivo tranfeencia
            elif opcion == 2:
                transferencia.transferenciaDinero()
            # llamamos la funcion del archivo retirar
            elif opcion == 3:
                retiro.retirarDinero()
            #llamamos la funcion del archivo depositar
            elif opcion == 4:
                depositar.depositarDinero()
            else:
                print("Gracias eso fue todo")
                break
cajero()
import inventario

def biblioteca():

    nombre = input("ingrese su nombre = ")

    while True:
        print(f"{nombre}. Elige una opción \n 1)Consultar libro \n 2)Realizar prestamo \n 3)Salir")

        opcion = input("Elije la opción = ")

        if opcion == 1:
            inventario.consultaLibros()
            
biblioteca()
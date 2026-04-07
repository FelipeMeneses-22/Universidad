class Vehiculo:
    def __init__(self, marca, modelo, anio, color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido: 
            self.encendido = True
            print("\n       El vehiculo esta encendido :D")
        else:
            print("\n       El carro ya esta encendido D:")
            
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("\n       El carro esta apagado")
        else:
            print("\n       El carro esta encendido")

    def pitar(self):
        if not self.encendido:
            print("\n       El carro ya esta apagado, no puede pitar")
        else:
            print("\n       taratatata taratatata taratatata taratatata")

    def girar(self):
        if not self.encendido:
            print("\n       El vehiculo esta apagad")
        else:
            girar = input("A que dirección quieres girar = ").lower()
            if girar == "derecha":
                print("El vehiculo esta girando a la derecha")
            elif girar == "izquierda":
                print("El vehiculo esta girando a la izquierda")
            else:
                return f"Sos dixlecico o que bro ?"
            
    def cambiarMarcha(self):
        if not self.encendido:
            print("\n       El vehiculo esta apagad")
        else:
            marcha = int(input("A que marcha quieres ir : "))
            if marcha == 1:
                print("estas en la primera marcha, vas lento :D")
            elif marcha == 2:
                print("estas en la segunda marcha, vas lento :D")
            elif marcha == 3:
                print("estas en la tercera marcha, vas lento :D")
            elif marcha == 4:
                print("estas en la cuarta marcha, vas rapido bro :D")
            elif marcha == 5:
                print("estas en la quinta marcha, vas rapido bro :D")
            else:
                print(f"__________________________________________________ \n \n\
            No existe esa marcha en el vehiculo {self.marca}, {self.modelo}, {self.anio}, {self.color}")

    def __str__(self):
        return f"__________________________________________________\n \n\
            La marca del vehiculo es {self.marca} \n\
            La modelo del vehiculo es {self.modelo} \n\
            La anio del vehiculo es {self.anio} \n\
            La color del vehiculo es {self.color} \n\
__________________________________________________\n"

print("__________________________________________________\n")
print("                Bienvenido :D \n")
marca = input("        Elige la marca del vehiculo : ")
modelo = input("        Elige la modelo del vehiculo : ")
anio = input("        Elige la año del vehiculo : ")
color = input("        Elige la color del vehiculo : ")

coche=Vehiculo(marca, modelo, anio, color)

def main():    
    print("__________________________________________________\n\
        1. Encender \n\
        2. Apagar \n\
        3. Pitar \n\
        4. Girar \n\
        5. Cambiar marcha \n\
        6. Salir \n\
        \n")

    try:
        print("__________________________________________________\n")
        opcion = int(input("        Elige la opción : "))
    except ValueError:
        print("No ponga letras")
        
    if opcion == 1:
        coche.encender()
    elif opcion == 2:
        coche.apagar()
    elif opcion == 3:
        coche.pitar()
    elif opcion == 4:
        coche.girar()
    elif opcion == 5:
        coche.cambiarMarcha()
    elif opcion == 6:
        print("Saliendo del vehiculo :D")
        return False
    else:
        print("Solo numeros del 1 al 6 ")
    
while True:
    op = main()
    if op==False:
        break
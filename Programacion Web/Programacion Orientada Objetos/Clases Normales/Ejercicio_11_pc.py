# Crea una clase Computadora que tenga los atributos marca, modelo, procesador y RAM, los cuales serán solicitados en el constructor. La clase debe tener los siguientes métodos: encender() para encender la computadora, apagar() para apagar la computadora, abrir_programa(nombre_programa) para abrir un programa dado, cerrar_programa(nombre_programa) para cerrar un programa, y mostrar_info_sistema() que muestre la información del sistema (marca, modelo, procesador, RAM).
# Crea un menú interactivo para ejecutar las opciones y una opción para salir.

class Computadora:
    def __init__(self, marca, modelo, procesador, ram):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El computador fue encendido, usalo como gustes")
        else:
            print("El computador ya esta encendido, no puede prenderlo otra ver")
        
    def apagar(self):
        if not self.encendido:
            self.encendido = False
            print("El computador esta apagado")
        else:
            print("El computador ya esta apagado")

    def abrirPrograma(self):
        if not self.encendido:
            self.encendido = True
            print("____________________________________________________ \n")
            while True:
                print("____________________________________________________ \n\
                    Lista de programas instalados en la computadora. \n\
                        * Tinder \n\
                        * Google \n\
                        * Yahoo \n\
                        * Steam \n\
                        * Wikipedia \n\
                        * Salir")
                
                programa = input("Selecciona un programa : ").capitalize()

                if programa == "Tinder":
                    print("Haz ingresa a Tinder, que la pases bien colega")
                elif programa == "Google":
                    print("Haz ingresa a Google, navega como quieras")
                elif programa == "Yahoo":
                    print("Haz ingresa a Tinder, que la pases bien colega")
                elif programa == "Steam":
                    print("Hay nuevos juegos para que disfrutes en Steam :D")
                elif programa == "Wikipedia":
                    print("Nunca es tarde para hacer la tarea con wikipedia amigo")
                else:
                    print("Pasala bien y vuelve pronto a abrir un programa amigo")
                    break
        else:
            print("Debes de cerrar el programa")
            
    def cerrarPrograma(self):
        pass
    
    def __str__(self):
        return f"____________________________________________________ \n\
                    Marca : {self.marca} \n\
                    Modelo : {self.modelo} \n\
                    Procesador : {self.procesador} \n\
                    RAM : {self.ram} \n\
                        "

marca = input("Marca del computador : ")
modelo = input("Modelo del Computador : ")
procesador = input("Procesador PC :")
ram = input("Ingrese la RAM : ")

pc = Computadora(marca,modelo,procesador,ram)

def main():
    print("____________________________________________________ \n\
        Bienvenido al Menu de tu computadora \n \n\
                1. Encender \n\
                2. Apagar \n\
                3. Abrir Programa \n\
                4. Cerrar programa \n\
                5. Salir \n\
                    ")
    try:
        op = int(input("Elige una opción : "))
    except ValueError:
        print("Error : Ingrese solo numeros")

    if op == 1:
        pc.encender()
    elif op == 2:
        pc.apagar()
    elif op == 3:
        pc.abrirPrograma()
    elif op == 4:
        pc.cerrarPrograma()
    elif op == 5:
        print("Apagando el celular")
        return False
    else:
        print("Elige una opcion entre 1 a 5 :D")

while True:
    p = main()
    if p==False:
        break

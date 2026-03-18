class Amigo:
    # Atributos de la clase Amigo
    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = int(telefono)
        self.listaAmigo = []

    ###################################################
    # Métodos Setter
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCorreo(self, correo):
        self.__correo = correo

    def setTelefono(self, telefono):
        self.__telefono = telefono

    ###################################################
    # Métodos Getter
    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getCorreo(self):
        return self.__correo

    @property
    def getTelefono(self):
        return self.__telefono

    ###################################################
    def agregarAmigo(self):
        self.__nombre = input(f"   Ingresa el nombre de tu amig@ = ")
        self.__correo = input(f"    Ingresa el correo de tu amig@ = ")
        try:
            self.__telefono = int(input(f"    Ingresa el telefono de tu amig@ = "))
        except ValueError:
            print("Digite un número válido")

        listadoAmigos = {
            'nombre': self.__nombre,
            'correo': self.__correo,
            'telefono': self.__telefono
        }
        self.listaAmigo.append(listadoAmigos)

    ###################################################
    def modificarAmigo(self):
        while True:
            if len(self.listaAmigo) > 0:
                print("______________________________________________________\n")
                print("            Listado de amigos:")
                for idx, amigo in enumerate(self.listaAmigo):
                    print(f"{idx + 1}. Nombre: {amigo['nombre']}, Correo: {amigo['correo']}, Teléfono: {amigo['telefono']} \n")
            else:
                print("        No hay amigos en la lista\n")
                break

            print("        Vas a modificar a un amigo \n\
        Selecciona lo que deseas realizar\n\
            1. Cambiar nombre \n\
            2. Cambiar correo \n\
            3. Cambiar teléfono \n\
            4. Salir")

            op = int(input("        Ingrese lo que desea realizar: "))

            if op == 1:
                amigoActual = input("           Escribe el nombre del amigo que quieres cambiar: ")
                newNombre = input("\n           Escribe el nuevo nombre de tu amigo: ")
                for amigo in self.listaAmigo:
                    if amigo["nombre"] == amigoActual:
                        amigo["nombre"] = newNombre
                        print(f"\nEl nombre ha sido cambiado con éxito a {newNombre} \n")
            elif op == 2:
                amigoActual = input("Escribe el correo del amigo que quieres cambiar: ")
                newCorreo = input("\nEscribe el nuevo correo de tu amigo: ")
                for amigo in self.listaAmigo:
                    if amigo["correo"] == amigoActual:
                        amigo["correo"] = newCorreo
                        print(f"\nEl correo ha sido cambiado con éxito a {newCorreo} \n")
            elif op == 3:
                amigoActual = int(input("Escribe el teléfono del amigo que quieres cambiar: "))
                newTelefono = int(input("\nEscribe el nuevo teléfono de tu amigo: "))
                for amigo in self.listaAmigo:
                    if amigo["telefono"] == amigoActual:
                        amigo["telefono"] = newTelefono
                        print(f"\nEl teléfono ha sido cambiado con éxito a {newTelefono} \n")
            else:
                print("Has elegido salir del menú de modificación")
                break

    def eliminarAmigo(self):
        nombre = input("        Ingrese el nombre del amigo que desea eliminar: ").lower()
        for amigo in self.listaAmigo:
            if amigo["nombre"] == nombre:
                self.listaAmigo.remove(amigo)
                print("\nAmigo eliminado exitosamente.")
                return
        print("\nNo se encontró el amigo.")

    def mostrarAmigo(self):
        print(f"\nLa lista de tus amigos actual es {self.listaAmigo}")


n1 = Amigo("", "", 0)

def main():
    print("______________________________________________________")
    print("Bienvenido a la lista de contactos \n\
    Opciones que se pueden realizar: \n\
        1. Agregar amigos \n\
        2. Modificar amigos \n\
        3. Eliminar amigos\n\
        4. Mostrar lista de amigos\n\
        5. Salir del menú")

    while True:
        try:
            opcion = int(input("Ingrese qué opción desea realizar: "))
            if 1 <= opcion <= 5:
                break
            else:
                print("\nIngresaste una opción que no se encuentra en el menú.")
        except ValueError:
            print("\nDigitaste un carácter no válido en el menú.")

    if opcion == 1:
        n1.agregarAmigo()
        print(f"\nTu amigo '{n1.getNombre}' ha sido agregado con éxito")
    elif opcion == 2:
        n1.modificarAmigo()
    elif opcion == 3:
        n1.eliminarAmigo()
    elif opcion == 4:
        n1.mostrarAmigo()
    else:
        print("Saliendo del menú. Vuelve pronto.")


while True:
    main()
    if input("¿Deseas salir? (s/n): ").lower() == 's':
        print("\nSaliste de la agenda de contactos, ten una buena tarde\n")
        break
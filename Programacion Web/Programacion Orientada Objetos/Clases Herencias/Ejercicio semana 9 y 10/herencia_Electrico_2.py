#Enunciado: Crea un sistema que gestione dispositivos electrónicos. Define una clase Dispositivo que contenga el nombre y el consumo energético. Luego, crea una clase Telefono que herede de Dispositivo y añada capacidad de almacenamiento, y una clase Computadora que añada el tipo de procesador. Finalmente, crea una clase Smartphone que herede de ambas y permita gestionar tanto la capacidad como el procesador.

#Clases involucradas:

#Dispositivo: nombre, consumo energético.
#Telefono: hereda de Dispositivo y añade capacidad de almacenamiento.
#Computadora: hereda de Dispositivo y añade tipo de procesador.
#Smartphone: hereda de Telefono y Computadora, maneja ambos atributos.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 18/10/2024
# ----------------------------------------

# ------------clase base------------
class Dispositivo:
    def __init__(self, nombre, consumo_energetico):
        self.__nombre = nombre
        self.__consumo_energetico = consumo_energetico

    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getConsumoEnergetico(self):
        return self.__consumo_energetico

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setConsumoEnergetico(self, consumo_energetico):
        self.__consumo_energetico = consumo_energetico

    def __str__(self):
        return f"Dispositivo: {self.getNombre}, Consumo Energético: {self.getConsumoEnergetico}W"


# ------------clase que hereda de Dispositivo------------
class Telefono(Dispositivo):
    def __init__(self, nombre, consumo_energetico, capacidad_almacenamiento):
        super().__init__(nombre, consumo_energetico)
        self.__capacidad_almacenamiento = capacidad_almacenamiento

    @property
    def getCapacidadAlmacenamiento(self):
        return self.__capacidad_almacenamiento

    def setCapacidadAlmacenamiento(self, capacidad_almacenamiento):
        self.__capacidad_almacenamiento = capacidad_almacenamiento

    def __str__(self):
        return f"{super().__str__()}, Capacidad de Almacenamiento: {self.getCapacidadAlmacenamiento}GB"


# ------------clase que hereda de Dispositivo------------
class Computadora(Dispositivo):
    def __init__(self, nombre, consumo_energetico, tipo_procesador):
        super().__init__(nombre, consumo_energetico)
        self.__tipo_procesador = tipo_procesador

    @property
    def getTipoProcesador(self):
        return self.__tipo_procesador

    def setTipoProcesador(self, tipo_procesador):
        self.__tipo_procesador = tipo_procesador

    def __str__(self):
        return f"{super().__str__()}, Tipo de Procesador: {self.getTipoProcesador}"


# ------------clase con herencia múltiple------------
class Smartphone(Telefono, Computadora):
    def __init__(self, nombre, consumo_energetico, capacidad_almacenamiento, tipo_procesador):
        Telefono.__init__(self, nombre, consumo_energetico, capacidad_almacenamiento)
        Computadora.__init__(self, nombre, consumo_energetico, tipo_procesador)

    def __str__(self):
        return f"{Telefono.__str__(self)}, Procesador: {self.getTipoProcesador}"


# -------------clase de interacción-----------# In Python, the `--` operator is used for decrementing
# a numerical value by 1. It is a shorthand notation for
# subtracting 1 from the variable.

class SistemaDispositivos:
    def __init__(self):
        self.listaDispositivos = []

    def agregarDispositivo(self, dispositivo):
        self.listaDispositivos.append(dispositivo)
        print(f"El dispositivo '{dispositivo.getNombre}' se agregó con éxito.")

    def mostrarDispositivos(self):
        if self.listaDispositivos:
            print("\nDispositivos registrados:")
            for dispositivo in self.listaDispositivos:
                print(dispositivo)
        else:
            print("\nNo hay dispositivos registrados.")

    def menu(self):
        while True:
            print("\n  Sistema de Gestión de Dispositivos Electrónicos \n\
                    1. Registrar Dispositivo \n\
                    2. Mostrar Dispositivos \n\
                    3. Salir")

            opcion = int(input("\n Ingrese la opción que desea realizar: "))

            if opcion == 1:
                self.registrarDispositivo()
            elif opcion == 2:
                self.mostrarDispositivos()
            elif opcion == 3:
                print("Saliendo del sistema.")
                break
            else:
                print("Opción incorrecta.")

    def registrarDispositivo(self):
        nombre = input("Ingrese el nombre del dispositivo: ")
        consumo = float(input("Ingrese el consumo energético en watts: "))
        tipo_dispositivo = input("¿Es un teléfono, computadora o smartphone? (t/c/s): ").lower()

        if tipo_dispositivo == "t":
            capacidad = int(input("Ingrese la capacidad de almacenamiento (en GB): "))
            nuevo_dispositivo = Telefono(nombre, consumo, capacidad)
        elif tipo_dispositivo == "c":
            procesador = input("Ingrese el tipo de procesador: ")
            nuevo_dispositivo = Computadora(nombre, consumo, procesador)
        elif tipo_dispositivo == "s":
            capacidad = int(input("Ingrese la capacidad de almacenamiento (en GB): "))
            procesador = input("Ingrese el tipo de procesador: ")
            nuevo_dispositivo = Smartphone(nombre, consumo, capacidad, procesador)
        else:
            print("Tipo de dispositivo no válido.")
            return

        self.agregarDispositivo(nuevo_dispositivo)


# ----------Inicializando el menú-----------------
sistema = SistemaDispositivos()
sistema.menu()
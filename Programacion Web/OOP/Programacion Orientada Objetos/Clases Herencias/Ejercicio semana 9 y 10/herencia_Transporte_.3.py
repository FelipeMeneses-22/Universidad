# Enunciado: Desarrolla un sistema de administración para diferentes medios de transporte. Crea una clase Vehiculo que contenga el número de ruedas y el tipo de combustible. Luego, crea una clase Bicicleta que herede de Vehiculo y añada el tipo de freno, y una clase Automovil que añada la capacidad del motor. Finalmente, crea una clase BicicletaElectrica que herede de ambas, representando una bicicleta con asistencia eléctrica.

# Clases involucradas:

# Vehiculo: número de ruedas, tipo de combustible.
# Bicicleta: hereda de Vehiculo y añade tipo de freno.
# Automovil: hereda de Vehiculo y añade capacidad del motor.
# BicicletaElectrica: hereda de Bicicleta y Automovil.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 18/10/2024
# ----------------------------------------


class Vehiculo:  # clase base
    def __init__(self, ruedas, tipoCombustible):
        self.__ruedas = ruedas  # Atributo protegido
        self.__tipoCombustible = tipoCombustible  # Atributo protegido

    def __str__(self) -> str:  # str que describe cada atributo
        return f"Numero de ruedas : {self.getRueda}, Tipo de combustible : {self.getTipoCombustible}"

    # ________________Getter______________________________
    @property
    def getRueda(self):
        return self.__ruedas

    def setRueda(self, ruedas):
        self.__ruedas = ruedas

    # ________________Setter______________________________
    @property
    def getTipoCombustible(self):
        return self.__tipoCombustible

    def setTipoCombustible(self, tipoCombustible):
        self.__tipoCombustible = tipoCombustible


class Bicicleta(Vehiculo):  # clase que hereda los atributos de la clase vehiculo
    def __init__(self, ruedas, tipoCombustible, tipoFreno):
        super().__init__(ruedas, tipoCombustible)
        self.__tipoFreno = tipoFreno

    def __str__(self):  # str que describe cada atributo
        return f"{super().__str__()}, Tipo de freno : {self._tipoFreno}"

    # ________________Getter______________________________
    @property
    def _tipoFreno(self):
        return self.__tipoFreno

    # ________________Setter______________________________
    @_tipoFreno.setter
    def _tipoFreno(self, value):
        self.__tipoFreno = value


class Automovil(Vehiculo):
    def __init__(self, ruedas, tipoCombustible, tipoMotor):
        super().__init__(ruedas, tipoCombustible)
        self.__tipoMotor = tipoMotor

    def __str__(self):  # str que describe cada atributo
        return f"{super().__str__()}, Tipo de motor : {self._tipoMotor}"

    # ________________Getter______________________________
    @property
    def _tipoMotor(self):
        return self.__tipoMotor

    # ________________Setter______________________________
    def setTipoMotor(self, tipoMotor):
        self.__tipoMotor = tipoMotor


class BicicletaElectrica(Bicicleta, Automovil):
    def __init__(self, ruedas, tipoCombustible, tipoFreno, tipoMotor):
        Bicicleta.__init__(ruedas, tipoCombustible, tipoFreno)
        Automovil.__init__(ruedas, tipoCombustible, tipoMotor)

    def __str__(self):  # str que describe la la bicicleta y el tipo de motor
        return f"{Bicicleta.__str__(self)}, Tipo de motor : {self._tipoMotor}"


class asistenciaElectrica:
    def __init__(self) -> None:
        self.listaBici = []

    def mostrarBicis(self):  # metodo para mostrar los datos registrados
        if self.listaBici:
            print("\nLista de vehiculos")
            for bici in self.listaBici:
                print(bici)
        else:
            print("\n No hay vehiculos registrados")

    def registrarBici(self):
        ruedas = int(input("Cuantas ruedas tiene tu medio de transporte : "))
        combustible = input("Ingresa el tipo de combustible : ")
        freno = input("Ingresa el tipo de freno : ")
        motor = input("Ingresa el tipo de motor : ")

        bici_electrica = BicicletaElectrica(ruedas, combustible, freno, motor)
        self.listaBici.append(bici_electrica)

    def main(self):
        while True:
            while True:
                try:
                    opcionPanel = int(input("____________________________________________\n \n\
    Sistema de Gestión de habitaciones \n \n\
        1. Registrar Habitacion Normal - VIP \n\
        2. Mostrar habitaciones Actuales \n \n\
        3. Salir \n \n\
    Su opcion: "))
                except ValueError:
                    print("Caracter no valido")
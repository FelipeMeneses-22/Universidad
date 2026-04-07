class Pasajero:
    # Metodo constructor
    def __init__(self, nombre, telefono ,nacionalidad) -> None:
        self._nombre = nombre
        self._telefono = int(telefono)
        self._nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f"   ____________________________________________ \n\
            Nombre del pasajero : {self._nombre} \n\
            Telefono del pasajero : {self._telefono} \n\
            Nacionalidad : {self._nacionalidad}"

    # Metodos Getter
    @property
    def getNombre(self):
        return self._nombre
    @property
    def getTelefono(self):
        return self._telefono
    
    # Metodos Setter
    def setNombre(self, nombre):
        self._nombre = nombre
    def setTelefono(self, telefono):
        self._telefono = telefono
    def setNacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad
    

class PasajeroVip(Pasajero):
    def __init__(self, nombre, telefono ,nacionalidad, categoria):
        super().__init__(nombre, telefono ,nacionalidad)
        self._categoria = categoria

    # Metodos Getter
    @property
    def getCategoria(self):
        return self._categoria
    
    # Metodos Setter
    def setCategoria(self, categoria):
        self._categoria = categoria

class sistemaGestionVuelo:
    def __init__(self) -> None:
        self._pasajero = [] # Lista vacia de los pasajeros

    def guardarRegistro(self, pasajero):
        self._pasajero.append(pasajero) # Agregamos los datos del cliente

    def registrarPasajero(self):
        # Formulario de registro
        print("____________________________________________")
        nombre = input("    Ingrese su nombre : ")
        telefono = int(input("    Ingrese su telefono : "))
        nacionalidad = input("    Ingrese su nacionalidad : ")
        categoria = input("    ¿Su categoria es especial? (s/n) : ").lower()

        # Condicional para saber si es vip o no
        while True:
            if categoria == "s":
                clase = input("    ¿Que clase de categoria es? VIP - Master :").lower()
                pasajero = PasajeroVip(nombre, telefono, nacionalidad, clase)
                self.guardarRegistro(pasajero)
                break
            elif categoria == "n":
                pasajero = Pasajero(nombre, telefono, nacionalidad)
                self.guardarRegistro(pasajero)
                break
            else:
                print("    Elige un opcion valida, apreciado cliente :D")

    def mostrarPasajero(self):
        if not self._pasajero:
            print("____________________________________________ \n\
                No tenemos clientes jefe :(")

        else:
            for pasajero in self._pasajero:
                i = 0
                print(pasajero)

    def main (self):
        while True:
            while True:
                try:
                    opcionPanel = int(input("____________________________________________\n \n\
    Sistema de Gestión de Vuelos \n \n\
        1. Registrar Pasajero \n\
        2. Mostrar Pasajeros Actuales \n \n\
        3. Salir \n \n\
    Su opcion: "))
                    if 1 <= opcionPanel <= 3:
                        break
                    else:
                        print("\n    Opcion ingresada no valida.")
                except ValueError:
                    print("\n    Caracter ingresado no valido.")

            if opcionPanel == 1:
                self.registrarPasajero()
            elif opcionPanel == 2:    
                self.mostrarPasajero()
            elif opcionPanel == 3:
                print("____________________________________________\n\
    Saliste del panel, ten un buen dia. \n\
____________________________________________ \n \n")
                break
    
    

cliente1 = sistemaGestionVuelo()
cliente1.main()
#Enunciado: Crea un sistema para gestionar una concesionaria de vehículos. La clase Vehiculo debe contener los atributos marca, modelo y año. Crea una clase VehiculoDeLujo que herede de Vehiculo y agregue un atributo adicional de precio. Implementa setters y getters para cada atributo. El sistema debe permitir:

#Registrar vehículos.
#Registrar vehículos de lujo.
#Mostrar todos los vehículos.
#Mostrar los vehículos de lujo con su precio.
#Clases involucradas:

#Vehiculo: marca, modelo, año.
#VehiculoDeLujo: hereda de Vehiculo y añade precio.


# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 17/10/2024
# ----------------------------------------

#-------------clase base------------

class vehiculo:
    def __init__(self, marca, modelo, anio) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        
    def __str__(self) -> str:
        return f"marca: {self.getMarca}, modelo: {self.getModelo}, año: {self.getAnio}"
        
# --------SETTERS Y GETTERS--------------

    @property
    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    @property
    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    @property
    def getAnio(self):
        return self.__anio

    def setAnio(self, anio):
        self.__anio = anio
        
        
#-----------------clase hereda---------------

class VehiculoDeLujo(vehiculo):
    def __init__(self, marca, modelo, anio, precio) -> None:
        super().__init__(marca, modelo, anio)
        self.__precio = precio
        
    def __str__(self) -> str:
        return f"{super().__str__()}, precio: {self.getPrecio} "
    
# --------SETTERS Y GETTERS--------------
        
    @property
    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio):
        self.__precio = precio
        
#-----clase interaccion---------

class SistemaGestionVehiculos:
    def __init__(self):
        self.listaVehiculo =[]
        self.listaVehiculoDeLujo =[]
    
    def agregarVehiculo(self, vehiculo):
        self.listaVehiculo.append(vehiculo)
        print(f"El vehiculo se agrego con exito")
    
        
    def registrarVehiculo(self):
        marca = input("Ingrese la marca del vehiculo: ")
        try:
            modelo = input("Ingrese el modelo: ")
        except ValueError:
            print("caracter no valido")
        anio = int(input("Ingrese el año: "))
        valor = input("¿Es un vehiculo de lujo? (s/n)").lower()
        if valor == "s":
            precio = input("Ingrese el precio: ")
            nuevoVehiculo = VehiculoDeLujo(marca, modelo, anio, precio)
            self.agregarVehiculoDeLujo(nuevoVehiculo)
        else:
            nuevoVehiculo = vehiculo(marca, modelo, anio)
            self.agregarVehiculo(nuevoVehiculo)
    
        
    def agregarVehiculoDeLujo(self, vehiculoDeLujo):
        self.listaVehiculoDeLujo.append(vehiculoDeLujo)
        print(f"El vehiculo de lujo se agrego con exito")
     
    
    def mostrarVehiculo(self):
        if self.listaVehiculo:
            for vehiculo in self.listaVehiculo:
                print (vehiculo)
                
        else:
            print("No hay vehiculos")
    
    def mostrarVehiculosDeLujo(self):
        if self.listaVehiculoDeLujo:
            for vehiculoDeLujo in self.listaVehiculoDeLujo:
                print (vehiculoDeLujo)
                
        else:
            print("No hay vehiculos de lujo")
            
    def menu(self):    
        while True:
            print("\n  Bienvenido al sistema de gestion de vehiculos \n \n\
                    1. Registrar vehiculo \n\
                    2. Mostar lista de vehiculos  \n\
                    3. Mostar lista de vehiculos de lujo \n\
                    4. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarVehiculo()
            
            elif opcion == 2:
                self.mostrarVehiculo()
            
            elif opcion == 3:
                self.mostrarVehiculosDeLujo()
            
            elif opcion == 4:
                print("Saliendo del menú.")
                break
                
            else:
                print ("Opcion incorrecta")
                
                
#----------Inicializando el menu-----------------
sis = SistemaGestionVehiculos()
sis.menu()

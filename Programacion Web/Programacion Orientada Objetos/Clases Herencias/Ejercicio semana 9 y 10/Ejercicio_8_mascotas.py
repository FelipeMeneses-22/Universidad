#Enunciado: Desarrolla un sistema de gestión para una veterinaria. Crea una clase Mascota con los atributos nombre, especie y edad. La clase MascotaExotica hereda de Mascota y añade un atributo país de origen. Implementa setters y getters para todos los atributos. El menú debe permitir:


# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 17/10/2024
# ----------------------------------------

#-------------clase base------------

class Mascota:
    def __init__(self, nombre, especie, edad) -> None:
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        
    def __str__(self) -> str:
        return f"Nombre: {self.getNombre}, Especie: {self.getEspecie}, Edad: {self.getEdad}"
        
# --------SETTERS Y GETTERS--------------

    @property
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie

    @property
    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad
        
        
#-----------------clase hereda---------------
class MascotaExotica(Mascota):
    def __init__(self, nombre, especie, edad, paisOrigen):
        super().__init__(nombre, especie, edad)
        self.__paisOrigen = paisOrigen
        
    def __str__(self) -> str:
        return f"{super().__str__()}, fecha caducidad: {self.getPaisOrigen} "
    
# --------SETTERS Y GETTERS--------------
    @property
    def getPaisOrigen(self):
        return self.__paisOrigen

    def setPaisOrigen(self, pais):
        self.__paisOrigen = pais
        
#-----clase interaccion---------

class SistemaGestionMascotas:
    def __init__(self):
        self.listaMascotas =[]
        self.listaMascotasExoticas =[]
    
    # Metodo para guardar los datos de la mascota
    def agregarMascota(self, mascota):
        self.listaMascotas.append(mascota)
        print(f"La mascota {mascota.getNombre} se agrego con exito")
    
    def agregarMascotaExotica(self, mascotaExotica):
        self.listaMascotasExoticas.append(mascotaExotica)
        print(f"La mascota exotica {mascotaExotica.getNombre} se agrego con exito")
    
    #_________________________________________________________________________________
    
    # Metodo para registrar los datos de la mascota
    def registrarMascota(self):
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie: ")
        edad = int(input("Ingrese la edad: "))
        exotica = input("¿Es una mascota exotica? (s/n)").lower()
        if exotica == "s":
            paisOrigen = input("Ingrese el pais de origen: ")
            nuevaMascota = MascotaExotica(nombre, especie, edad, exotica, paisOrigen)
            self.agregarMascotaExotica(nuevaMascota)
        else:
            nuevaMascota = Mascota(nombre, especie, edad)
            self.agregarMascota(nuevaMascota)
    
    # Muestra las mascotas guardadas en la lista
    def mostrarMascota(self):
        if self.listaMascotas:
            for mascota in self.listaMascotas:
                print (mascota)
        else:
            print("No hay mascotas")
    
    def mostrarMascotasExotica(self):
        if self.listaMascotasExoticas:
            for mascotaExotica in self.listaMascotasExoticas:
                print (mascotaExotica)
        else:
            print("No hay mascotas exoticas")

    # Menu de interfaz para el usuario
    def menu(self):    
        while True:
            print("\n  Bienvenido al sistema de gestion de mascotas \n \n\
                    1. Registrar mascota \n\
                    2. Mostar lista de mascotas  \n\
                    3. Mostar lista de mascotas exoticas \n\
                    4. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarMascota()
            
            elif opcion == 2:
                self.mostrarMascota()
            
            elif opcion == 3:
                self.mostrarMascotasExotica()
            
            elif opcion == 4:
                print("Saliendo del menú.")
                break
                
            else:
                print ("Opcion incorrecta")
                
                
#----------Inicializando el menu-----------------
sis = SistemaGestionMascotas()
sis.menu()

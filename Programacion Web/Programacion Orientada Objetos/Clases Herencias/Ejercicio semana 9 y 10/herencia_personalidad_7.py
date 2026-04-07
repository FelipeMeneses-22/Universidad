# Enunciado: Crea un sistema para gestionar personalidades históricas. Define una clase PersonaHistorica que contenga el nombre y la fecha de nacimiento. Luego, crea una clase Cientifico que herede de PersonaHistorica y añada el campo de estudio, y una clase Artista que añada el tipo de arte. Finalmente, crea una clase CientificoArtista que herede de ambas, representando personas que hicieron aportes tanto a la ciencia como al arte.

# Clases involucradas:

# PersonaHistorica: nombre, fecha de nacimiento.
# Cientifico: hereda de PersonaHistorica y añade campo de estudio.
# Artista: hereda de PersonaHistorica y añade tipo de arte.
# CientificoArtista: hereda de Cientifico y Artista.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 30/10/2024
# ----------------------------------------

class PersonaHistorica: # clase padre
    def __init__(self, nombre, fecha_nacimiento): # metodo constructor
        self.__nombre = nombre  # atributo privado
        self.__fecha_nacimiento = fecha_nacimiento # atributo privado

    def __str__(self): # metodo para mostrar la informacion
        return f"Nombre : {self._nombre}, Fecha nacimiento : {self._fecha_nacimiento}"

# _____________getter y Setter usando @property___________________
    @property
    def _nombre(self):
        return self.__nombre
    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _fecha_nacimiento(self):
        return self.__fecha_nacimiento
    @_fecha_nacimiento.setter
    def _fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

class Cientifico(PersonaHistorica): #  clase hija
    def __init__(self, nombre, fecha_nacimiento, campo_estudio):
        super().__init__(nombre, fecha_nacimiento) # llamando al constructor de la clase padre
        self.__campo_estudio = campo_estudio # atributo protegido

    def __str__(self): # metodo para mostrar la informacion
        return f"{super().__str__()}, Campo que estudia : {self._campo_estudio}"

# _____________getter y Setter usando @property___________________
    @property
    def _campo_estudio(self):
        return self.__campo_estudio
    @_campo_estudio.setter
    def _campo_estudio(self, value):
        self.__campo_estudio = value

class Artista(PersonaHistorica): # clase hija
    def __init__(self, nombre, fecha_nacimiento, tipo_artista):
        super().__init__(nombre, fecha_nacimiento) # llamando al constructor de la clase padre
        self.__tipo_artista = tipo_artista # atributo privado

    def __str__(self):
        return f"{super().__str__()}, Tipo de artista: {self.__tipo_artista}"

# _____________getter y Setter usando @property___________________
    @property
    def _tipo_artista(self):
        return self.__tipo_artista
    @_tipo_artista.setter
    def _tipo_artista(self, value):
        self.__tipo_artista = value

class CientificoArtista(Cientifico, Artista): # clase hija
    def __init__(self, nombre, fecha_nacimiento):

        Cientifico.__init__(self, nombre, fecha_nacimiento,  campo_estudio=None) # llamando al constructor de la clase Cientifico
        Artista.__init__(self,  nombre, fecha_nacimiento, tipo_artista=None) # llamando al constructor de la clase padre


    def __str__(self): # metodo para mostrar la informacion
        return f"{Cientifico.__str__()},  {Artista.__str__()}"

class SistemaGestionCientifico: # clase encarga de lo dinamico
    def __init__(self): # metodo que se encarga de tener la lista
        self.cientificos = [] # Lista

    def  agregar_cientifico(self, cientifico): # metodo para guardar
        self.cientificos.append(cientifico) # agregando a la lista

    def registrarCientificos(self): # metodo para registrar los datos
        nombre = input("Ingrese el nombre del cientifico: ")
        fecha = input("Ingrese la fecha de nacimiento: ")
        elegir = int(input("Elige que eres \n 1) Cientifico \n 2) Artista \n 3)  Cientifico y Artista \n Opcion: "))

        # condicionales para  elegir la clase
        if elegir == 1:
            campo =  input("Ingrese el campo de estudio: ")
            cientifico = Cientifico(nombre, fecha, campo)
            self.agregar_cientifico(cientifico)# llamamos el metodo que guarda los datos
        elif  elegir == 2:
            tipo = input("Ingrese el tipo de artista: ")
            cientifico = Artista(nombre, fecha, tipo) 
            self.agregar_cientifico(cientifico)
        else:
            tipo = input("Ingrese el tipo de artista: ")
            campo =  input("Ingrese el campo de estudio: ")
            cientifico = CientificoArtista(nombre, fecha) #  si es 3 es la clase hija
            self.agregar_cientifico(cientifico)

    def  mostrar_cientificos(self): # metodo para mostrar los datos
        if self.cientificos:# comprobamos si hay datos almacenados
            for cientifico in self.cientificos: # recorriendo la lista
                print(cientifico) # mostrando los datos
        else:
            print("No hay cientificos registrados")

    def menu(self):
        while True:
            #  menu
            print("\nMenu de opciones")
            print("1) Registrar Cientifico")
            print("2) Mostrar Cientificos")
            print("3) Salir")
            
            while True:
                try: # controlamos el error por si ponen un caracter no valido
                    opcion = int(input("Ingrese la opcion que desee: "))
                    if 1 <= opcion <= 3:
                        break
                except  ValueError:
                    print("Error, ingrese un valor numerico")
            
            if  opcion == 1:
                self.registrarCientificos() # llamamos el metodo para registrar
            elif  opcion == 2:
                self.mostrar_cientificos() # llamamos el metodo para mostrar
            else:
                print("Gracias por utilizar el sistema")
                break # cerramos el bucle

cin = SistemaGestionCientifico()
cin.menu() # llamamos el metodo para iniciar el menu
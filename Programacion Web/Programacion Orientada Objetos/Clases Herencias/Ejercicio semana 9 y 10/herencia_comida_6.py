# Enunciado: Desarrolla un sistema para gestionar tipos de comida. Crea una clase Comida que contenga nombre y precio. Luego, crea una clase Vegetariana que herede de Comida y añada el atributo es_vegano, y una clase Rapida que añada el atributo tiempo_preparacion. Finalmente, crea una clase ComidaRapidaVegetariana que herede de ambas y represente platos que sean tanto vegetarianos como de preparación rápida.

# Clases involucradas:

# Comida: nombre, precio.
# Vegetariana: hereda de Comida y añade si es vegano o no.
# Rapida: hereda de Comida y añade tiempo de preparación.
# ComidaRapidaVegetariana: hereda de Vegetariana y Rapida.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 24/10/2024
# ----------------------------------------

class Comida:  # clase padre
    def __init__(self, nombre, precio):  # metodo constructor
        self.__nombre = nombre  # atributo principal
        self.__precio = float(precio)  # atributo principal

    def __str__(self):  # descripcion de la clase
        return f"Nombre : {self._nombre}, Precio : {self._precio}"

    # _____________getter y Setter usando @property___________________
    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value


class Vegetariana(Comida):
    def __init__(self, nombre, precio, es_vegano):
        super().__init__(nombre, precio)  # hereda los atributos de comida
        self.__es_vegano = es_vegano  # atributo protegido

    def __str__(self):  # descripcion de la clase
        return f"{super().__str__()}, Comida Vegana: {self._es_vegano}"

    # _____________getter y Setter usando @property___________________
    @property
    def _es_vegano(self):
        return self.__es_vegano

    @_es_vegano.setter
    def _es_vegano(self, value):
        self.__es_vegano = value

class Rapida(Comida):
    def __init__(self, nombre, precio, tiempo_preparacion):
        super().__init__(nombre, precio)
        self.__tiempo_preparacion = tiempo_preparacion  # atributo protegido

    def __str__(self):  # descripcion de la clase
        return f"{super().__str__()}, Tiempo de preparación: {self._tiempo_preparacion} minutos"

    # _____________getter y Setter usando @property___________________
    @property
    def _tiempo_preparacion(self):
        return self.__tiempo_preparacion

    @_tiempo_preparacion.setter
    def _tiempo_preparacion(self, value):
        self.__tiempo_preparacion = value

class ComidaRapidaVegetariana(Vegetariana, Rapida):
    def __init__(self, nombre, precio, es_vegano, tiempo_preparacion):
        Vegetariana.__init__(self, nombre,  precio, es_vegano)  # hereda los atributos de comida
        Rapida.__init__(self,  nombre, precio, tiempo_preparacion)  # hereda los atributos de comida rapida

    def __str__(self):  # descripcion de la clase
        return f"{Vegetariana.__str__(self)}, Tiempo de preparacion: {self._tiempo_preparacion}"

class GestionComida:
    def __init__(self):
        self.listaComida = []  # definimos la lista

    def guardarComida(self, comida):
        self.listaComida.append(comida)  # agregamos la comida a la lista

    def registrarComida(self):
        # ingresamos los datos basicos  de la comida
        nombre =  input("Ingrese el nombre de la comida: ")
        precio = float(input("Ingrese el precio de la comida: "))
        es_vegano = input("¿La comida es vegana? (s/n): ")

        # condicional para saber si es vegeana o no
        if es_vegano.lower() == "s":
            vegano = True
            tiempo = input("¿La comida es rapida? (s/n): ")
            if  tiempo.lower() == "s": #si la comida es rapida vegena
                tiempo_preparacion = int(input("Ingrese el tiempo de preparacion: "))
                comida = ComidaRapidaVegetariana(nombre, precio, vegano, tiempo_preparacion)
                self.guardarComida(comida) #guardamos los datos con el metodo
                #mensaje de confirmacion
                print(f"----------La comida  '{comida._nombre}' ha sido agregada a la lista--------")
            else:
                comida = Vegetariana(nombre, precio,  vegano)
                self.guardarComida(comida) #guardamos los datos con el metodo
                print(f"----------la comida '{vegano}' ha sido agregada a la lista----------")



        elif  es_vegano.lower() == "n":
            vegano  = False
            tiempo = input("¿La comida es rapida? (s/n): ")
            if tiempo.lower() == "s": #si la comida es rapida no vegana
                tiempo = True
                tiempo_preparacion = int(input("Ingrese el tiempo de preparacion: "))
                comida = Rapida(nombre, precio, tiempo_preparacion) #creamos
                self.guardarComida(comida) #guardamos los datos con el metodo
                #mensaje de confirmacion
                print(f"----------La comida  {comida._nombre} ha sido agregada a la lista........")
            else:
                comida = Comida(nombre, precio)
                self.guardarComida(comida) #guardamos los datos con el metodo
                #mensaje de confirmacion   
                print(f"--------La comida  '{comida._nombre}' ha sido agregada a la lista----------")

    def mostrarComida(self):  # metodo  para mostrar la lista de comidas
        if self.listaComida:  #  si la lista no esta vacia
            print("\n---------Listado de comidas----------")
            for idx,comida in enumerate(self.listaComida,1):
                print(f"{idx}. {comida}")
        else:
            print("No hay comida en la lista")

    def menu(self):
        while True:# bucle para repietir el menu hasta qeu le de salir
            while True:# bucle para que ponga numeros del 1 al 3 del menu
                try:# conttrolamos el error por si pone un caracter no valido
                    print("\n Menu \n")
                    print("1) Resgistrar comida")
                    print("2) Mostrar lista de comidas ")
                    print("3) Salir")

                    op = int(input("Seleccione la opcion que desea realizar: "))

                    if 1 <= op <= 3: # validamos datos si es del uno al 3
                        break# rompemos bucle
                    else:
                        print("Opcion invalida, por favor seleccione una opcion valida")
                except ValueError: 
                    print("caracter no valido")

            if op == 1:
                self.registrarComida()
            elif op == 2:
                self.mostrarComida()
            else:
                print("Gracias por utilizar el sistema")
                break

com = GestionComida()
com.menu()


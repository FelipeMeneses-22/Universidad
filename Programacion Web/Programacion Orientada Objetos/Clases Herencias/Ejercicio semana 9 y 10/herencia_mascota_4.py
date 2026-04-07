# Enunciado: Desarrolla un sistema para gestionar diferentes tipos de mascotas. Crea una clase Animal que contenga nombre y especie. Luego, crea dos clases, Perro y Gato, que hereden de Animal. La clase Perro debe añadir el atributo raza y la clase Gato debe añadir el atributo longitud_pelo. Finalmente, crea una clase PerroGato que herede de ambas, y que permita tener una mezcla de ambos animales.

# Clases involucradas:

# Animal: nombre, especie.
# Perro: hereda de Animal y añade raza.
# Gato: hereda de Animal y añade longitud del pelo.
# PerroGato: hereda de Perro y Gato, maneja ambos atributos.


# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 21/10/2024
# ----------------------------------------


class Animal: #clase base
    def __init__(self, nombre, especie):
        self.__nombre = nombre  # atributo protegido
        self.__especie = especie  # atributo protegido

    def __str__(self):
        return f"Nombre : {self.getNombre}, Especie : {self.getEspecie}"

    # _____________getter y Setter usando @property___________________
    @property
    def getNombre(self):
        return self.__nombre

    @getNombre.setter
    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def getEspecie(self):
        return self.__especie

    @getEspecie.setter
    def setEspecie(self, especie):
        self.__especie = especie


class Perro(Animal): # clase que hereda animal
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.__raza = raza  # atributo protegido

    def __str__(self):
        return f"{super().__str__()}, Raza : {self._raza}"

    # _____________getter y Setter___________________
    @property
    def _raza(self):
        return self.__raza

    @_raza.setter
    def _raza(self, raza):
        self.__raza = raza


class Gato(Animal): # clase que hereda animal
    def __init__(self, nombre, especie, longitud_pelo):
        super().__init__(nombre, especie)
        self.__longitud_pelo = longitud_pelo  # atributo protegido

    def __str__(self):
        return f"{super().__str__()}, Longitud del pelo : {self.longitud_pelo}cm"

    # _____________getter y Setter___________________
    @property
    def longitud_pelo(self):
        return self.__longitud_pelo

    @longitud_pelo.setter
    def longitud_pelo(self, longitud_pelo):
        self.__longitud_pelo = longitud_pelo 


class PerroGato(Perro, Gato):  # clase que herda perro y gato
    def __init__(self, nombre, especie, raza, longitud_pelo):
        Perro.__init__(self, nombre, especie, raza)
        Gato.__init__(self, nombre, especie, longitud_pelo)


class sistemaPerroGato():
    def __init__(self) -> None:
        self.listaAnimal = [] # Guarda el animal en la lista

    def guardarAnimal(self, animal):  # metodo para guardar los registros
        self.listaAnimal.append(animal)

    def registrarAnimal(self):  # metodo para registrar los datos
        print("---------------------------")
        nombre = input("Ingrese el nombre del animal : ").capitalize()
        especie = input("Ingrese la especie del animal : ").capitalize()
        tipo = input("¿El animal es perro o gato? p/g : ").lower()
        if tipo == "p":
            while True:  # bucle para que ponga un caracter valido
                try:  # manjeamos el error con un try para el el ususario no ingrese caracteres invalidos
                    raza = input("Ingrese la raza del perro : ")
                    break
                except ValueError:
                    print("Caracter no valido.")
            animal = Perro(nombre, especie, raza)
            self.guardarAnimal(animal)
        else:
            while True:  # bucle para que ponga un caracter valido
                try:  # manjeamos el error con un try para el el ususario no ingrese caracteres invalidos
                    longitud_pelo = int(
                        input("Ingrese la longitud del pelo en (cm) : ")
                    )
                    break
                except ValueError:
                    print("Caracter no valido.")
            animal = Gato(nombre, especie, longitud_pelo)
            self.guardarAnimal(animal)

    def mostrarAnimal(self):
        if self.listaAnimal:
            print("\n---------Listado de animales.---------")
            for animal in self.listaAnimal:
                print(animal)
        else:
            print("\n---------No hay animales registrados.---------")

    def main(self):
        while True: # bucle hasta que el usuario le de salir
            while True:# bucle para que el usuario no ponga un caracter no valido
                try:
                    print("\nMenú\n")
                    print("1) Regitrar animal ")
                    print("2) Mostrar animal ")
                    print("3) Salir del menu ")
                    op = int(input("Ingresa la opcion que deseas realizar : "))

                    if 1 <= op <= 3:
                        break
                except ValueError:
                    print("\n---------Caracter no valido.---------")

            # condicionales para las opciones
            if op == 1:
                self.registrarAnimal()
            elif op == 2:
                self.mostrarAnimal()
            else:
                print("Muchas gracias bro, vuelve pronto")
                break


aniaml = sistemaPerroGato()
aniaml.main()

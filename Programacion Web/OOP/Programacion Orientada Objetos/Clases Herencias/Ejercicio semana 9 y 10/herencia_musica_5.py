# Enunciado: Desarrolla un sistema para gestionar músicos. Define una clase Artista que contenga nombre y género musical. Luego, crea una clase Cantante que herede de Artista y añada el atributo registro_vocal, y una clase Instrumentista que añada el atributo instrumento. Finalmente, crea una clase MultiTalento que herede de ambas y permita que el artista cante y toque un instrumento.

# Clases involucradas:

# Artista: nombre, género musical.
# Cantante: hereda de Artista y añade registro vocal.
# Instrumentista: hereda de Artista y añade instrumento.
# MultiTalento: hereda de Cantante y Instrumentista.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 24/10/2024
# ----------------------------------------


class Artista:  # clase padre
    def __init__(self, nombre, genero) -> None:  # metodo constructor
        self.__nombre = nombre  # atributo privado
        self.__genero = genero  # atributo privado

    def __str__(self):
        return f"Nombre : {self.nombre}, Genero musical : {self.genero}"

    # _____________getter y Setter usando @property___________________
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value


class Cantante(Artista):  # clase hija
    def __init__(self, nombre, genero, registro_vocal) -> None:
        super().__init__(nombre, genero)  # hereda los atributos de artista
        self.__registro_vocal = registro_vocal  # atributo privado

    def __str__(self):
        return f"{super().__str__()}, Registro vocal : {self.registro_vocal}"

    # _____________getter y Setter usando @property___________________
    @property
    def registro_vocal(self):
        return self.__registro_vocal

    @registro_vocal.setter
    def registro_vocal(self, value):
        self.__registro_vocal = value


class Instrumentista(Artista):  # clase padre
    def __init__(self, nombre, genero, instrumento) -> None:
        super().__init__(nombre, genero)  # hereda los atributos de artista
        self.__instrumento = instrumento  # atributo privado

    # _____________getter y Setter usando @property___________________
    @property
    def _instrumento(self):
        return self.__instrumento

    @_instrumento.setter
    def _instrumento(self, value):
        self.__instrumento = value


class MultiTalento(Cantante, Instrumentista):  # clase multiple
    def __init__(self, nombre, genero, registro_vocal, instrumento) -> None:
        Cantante.__init__(self, nombre, genero, registro_vocal)  # clase cantante
        Instrumentista.__init__(
            self, nombre, genero, instrumento
        )  # clase instrumentista

    def __str__(
        self,
    ):  # descripcion del musico que tiene registro vocal y toca instrumeto
        return f"{Cantante.__str__(self)}, {Instrumentista.__str__(self)}"


class GestionMusica:
    def __init__(self):
        self.listaMusicos = []  # lista

    def regsitrarMusico(self):
        print(f"\nMenu de registro de musicos\n")
        nombre = input("Ingrese el nombre del artista : ").capitalize()
        genero = input("Ingrese el genero de la musica : ").capitalize()

        info = input(
            "¿Tiene registro vocal? s/n : "
        ).lower()  # pregunto si tiene registro vocal
        if info == "s":  # si tiene registro vocal
            print(  # pequeño menú que contiene los registros vocales
                "\n Registro vocal femenino \n Soprano \n Mezzosoprano \n Contralto \n ----------- \n Registro vocal masculino \n Tenor \n Barítono \n Bajo \n"
            )
            registro = input("Ingrese el registro vocal : ").capitalize()
            musico = Cantante(
                nombre, genero, registro
            )  # guardamos los datos en la lista
            self.guardarMusico(musico)  # llamamos el metodo para gaurdar los datos

        instru = input("¿Toca instrumentos? s/n : ").lower()
        if instru == "s":
            instrumento = input("Ingrese el instruento : ")
            musico = Instrumentista(
                nombre, genero, instrumento
            )  # guardamos los datos en la lista
            self.guardarMusico(musico)  # llamamos el metodo para gaurdar los datos

        elif registro == "s" and instrumento == "s":
            musico = MultiTalento(nombre, genero, registro, instrumento)
            self.guardarMusico(musico)  # llamamos el metodo para gaurdar los datos
        else:
            print("")

        self.guardarMusico(musico)  # llamamos el metodo para gaurdar los datos
        print(f"----------El artista {nombre} se guardo con exito----------")

    def guardarMusico(self, musico):  # metodo para guardar los datos en la lista
        self.listaMusicos.append(musico)

    def mostrarInformacion(self):
        if self.listaMusicos:  # comprobamos si la lista esta vacia o no
            print("\n ----------Listado de musicos----------")
            for musico in self.listaMusicos:
                print(musico)
        else:
            print("\n ----------No hay musicos guardados----------")

    def main(self):
        while True:
            while True:
                try:
                    print("\nMenú\n")
                    print("1) Regitrar Musico ")
                    print("2) Mostrar Musicos ")
                    print("3) Salir del menu ")
                    op = int(input("Ingresa la opcion que deseas realizar : "))

                    if 1 <= op <= 3:
                        break
                except ValueError:
                    print("\n---------Caracter no valido.---------")

            if op == 1:
                self.regsitrarMusico()
            elif op == 2:
                self.mostrarInformacion()
            elif op == 3:
                print("Gracias por usar nuestro sistema.")
                break
            else:
                print("Ingrese una opcion valiida")


mus = GestionMusica()
mus.main()

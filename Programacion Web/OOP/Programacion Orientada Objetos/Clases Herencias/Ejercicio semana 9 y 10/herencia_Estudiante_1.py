#Enunciado: Desarrolla un sistema que gestione estudiantes y trabajadores. Crea una clase Persona que contenga nombre y edad. Luego, crea dos clases, Estudiante y Trabajador, que hereden de Persona. Finalmente, crea una clase EstudianteTrabajador que herede de ambas, representando a una persona que estudia y trabaja. Implementa métodos que permitan mostrar si la persona está matriculada en un curso y también si tiene un empleo.

#Clases involucradas:

#Persona: nombre, edad.
#Estudiante: hereda de Persona y añade método matricular_curso().
#Trabajador: hereda de Persona y añade método obtener_empleo().
#EstudianteTrabajador: hereda de Estudiante y Trabajador, permite que una persona estudie y trabaje.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 18/10/2024
# ----------------------------------------

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
    
    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getEdad(self):
        return self.__edad



# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__matriculado = False

    def matricular_curso(self):
        self.__matriculado = True
        print(f"{self.getNombre} ha sido matriculado en un curso.")

    def esta_matriculado(self):
        return self.__matriculado

    def __str__(self):
        estado = "matriculado" if self.__matriculado else "no matriculado"
        return f"{super().__str__()}, Estado de estudiante: {estado}"


# Clase Trabajador que hereda de Persona
class Trabajador(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__empleo = None

    def obtener_empleo(self, trabajo):
        self.__empleo = trabajo
        print(f"{self.getNombre} ha obtenido un empleo como {trabajo}.")

    def tiene_empleo(self):
        return self.__empleo is not None

    def __str__(self):
        estado = f"Empleo: {self.__empleo}" if self.__empleo else "Desempleado"
        return f"{super().__str__()}, Estado de trabajador: {estado}"


# Clase EstudianteTrabajador que hereda de Estudiante y Trabajador (herencia múltiple)
class EstudianteTrabajador(Estudiante, Trabajador):
    def __init__(self, nombre, edad):
        Estudiante.__init__(self, nombre, edad)
        Trabajador.__init__(self, nombre, edad)

    def __str__(self):
        return f"{Estudiante.__str__(self)}, {Trabajador.__str__()}"


# ------- Sistema de gestión ---------
class SistemaGestion:
    def __init__(self):
        self.listaPersonas = []

    # Método para registrar estudiantes, trabajadores o ambos
    def registrar_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        es_trabajador = input("¿Es un trabajador? (s/n): ").lower()
        es_estudiante = input("¿Es un estudiante? (s/n): ").lower()

        if es_trabajador == "s" and es_estudiante == "s":
            persona = EstudianteTrabajador(nombre, edad)
        elif es_trabajador == "s":
            persona = Trabajador(nombre, edad)
        elif es_estudiante == "s":
            persona = Estudiante(nombre, edad)
        else:
            persona = Persona(nombre, edad)

        self.listaPersonas.append(persona)
        print(f"Persona '{persona.getNombre}' registrada con éxito.")

    # Mostrar todas las personas registradas
    def mostrar_personas(self):
        if self.listaPersonas:
            print("\nPersonas registradas:")
            for persona in self.listaPersonas:
                print(persona)
        else:
            print("\n-----------No hay personas registradas.----------")

    # Método para matricular a un estudiante en un curso
    def matricular_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante a matricular: ")
        for persona in self.listaPersonas:
            if isinstance(persona, Estudiante) and persona.getNombre == nombre:
                persona.matricular_curso()
                return
        print(f"No se encontró a ningún estudiante con el nombre {nombre}.")

    # Método para dar empleo a un trabajador
    def dar_empleo(self):
        nombre = input("Ingrese el nombre del trabajador: ")
        for persona in self.listaPersonas:
            if isinstance(persona, Trabajador) and persona.getNombre == nombre:
                trabajo = input("Ingrese el tipo de empleo: ")
                persona.obtener_empleo(trabajo)
                return
        print(f"No se encontró a ningún trabajador con el nombre {nombre}.")

    # Menú de interacción
    def menu(self):
        while True:
            print("\n  Menú del sistema de gestión: \n\
                    1. Registrar persona \n\
                    2. Mostrar todas las personas \n\
                    3. Matricular estudiante en un curso \n\
                    4. Dar empleo a un trabajador \n\
                    5. Salir")

            opcion = int(input("\nIngrese la opción que desea realizar: "))

            if opcion == 1:
                self.registrar_persona()

            elif opcion == 2:
                self.mostrar_personas()

            elif opcion == 3:
                self.matricular_estudiante()

            elif opcion == 4:
                self.dar_empleo()

            elif opcion == 5:
                print("Saliendo del sistema de gestión.")
                break

            else:
                print("Opción incorrecta.")


# ---------- Inicializando el sistema ---------------
sistema = SistemaGestion()
sistema.menu()
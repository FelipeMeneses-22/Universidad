# Enunciado: Crea un sistema de gestión de empleados en una empresa. Implementa dos clases: Empleado (que almacena nombre y salario) y Gerente (que hereda de Empleado y tiene un atributo adicional para su departamento). Usa setters y getters para todos los atributos. Crea un menú que permita:

# Registrar empleados.
# Registrar gerentes.
# Mostrar todos los empleados.
# Mostrar los gerentes con sus departamentos.
# Clases involucradas:
# Empleado: nombre, salario.
# Gerente: hereda de Empleado y añade departamento.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 17/10/2024
# ----------------------------------------


# -------------clase base------------
class Empleado:
    def __init__(self, nombre, salario) -> None:
        self.__nombre = nombre
        self.__salario = salario
        
    def __str__(self) -> str:
        return f"Nombre: {self.getNombre}, Salario: {self.getSalario}"
        
# --------SETTERS Y GETTERS--------------

    @property
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def getSalario(self):
        return self.__salario

    def setsalario(self, salario):
        self.__salario = salario


# -----------------clase hereda---------------
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento) -> None:
        super().__init__(nombre, salario)
        self.__departamento = departamento

    def __str__(self):
        return f"{super().__str__()}, Departamento : {self.__departamento}"

    @property
    def getDepartamento(self):
        return self.__departamento

    def departamento(self, departamento):
        self.__departamento = departamento


# -----clase interaccion---------

class sistemaGestionEmpleado:
    def __init__(self):
        self.listaEmleado =[]
        self.listaGerente =[]
    
    # Metodo para guardar los datos del registro
    def agregarEmpleado(self, empleado):
        self.listaEmleado.append(empleado)
        print(f"El empleado {empleado.getNombre} se agrego con exito")
    
    def agregarGerente(self, gerente):
        self.listaGerente.append(gerente)
        print(f"El gerente {gerente.getNombre} se agrego con exito")
    
    #_________________________________________________________________________________
    
    # Metodo para registrar los datos
    def registrarEmpleado(self):
        nombre = input("Ingrese el nombre del empleado: ")
        salario = input("Ingrese el salario: ")
        dep = input("¿Es gerente? (s/n)").lower()
        if dep == "s":
            departamento = input("Ingrese el departamento al que pertenece: ")
            nuevoEmpleado = Gerente(nombre, salario, departamento)
            self.agregarGerente(nuevoEmpleado)
        else:
            nuevoEmpleado = Empleado(nombre, salario)
            self.agregarEmpleado(nuevoEmpleado)
    
    # Muestra las empleados guardadas en la lista
    def mostrarEmpleado(self):
        if self.listaEmleado:
            for emple in self.listaEmleado:
                print (emple)
        else:
            print("No hay empleados")
    
    def mostrarGerente(self):
        if self.listaGerente:
            for gerente in self.listaGerente:
                print (gerente)
        else:
            print("\nNo hay gerentes")

    # Menu de interfaz para el usuario
    def menu(self):    
        while True:
            print("\n  Bienvenido al sistema de gestion de empleados \n \n\
                    1. Registrar Empleado/Gerente \n\
                    2. Mostar lista de Empleados  \n\
                    3. Mostar lista de Gerentes \n\
                    4. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarEmpleado()
            
            elif opcion == 2:
                self.mostrarEmpleado()
            
            elif opcion == 3:
                self.mostrarGerente()
            
            elif opcion == 4:
                print("Saliendo del menú.")
                break
                
            else:
                print ("Opcion incorrecta")


# ----------Inicializando el menu-----------------
sis = sistemaGestionEmpleado()
sis.menu()

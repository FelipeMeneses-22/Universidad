# Ejercicio 2_ Herencia de empleado y gerente, Crea una clase base de empleado con un constructor que inicialice  nombre,salario, puesto, luego crea una clase derivada gerente que añade un atributo adicional departamento 

class Empleado:
    def __init__(self, nombre, salario, puesto):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    def descripcionEmpleado(self):
        return f"\n\
                        Empleado : {self.nombre} \n\
                        Salario : {self.salario} \n\
                        Puesto : {self.puesto}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, puesto, departamento):
        super().__init__(nombre, salario, puesto)
        self.departamento = departamento

    def descripcionGerente(self):
        return f"_____________________________________________________________________________ \n\
                {self.descripcionEmpleado()} \n\
                        Departamento : {self.departamento} \n \n"
print("_____________________________________________________________________________\n ")
nombre = input("                        Ingrese el nombre del empleado : ")
salario = float(input("                        Ingrese el salario = "))
puesto = input("                        Ingrese el puesto : ")
departamento = input("                        El departamento al que pertenece : ")

gerente = Gerente(nombre, salario, puesto, departamento)

print(gerente.descripcionGerente())
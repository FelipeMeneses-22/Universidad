class Empleado:
    def __init__(self, nombre, saliro, puesto):
        self._nombre = nombre  # Atributo protegido
        self.__saliro = saliro  # Atributo privado
        self.__puesto = puesto  # Atributo privado

#________________________________________________________________________________

    # Métodos Setter
    def set_saliro(self, saliro):
        self.__saliro = saliro

    def set_puesto(self, puesto):
        self.__puesto = puesto

    # Métodos Getter
    @property
    def get_saliro(self):
        return self.__saliro
    
    @property
    def get_puesto(self):
        return self.__puesto
#________________________________________________________________________________

# Clase derivada
class Gerente(Empleado):
    def __init__(self, nombre, saliro, puesto, departamento):
        super().__init__(nombre, saliro, puesto)
        self.departamento = departamento

    def descripcion(self):
        return f"Nombre: {self._nombre}, Salario: {self.get_saliro}, Puesto: {self.get_puesto}, Departamento: {self.departamento}"

# Uso de las clases
mi_empleado = Gerente("Felipe", 10000, "servicio al cliente", "Ventas")
print(mi_empleado.descripcion())
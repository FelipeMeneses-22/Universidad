class Empleado:
    def __init__(self, nombre, salario, puesto) -> None:
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto
    
    def aumentarSalario(self, porcentaje):
        aumento = self.salario + (porcentaje / 100)
        self.salario += aumento
        

    def puesto_c(self,cambiarPuesto):
        self.puesto = cambiarPuesto
        return (f"El empleado {self.nombre} cambio de puesto a {self.puesto}")
    
empleado = Empleado(salario=1000, puesto="Chambeador", nombre="Felipe")

print(empleado.aumentarSalario(20))
print(empleado.puesto_c("Flojo"))


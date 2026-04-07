class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self._marca = marca  # Atributo protegido
        self.__modelo = modelo  # Atributo privado

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        # Llamamos correctamente al constructor de la clase padre pasando ambos argumentos
        super().__init__(marca, modelo)
        # Utilizamos self para acceder al método set_modelo
        self.set_modelo(modelo)

    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self.get_modelo()}"

# Creación de un objeto de la clase Coche
n1 = Coche("Toyota", "Corolla")
print(n1.descripcion())
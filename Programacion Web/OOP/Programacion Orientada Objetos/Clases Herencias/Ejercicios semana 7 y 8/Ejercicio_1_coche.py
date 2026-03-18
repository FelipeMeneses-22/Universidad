class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo protegido
        self.__modelo = modelo  # Atributo privado

    # Métodos Setter
    def set_modelo(self, modelo):
        self.__modelo = modelo

    # Métodos Getter
    @property
    def get_modelo(self):
        return self.__modelo

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, n_puertas):
        super().__init__(marca, modelo)
        self.n_puertas = n_puertas

    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self.get_modelo}, Número de puertas: {self.n_puertas}"

# Uso de las clases
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.descripcion())
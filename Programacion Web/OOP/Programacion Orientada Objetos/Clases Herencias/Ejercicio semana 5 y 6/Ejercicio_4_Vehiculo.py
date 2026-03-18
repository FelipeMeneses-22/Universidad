class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"_______________________________\n\
                La marca del coche es {self.marca} \n\
                La modelo del coche es {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puerta):
        super().__init__(marca, modelo)
        self.num_puerta = num_puerta

    def descripcion(self):
        return f"El {super().descripcion()}, tiene {self.num_puerta} puertas"

class Electrico(Coche):
    def __init__(self, marca, modelo, num_puerta, bateria):
        super().__init__(marca, modelo, num_puerta)
        self.bateria = bateria
        
    def descripcion(self):
        return f"{super().descripcion()}, y la bateria es {self.bateria}"

coche = Coche("Mazda", "Mazda 3", 2)
electro = Electrico("Tesla", "siver", 2, "electrica")

print(coche.descripcion())
print(electro.descripcion())


# Crea una clase Coche que tenga los atributos marca, modelo, año y kilometraje. Añade un método conducir que acepte como argumento la cantidad de kilómetros recorridos y actualice el kilometraje. Luego, crea otro método detalles_coche que devuelva una descripción del coche.


class Coche:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def conducir(self):
        km_recorrido = int(input("\n                        Kilometros recorridos : "))
        km_actualizado = self.kilometraje + km_recorrido
        
        return f"\n \n\
                        Kilometraje actual : {self.kilometraje} \n\
                        Kilometraje recorrido : {km_recorrido} \n\
                        Kilometros actualizados : {km_actualizado} \n\
_______________________________________________________________________\n"

class detallesCoche(Coche):
    def __init__(self, marca, modelo, anio, kilometraje):
        super().__init__(marca, modelo, anio, kilometraje)

    def __str__(self):
        return f"_______________________________________________________________________\n \n\
                        Descripción del coche - \n\
                        Marca : {self.marca} \n\
                        Modelo : {self.modelo} \n\
                        Año : {self.anio} \n\
_______________________________________________________________________"



coche1 = Coche(input("_______________________________________________________________________\n \n                        Ingrese la marca del coche: "), input("                        Ingrese el modelo del coche: "), int(input("                        Ingrese el año del coche : ")), int(input("                        Ingrese el kilometraje del coche : ")))

print(coche1.__str__(), coche1.conducir())
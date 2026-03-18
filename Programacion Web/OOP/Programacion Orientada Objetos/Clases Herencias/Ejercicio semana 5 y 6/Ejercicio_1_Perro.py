class Animal:
    def __init__(self, nombre, ) -> None:
        self.nombre = nombre

    def hablar(self):
        return f"El animal hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau Guau"

perro1= Perro("Bat")

print(perro1.nombre)
print(perro1.hablar())
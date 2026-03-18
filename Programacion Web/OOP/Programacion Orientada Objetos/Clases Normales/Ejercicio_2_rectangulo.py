#Ejercicio 2
#Definimos la clase
class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def calcularArea(self):
        return self.ancho * self.altura
    
    def calcularPerimetro(self):
        return 2 * (self.ancho + self.altura)

rectangulo = Rectangulo(20,30)


print(f"El area es de {rectangulo.calcularArea()}")
print(f"El perimetro es {rectangulo.calcularPerimetro()}")
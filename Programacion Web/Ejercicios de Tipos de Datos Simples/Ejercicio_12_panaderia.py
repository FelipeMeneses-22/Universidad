# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

class panaderia:
    def __init__(self) -> None:
        self.panBueno = 3.49
        self.panViejo = .60
        

    def ventas(self):
        panAyer = input("Ingrese la cantidad de oan viejo vendido ")

    
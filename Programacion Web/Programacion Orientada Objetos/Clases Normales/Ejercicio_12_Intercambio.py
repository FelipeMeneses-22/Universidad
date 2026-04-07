

# Casa de cambio

# Ejercicio 1
# Desarrolla un programa en Python que implemente un sistema de conversión de monedas entre diferentes divisas usando clases y funciones. El objetivo es crear una clase que permita convertir entre distintas monedas y gestionar el tipo de cambio. El programa debe cumplir con los siguientes requisitos:

# 1. Clase ConversorMonedas:
# - La clase debe poder recibir la cantidad de dinero y el tipo de moneda de origen. OK
# - Debe incluir un método que permita convertir el valor recibido a cualquier otra moneda deseada. OK
# - El programa debe manejar al menos cinco tipos de monedas (por ejemplo, USD, EUR, MXN, JPY, GBP). OK
# - Debe generar mensajes de información sobre los objetos creados y los resultados de las conversiones. OK

# 2. Menú Interactivo: OK
# - El programa debe incluir un menú que permita al usuario: OK
# - Convertir una cantidad de dinero de una moneda a otra. OK
# - Mostrar los tipos de monedas soportadas y sus tasas de conversión. OK
# - Salir del programa. OK
# - El menú debe capturar y validar la información ingresada por el usuario, como la cantidad a convertir, la moneda de origen y la moneda destino. OK

# 3. Requisitos Adicionales:
# - Utiliza un diccionario o estructura similar para gestionar las tasas de conversión. OK
# - El sistema debe proporcionar un mensaje adecuado en caso de que el usuario introduzca una moneda no soportada. OK
# - El programa debe estar diseñado de manera que sea fácil agregar nuevas monedas o modificar las tasas de cambio en el futuro. 
# Implementa las funciones y la clase necesarias para cumplir con estos requisitos y asegúrate de que el programa sea fácil de usar y comprensible para el usuario final


# class ConversorMonedas:  
#     def _init_(self):
#         self.monedasExistentes = ["USD", "EUR", "MXN", "JPY", "GBP"]
#         self.tasasConversion = {
#             "USD": 4153.95,
#             "EUR": 4637.08,
#             "MXN": 214.14,
#             "JPY": 28.88,
#             "GBP": 5530.65
#         }

class ConversorMonedas:
    def __init__(self):
        # Diccionario que contiene las tasas de cambio con respecto al dólar estadounidense (USD)
        self.tasas_cambio = {
            'USD': 1.0,
            'EUR': 0.85,
            'MXN': 20.0,
            'JPY': 110.0,
            'GBP': 0.75
        }
    
    def convertir(self, cantidad, moneda_origen, moneda_destino):
        # Validar si las monedas están soportadas
        if moneda_origen not in self.tasas_cambio:
            return f"Moneda de origen '{moneda_origen}' no soportada."
        if moneda_destino not in self.tasas_cambio:
            return f"Moneda de destino '{moneda_destino}' no soportada."
        
        # Convertir a USD y luego a la moneda destino
        cantidad_usd = cantidad / self.tasas_cambio[moneda_origen]
        cantidad_convertida = cantidad_usd * self.tasas_cambio[moneda_destino]
        
        return f"{cantidad} {moneda_origen} son {cantidad_convertida:.2f} {moneda_destino}."
    
    def mostrar_monedas(self):
        print("Monedas soportadas y sus tasas de conversión con respecto a USD:")
        for moneda, tasa in self.tasas_cambio.items():
            print(f"{moneda}: {tasa}")

def menu():
    conversor = ConversorMonedas()
    
    while True:
        print("\n--- Menú de Conversión de Monedas ---")
        print("1. Convertir moneda")
        print("2. Mostrar monedas soportadas")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            cantidad = float(input("Introduce la cantidad de dinero: "))
            moneda_origen = input("Introduce la moneda de origen (USD, EUR, MXN, JPY, GBP): ").upper()
            moneda_destino = input("Introduce la moneda de destino (USD, EUR, MXN, JPY, GBP): ").upper()
            resultado = conversor.convertir(cantidad, moneda_origen, moneda_destino)
            print(resultado)
        
        elif opcion == '2':
            conversor.mostrar_monedas()
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor selecciona nuevamente.")

# Ejecutar el menú interactivo
menu()
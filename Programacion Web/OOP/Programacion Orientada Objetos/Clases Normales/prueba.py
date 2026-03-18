class ConversorMonedas:  
    def _init_(self):
        self.monedasExistentes = ["USD", "EUR", "MXN", "JPY", "GBP"]
        self.tasasConversion = {
            "USD": 4153.95,
            "EUR": 4637.08,
            "MXN": 214.14,
            "JPY": 28.88,
            "GBP": 5530.65
        }

    def convertirMoneda (self):
        while True:
            origenMoneda = input (f"_________________________ z\n \n\
    Ingrese el origen de su moneda {self.monedasExistentes}: ").upper()
            if origenMoneda in self.monedasExistentes:
                break
            else:
                print("\n    La moneda que estas ingresando no se encuentra en las opciones.")
        
        while True:
            try:
                cantidadDinero = float(input("\n\
    Digite la cantidad de dinero en los pesos del origen: "))
                if cantidadDinero > 0:
                    break
                else:
                    print("\n    Para que quieres converir 0 o un numero negativo?")
            except ValueError:
                print("\n    Digite un caracter valido, ingresaste un caracter de textos.")

        tasaMoneda = self.tasasConversion[origenMoneda]
        conversionDinero = cantidadDinero * tasaMoneda
        return(f"\n    El cambio de pesos {origenMoneda} a pesos COP es {conversionDinero}")
    
    def actualizarTasas(self):
        while True:
            print(f"_________________________ \n \n\
    Monedas Actuales \n\
    {self.monedasExistentes}")
            monedaActualizar = input("\n    Ingrese el nombre de la moneda que desea cambiar: ").upper()
            if monedaActualizar in self.monedasExistentes:
                nuevaTasa = float(input(f"\n    Ingrese la tasa actualizada para {monedaActualizar}: "))
                self.tasasConversion[monedaActualizar] = nuevaTasa
                print(f"_________________________ \n \n\
    La tasa de {monedaActualizar} fue actualizada a {nuevaTasa}.")
                break
            else:
                print("\n    La moneda que estas ingresando no se encuentra en el listado.")

    def agregarMonedas(self):
        while True:
            try:
                cantidadMonedas = int(input("_________________________ \n \n\
    Digite la cantidad de monedas que desea ingresar (Maximo 3): "))
                if 1 <= cantidadMonedas <= 3:
                    break
                else:
                    print("\n    La cantidad que estas ingresando no es valida")
            except ValueError:
                print("\n    Estas ingresando un caracter no valido")
                
        for i in range(cantidadMonedas):
            while True:
                try:
                    monedaNueva = input(f"\n    Digite el nombre de la nueva moneda: ").upper()
                    if not monedaNueva in self.monedasExistentes:
                        break
                    else:
                        print("\n    La moneda que estas ingresando ya esta en el listado \n\
_________________________")
                except ValueError:
                    print("\n    El caracter ingresado no es valido\n\
_________________________")
                    
            while True:
                try:
                    tasaNueva = float(input("\n    Digite la tasa de la nueva moneda: "))
                    if tasaNueva > 0:
                        self.tasasConversion[monedaNueva] = tasaNueva
                        print(f"\n    Moneda ingresada con exito \n\
    Ingresaste la moneda {monedaNueva} con la tasa de {tasaNueva}.")
                        break
                    else:
                        print("\n    Ingresaste un valor menor o igual a 0, no es valido.")
                except ValueError:
                        print("\n    Ingresaste un valor inadecuado.")
        
    def _str_(self):
        tasasActuales ="a".join([f"    El valor de la moneda {moneda} en pesos COP es {tasa}"
            for moneda, tasa in self.tasasConversion.items()])
        return f"_________________________ \n \n\
    Las actuales monedas del listado son: \n\
    {self.monedasExistentes} \n \n{tasasActuales}"

conversorMoneda = ConversorMonedas()

def main ():
    print("_________________________ \n \n\
    Bienvenido al panel de cambios de monedas \n\
        Opciones que se pueden realizar: \n\
            1. Convertir monedas a pesos COP\n\
            2. Consultar monedas y tasas \n\
            3. Agregar monedas con tasas\n\
            4. Actualizar monedas existentes \n\
            5. Salir del menu")

    while True:
        try:
            opcionPanel = int(input("\n        Ingrese que opcion desea realizar: "))
            if 1 <= opcionPanel <= 5:
                break
            else:
                print("\n    Ingresaste una opcion que no se encuentra en el panel.")
        except ValueError:
            print("\n    Digitaste un caracter no valido en el panel.")

    if opcionPanel == 1:
        print(conversorMoneda.convertirMoneda())
    elif opcionPanel == 2:
        print(conversorMoneda)
    elif opcionPanel == 3:
        conversorMoneda.agregarMonedas()
    elif opcionPanel == 4:
        conversorMoneda.actualizarTasas()
    elif opcionPanel == 5:
        return opcionPanel

while True:
    opcionesPanel = main()

    if opcionesPanel == 5:
        print("_________________________ \n \n\
    Saliste del panel, ten una buena tarde \n\
_________________________ \n \n")
        break
# Enunciado: Desarrolla un sistema para gestionar diferentes tipos de cuentas bancarias. Crea una clase CuentaBancaria que contenga número de cuenta y saldo. Luego, crea una clase CuentaCorriente que herede de CuentaBancaria y añada el atributo sobregiro, y una clase CuentaAhorro que añada el atributo tasa_interes. Finalmente, crea una clase CuentaMixta que herede de ambas, permitiendo manejar tanto la funcionalidad de una cuenta corriente como de ahorro.

# Clases involucradas:

# CuentaBancaria: número de cuenta, saldo.
# CuentaCorriente: hereda de CuentaBancaria y añade sobregiro.
# CuentaAhorro: hereda de CuentaBancaria y añade tasa de interés.
# CuentaMixta: hereda de CuentaCorriente y CuentaAhorro.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 30/10/2024
# ----------------------------------------

class  CuentaBancaria: # clase padre
    def __init__(self, numero_cuenta, saldo): # metodo cosntructor
        self.__numero_cuenta = numero_cuenta  # atributo protegido
        self.__saldo = saldo # atributo protegido

    def __str__(self): # str para describir los datos
        return f"Nombre:  {self.__numero_cuenta}, Saldo: {self.__saldo}"

# _____________getter y Setter usando @property___________________
    @property
    def _numero_cuenta(self):
        return self.__numero_cuenta
    @_numero_cuenta.setter
    def _numero_cuenta(self, value):
        self.__numero_cuenta = value

    @property
    def _saldo(self):
        return self.__saldo
    @_saldo.setter
    def _saldo(self, value):
        self.__saldo = value

class  CuentaCorriente(CuentaBancaria): # clase hija
    def __init__(self, numero_cuenta, saldo, sobregiro): # metodo constructor
        super().__init__(numero_cuenta, saldo) # herencia de la clase padre
        self.__sobregiro = sobregiro  # atributo protegido

    def __str__(self): # str para describir los datos
        return f"{super().__str__()},  Sobregiro: {self.__sobregiro}"

# _____________getter y Setter usando @property___________________
    @property
    def _sobregiro(self):
        return self.__sobregiro
    @_sobregiro.setter
    def _sobregiro(self, value):
        self.__sobregiro = value

class   CuentaAhorro(CuentaBancaria): # clase hija
    def __init__(self, numero_cuenta, saldo, tasa_interes): # metodo
        super().__init__(numero_cuenta, saldo) # herencia de la clase padre
        self.__tasa_interes = tasa_interes # atributo protegido

    def __str__(self):
        return f"{super().__str__()},  Tasa de interes: {self.__tasa_interes}%"


# _____________getter y Setter usando @property___________________
    @property
    def _tasa_interes(self):
        return self.__tasa_interes
    @_tasa_interes.setter
    def _tasa_interes(self, value):
        self.__tasa_interes = value

class CuentaMixta(CuentaCorriente, CuentaAhorro):
    def __init__(self, numero_cuenta, saldo):
        CuentaCorriente.__init__(self, numero_cuenta, saldo, sobregiro=None)
        CuentaAhorro.__init__(self, numero_cuenta, saldo, tasa_interes=None)
    
    def  __str__(self): # mostramos las descripciones de cada clase
        return f"{CuentaCorriente.__str__()}, Tasa de interes: {self.__tasa_interes}%"

class GestionCuenta:
    def __init__(self):
        self.listaCuenta = [] # lista
    
    def  agregarCuenta(self, cuenta): # metodo para agregar cuenta
        self.listaCuenta.append(cuenta) # agregar cuenta a la lista
    
    def registrarCuenta(self):
        numero_cuenta = input("Ingrese el numero de cuenta: ")
        saldo = float(input("Ingrese el saldo: "))

        elige = int(input("Elige el tipo de cuenta \n 1) Cuenta Ahorro \n 2)  Cuenta Corriente \n 3) Cuenta Mixta: \n Opcion: "))

        if  elige == 1:
            tasa_interes = float(input("Ingrese la tasa de interes: "))
            cuenta = CuentaAhorro(numero_cuenta, saldo, tasa_interes) 
            self.agregarCuenta(cuenta) # llamamos  al metodo para agregar cuenta
        elif  elige == 2:
            sobregiro = float(input("Ingrese el sobregiro: "))
            cuenta = CuentaCorriente(numero_cuenta, saldo, sobregiro)
            self.agregarCuenta(cuenta) # llamamos  al metodo para agregar cuenta
        
        else:
            tasa_interes = float(input("Ingrese la tasa de interes: "))
            sobregiro = float(input("Ingrese el sobregiro: "))
            cuenta = CuentaMixta(numero_cuenta, saldo)

            self.agregarCuenta(cuenta) # llamamos  al metodo para agregar cuenta
        
    def  mostrarCuentas(self):
        if self.listaCuenta: # comprobamos si hay cuentas registradas
            print("Lista de cuentas") 
            for cuenta in self.listaCuenta: # iteramos cada  cuenta en la lista
                print(cuenta)
        else:
            print("No hay cuentas registradas")
    
    def menu(self):
        while True:
            print("\nMenu de opciones")
            print("1) Registrar Cuentas")
            print("2) Mostrar Cuentas")
            print("3) Salir")

            while True:
                try:
                    opcion = int(input("Ingrese la opcion: "))
                    if 1 <= opcion <=  3:
                        break
                except  ValueError:
                    print("Error, ingrese un valor numerico")

            if  opcion == 1:
                self.registrarCuenta()
            
            elif opcion == 2:
                self.mostrarCuentas()
            
            else:
                print("Gracias por utilizar el sistema")
                break

cu =  GestionCuenta()
cu.menu() 


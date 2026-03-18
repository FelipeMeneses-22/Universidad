#Enunciado: Crea un sistema de gestión para cuentas bancarias. La clase Cuenta debe contener los atributos número de cuenta y saldo. Crea una clase CuentaCorriente que herede de Cuenta y añada un atributo de límite de sobregiro. Implementa setters y getters para todos los atributos. El menú debe permitir:

#Registrar cuentas.
#Registrar cuentas corrientes.
#Mostrar todas las cuentas.
#Actualizar el saldo y el límite de sobregiro.
#Clases involucradas:

#uenta: número de cuenta, saldo.
#CuentaCorriente: hereda de Cuenta y añade límite de sobregiro.



# ------------clase base------------
class Cuenta:
    def __init__(self, numero_cuenta, saldo) -> None:
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        
    def __str__(self) -> str:
        return f"Número de Cuenta: {self.getNumeroCuenta}, Saldo: {self.getSaldo}"

    # --------SETTERS Y GETTERS--------------
    @property
    def getNumeroCuenta(self):
        return self.__numero_cuenta

    def setNumeroCuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    @property
    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo


# -----------------clase que hereda---------------
class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, saldo, sobregiro) -> None:
        super().__init__(numero_cuenta, saldo)
        self.__sobregiro = sobregiro

    def __str__(self):
        return f"{super().__str__()}, Límite de Sobregiro: {self.__sobregiro}"

    @property
    def getSobregiro(self):
        return self.__sobregiro

    def setSobregiro(self, sobregiro):
        self.__sobregiro = sobregiro


# -----clase de interacción---------
class SistemaBancario:
    def __init__(self):
        self.listaCuentas = []
        self.listaCuentasCorrientes = []
    
    # Método para agregar cuentas a la lista
    def agregarCuenta(self, cuenta):
        self.listaCuentas.append(cuenta)
        print(f"La cuenta '{cuenta.getNumeroCuenta}' se agregó con éxito")
    
    def agregarCuentaCorriente(self, cuenta_corriente):
        self.listaCuentasCorrientes.append(cuenta_corriente)
        print(f"La cuenta corriente '{cuenta_corriente.getNumeroCuenta}' se agregó con éxito")
    
    # Método para registrar una cuenta o cuenta corriente
    def registrarCuenta(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        saldo = float(input("Ingrese el saldo de la cuenta: "))
        es_corriente = input("¿Es una cuenta corriente? (s/n): ").lower()
        
        if es_corriente == "s":
            sobregiro = float(input("Ingrese el límite de sobregiro: "))
            nuevaCuenta = CuentaCorriente(numero_cuenta, saldo, sobregiro)
            self.agregarCuentaCorriente(nuevaCuenta)
        else:
            nuevaCuenta = Cuenta(numero_cuenta, saldo)
            self.agregarCuenta(nuevaCuenta)
    
    # Mostrar las cuentas y cuentas corrientes registradas
    def mostrarCuentas(self):
        if self.listaCuentas:
            print("\nCuentas registradas:")
            for cuenta in self.listaCuentas:
                print(cuenta)
        else:
            print("\nNo hay cuentas registradas.")

    # 
    def mostrarCuentasCorrientes(self):
        if self.listaCuentasCorrientes:
            print("\nCuentas corrientes registradas:")
            for cuenta_corriente in self.listaCuentasCorrientes:
                print(cuenta_corriente)
        else:
            print("\nNo hay cuentas corrientes registradas.")
    
    # Método para actualizar el saldo y el límite de sobregiro
    def actualizarCuenta(self):
        numero_cuenta = input("Ingrese el número de cuenta para actualizar: ")
        for cuenta in self.listaCuentas + self.listaCuentasCorrientes:
            if cuenta.getNumeroCuenta == numero_cuenta:
                nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
                cuenta.setSaldo(nuevo_saldo)
                if isinstance(cuenta, CuentaCorriente):
                    nuevo_sobregiro = float(input("Ingrese el nuevo límite de sobregiro: "))
                    cuenta.setSobregiro(nuevo_sobregiro)
                print("La cuenta ha sido actualizada.")
                return
        print("La cuenta no fue encontrada.")
    
    # Menú de interacción con el usuario
    def menu(self):
        while True:
            print("\n  Bienvenido al sistema de gestión bancaria \n \n\
                    1. Registrar Cuenta/Cuenta Corriente \n\
                    2. Mostrar lista de Cuentas \n\
                    3. Mostrar lista de Cuentas Corrientes \n\
                    4. Actualizar Saldo y Límite de Sobregiro \n\
                    5. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarCuenta()
            
            elif opcion == 2:
                self.mostrarCuentas()
            
            elif opcion == 3:
                self.mostrarCuentasCorrientes()
            
            elif opcion == 4:
                self.actualizarCuenta()
            
            elif opcion == 5:
                print("Saliendo del menú.")
                break
                
            else:
                print("Opción incorrecta")


# ----------Inicializando el menú-----------------
sisBancario = SistemaBancario()
sisBancario.menu()
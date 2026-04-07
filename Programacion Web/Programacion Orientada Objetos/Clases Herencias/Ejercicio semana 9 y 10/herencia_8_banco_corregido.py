class CuentaBancaria:
    def _init_(self, numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente o cantidad inválida.")

    def _str_(self):
        return f"Cuenta {self.numero_cuenta} - Saldo: {self.saldo}"


class CuentaCorriente(CuentaBancaria):
    def _init_(self, numero_cuenta, saldo=0, sobregiro=0):
        super()._init_(numero_cuenta, saldo)
        self.sobregiro = sobregiro

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= (self.saldo + self.sobregiro):
            self.saldo -= cantidad
        else:
            print("Saldo y sobregiro insuficientes o cantidad inválida.")

    def _str_(self):
        return f"Cuenta Corriente {self.numero_cuenta} - Saldo: {self.saldo}, Sobregiro: {self.sobregiro}"


class CuentaAhorro(CuentaBancaria):
    def _init_(self, numero_cuenta, saldo=0, tasa_interes=0.02):
        super()._init_(numero_cuenta, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa_interes

    def _str_(self):
        return f"Cuenta Ahorro {self.numero_cuenta} - Saldo: {self.saldo}, Tasa de Interés: {self.tasa_interes * 100}%"


class CuentaMixta(CuentaCorriente, CuentaAhorro):
    def _init_(self, numero_cuenta, saldo=0, sobregiro=0, tasa_interes=0.02):
        CuentaCorriente._init_(self, numero_cuenta, saldo, sobregiro)
        CuentaAhorro._init_(self, numero_cuenta, saldo, tasa_interes)

    def _str_(self):
        return f"Cuenta Mixta {self.numero_cuenta} - Saldo: {self.saldo}, Sobregiro: {self.sobregiro}, Tasa de Interés: {self.tasa_interes * 100}%"


class GestionCuenta:
    def _init_(self):
        self.listaCuenta = []

    def agregarCuenta(self, cuenta):
        self.listaCuenta.append(cuenta)

    def registrarCuenta(self):
        numero_cuenta = int(input("Ingrese el número de cuenta: "))
        saldo = float(input("Ingrese el saldo: "))

        elige = int(
            input(
                "Elige el tipo de cuenta:\n 1) Cuenta Ahorro\n 2) Cuenta Corriente\n 3) Cuenta Mixta\nOpción: "
            )
        )

        if elige == 1:
            tasa_interes = float(input("Ingrese la tasa de interés: "))
            cuenta = CuentaAhorro(numero_cuenta, saldo, tasa_interes)
            self.agregarCuenta(cuenta)

        elif elige == 2:
            sobregiro = float(input("Ingrese el sobregiro: "))
            cuenta = CuentaCorriente(numero_cuenta, saldo, sobregiro)
            self.agregarCuenta(cuenta)

        elif elige == 3:
            tasa_interes = float(input("Ingrese la tasa de interés: "))
            sobregiro = float(input("Ingrese el sobregiro: "))
            cuenta = CuentaMixta(numero_cuenta, saldo, sobregiro, tasa_interes)
            self.agregarCuenta(cuenta)

        else:
            print("Opción no válida.")

    def mostrarCuentas(self):
        if self.listaCuenta:
            print("Lista de cuentas:")
            for cuenta in self.listaCuenta:
                print(cuenta)
        else:
            print("No hay cuentas registradas.")

    def menu(self):
        while True:
            print("\nMenú de opciones")
            print("1) Registrar Cuentas")
            print("2) Mostrar Cuentas")
            print("3) Salir")

            while True:
                try:
                    opcion = int(input("Ingrese la opción: "))
                    if 1 <= opcion <= 3:
                        break
                except ValueError:
                    print("Error, ingrese un valor numérico.")

            if opcion == 1:
                self.registrarCuenta()
            elif opcion == 2:
                self.mostrarCuentas()
            else:
                print("Gracias por utilizar el sistema.")
                break


# Ejecución del menú
gestion_cuenta = GestionCuenta()
gestion_cuenta.menu()

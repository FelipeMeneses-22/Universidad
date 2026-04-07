class Cajero:
    def __init__(self, nombre, saldo=0) -> None:
        self.nombre = nombre
        self.saldo = saldo

    # metodo para retirar
    def retirar(self,cantidad):
        if cantidad <= self.saldo: 
            self.saldo -= cantidad
            # imprimo una breve descripcion sobre el retiro del dinero
            print(f"La cantidad a retirara es de {cantidad}  su saldo actual es : {self.saldo}")
        else:
            print("Eres pobreton")

    # metodo para depositar
    def depositar(self,cantidad):
        if cantidad <= 0:
            print("No puede depositar una cantidad menos o igual a cero")
        else:
            self.saldo += cantidad
            print(f"Su saldo actual es de {self.saldo} La cantidad que deposito fue de {cantidad}")
            return 

    # metodo para consultar el saldo
    def consultarSaldo(self):
        print(f"Saldo actual {self.saldo}")

cuenta = Cajero("Felipe", 200)

cuenta.depositar(100)
cuenta.retirar(10)
cuenta.consultarSaldo()

print(cuenta.consultarSaldo)
class Vehicle:
    def __init__(self, numero_cuenta, nombre, balance):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance = self.balance + monto


cuenta = Vehicle("123456789", "yessenia", 5000)

cuenta.generar_balance()
cuenta.depositar(500)
cuenta.generar_balance()
cuenta.depositar(400)
cuenta.generar_balance()
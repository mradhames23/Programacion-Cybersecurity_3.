class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Depósito exitoso. Nuevo balance: {self.balance}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
        elif monto > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= monto
            print(f"Retiro exitoso. Nuevo balance: {self.balance}")

# Ejemplo de uso
cuenta1 = CuentaBancaria("Radhames", 5050)
cuenta1.depositar(1000)
cuenta1.retirar(10000)
cuenta1.retirar(1500)

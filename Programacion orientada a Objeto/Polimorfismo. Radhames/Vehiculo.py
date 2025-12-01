# Clase base
class Vehiculo:
    def mover(self):
        return "El vehículo se está moviendo."


# Clase hija: Carro
class Carro(Vehiculo):
    def mover(self):
        return "El carro avanza usando su motor."


# Clase hija: Bicicleta
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta avanza mediante pedaleo."


# Ejemplo de uso (polimorfismo)
vehiculos = [Carro(), Bicicleta(), Vehiculo()]

for v in vehiculos:
    print(v.mover())

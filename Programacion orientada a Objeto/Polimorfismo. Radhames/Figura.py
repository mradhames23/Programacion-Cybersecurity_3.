import math

# Clase base
class Figura:
    def area(self):
        return 0  # Área genérica (se sobrescribe en las hijas)


# Clase hija: Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Clase hija: Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


# Ejemplo de uso
figuras = [
    Circulo(8),
    Cuadrado(9)
]

for f in figuras:
    print("Área:", f.area())

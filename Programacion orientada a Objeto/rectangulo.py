class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
rect1 = Rectangulo(9, 38)
print("El área del rectángulo es:", rect1.calcular_area())

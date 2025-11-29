class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    
    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento
        print("La nueva velocidad es:", self.velocidad)

# Ejemplo de uso
coche1 = Coche("Ferrari",280)
coche1.aumentar_velocidad(20)

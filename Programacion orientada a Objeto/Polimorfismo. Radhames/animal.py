# Clase base
class Animal:
    def hablar(self):
        return "El animal hace un sonido."

# Clase hija Perro
class Perro(Animal):
    def hablar(self):
        return "El perro dice: ¡Guau!"

# Clase hija Gato
class Gato(Animal):
    def hablar(self):
        return "El gato dice: ¡Miau!"

# Ejemplo de uso (polimorfismo)
animales = [Perro(), Gato(), Animal()]

for a in animales:
    print(a.hablar())

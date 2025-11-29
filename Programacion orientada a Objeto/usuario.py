class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

# Ejemplo de uso
usuario1 = Usuario("Radhames", 26)
usuario1.mostrar_datos()

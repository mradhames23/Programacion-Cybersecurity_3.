class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones  # Lista de números
    
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

# Ejemplo de uso
est1 = Estudiante("Radhames", [70, 87, 70, 80])
print("El promedio de", est1.nombre, "es:", est1.calcular_promedio())

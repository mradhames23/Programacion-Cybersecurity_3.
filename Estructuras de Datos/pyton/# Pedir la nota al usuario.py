# Pedir la nota al usuario
nota = float(input("Introduce tu nota (0-100): "))

# Evaluar la nota
if nota >= 90:
    print("Aprobado con A")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

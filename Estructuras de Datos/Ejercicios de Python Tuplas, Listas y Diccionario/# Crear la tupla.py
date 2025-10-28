# Crear la tupla
vulnerabilidades = (
    'SQL Injection',
    'Cross-Site Scripting',
    'Buffer Overflow',
    'Denegación de Servicio'
)

# a) Mostrar el segundo elemento (índice 1)
print("a) Segundo elemento:")
print(vulnerabilidades[1])   # Cross-Site Scripting

# b) Mostrar los dos últimos elementos
print("\nb) Los dos últimos elementos:")
print(vulnerabilidades[-2:])  # ('Buffer Overflow', 'Denegación de Servicio')

# c) Intentar modificar un elemento y observar el resultado
print("\nc) Intento de modificar un elemento:")
try:
    vulnerabilidades[1] = 'XSS'   # intento de asignación
except TypeError as e:
    print("Se produjo un error:", e)

a) Segundo elemento:
Cross-Site Scripting

b) Los dos últimos elementos:
('Buffer Overflow', 'Denegación de Servicio')

c) Intento de modificar un elemento:
Se produjo un error: 'tuple' object does not support item assignment


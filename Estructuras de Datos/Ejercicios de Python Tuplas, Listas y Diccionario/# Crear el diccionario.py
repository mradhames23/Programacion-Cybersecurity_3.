# Crear el diccionario
dispositivo_red = {
    'IP': '192.168.1.10',
    'Hostname': 'Firewall-Corp',
    'Estado': 'Activo'
}

# a) Mostrar el valor de la clave 'Hostname'
print("Hostname:", dispositivo_red['Hostname'])

# b) Agregar una nueva clave 'Ubicación'
dispositivo_red['Ubicación'] = 'Centro de Datos'

# c) Cambiar el valor de 'Estado' a 'Inactivo'
dispositivo_red['Estado'] = 'Inactivo'

# d) Mostrar todo el diccionario actualizado
print("Diccionario actualizado:")
print(dispositivo_red)
Hostname: Firewall-Corp
Diccionario_actualizado:
{'IP': '192.168.1.10', 'Hostname': 'Firewall-Corp', 'Estado': 'Inactivo', 'Ubicación': 'Centro de Datos'}


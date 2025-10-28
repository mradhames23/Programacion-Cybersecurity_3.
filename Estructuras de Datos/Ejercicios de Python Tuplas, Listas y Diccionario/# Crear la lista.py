# Crear la lista
puertos_abiertos = [22, 80, 443, 8080]

# a) Agregar el puerto 21 a la lista
puertos_abiertos.append(21)

# b) Eliminar el puerto 8080
puertos_abiertos.remove(8080)

# c) Mostrar la lista ordenada de menor a mayor
puertos_abiertos.sort()

# Mostrar el resultado final
print("Lista de puertos abiertos ordenada:", puertos_abiertos)

Lista de puertos abiertos ordenada: [21, 22, 80, 443]


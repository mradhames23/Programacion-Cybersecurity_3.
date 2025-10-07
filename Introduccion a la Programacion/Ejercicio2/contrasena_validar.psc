Algoritmo contrasena_validar
	Definir contrasena Como Cadena
	Repetir
		Escribir 'Ingresa la contraseña:'
		Leer contrasena
		Si contrasena<>'1234' Entonces
			Escribir 'Contraseña incorrecta. Intenta nuevamente.'
		FinSi
	Hasta Que contrasena='1234'
	Escribir '¡Contraseña correcta!'
FinAlgoritmo

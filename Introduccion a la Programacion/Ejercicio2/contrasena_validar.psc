Algoritmo contrasena_validar
	Definir contrasena Como Cadena
	Repetir
		Escribir 'Ingresa la contrase�a:'
		Leer contrasena
		Si contrasena<>'1234' Entonces
			Escribir 'Contrase�a incorrecta. Intenta nuevamente.'
		FinSi
	Hasta Que contrasena='1234'
	Escribir '�Contrase�a correcta!'
FinAlgoritmo

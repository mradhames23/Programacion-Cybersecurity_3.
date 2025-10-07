Algoritmo suma_cero
	Definir numero, suma Como Real
	suma <- 0
	Escribir 'Ingresa un número (ingresa 0 para terminar y ver la suma total):'
	Leer numero
	Mientras numero<>0 Hacer
		suma <- suma+numero
		Escribir 'Ingresa otro número (0 para finalizar):'
		Leer numero
	FinMientras
	Escribir '---------------------------------------'
	Escribir 'La suma total de todos los números ingresados es: ', suma
FinAlgoritmo

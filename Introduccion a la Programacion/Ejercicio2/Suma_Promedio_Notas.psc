Algoritmo Suma_Promedio_Notas
	Definir nota, suma, promedio Como Real
	Definir i Como Entero
	suma <- 0
	Para i<-1 Hasta 5 Hacer
		Escribir 'Ingresa la nota ', i, ':'
		Leer nota
		suma <- suma+nota
	FinPara
	promedio <- suma/5
	Escribir 'La suma de las notas es: ', suma
	Escribir 'El promedio final es: ', promedio
FinAlgoritmo

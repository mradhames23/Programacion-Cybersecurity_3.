Algoritmo Calcular_Factorial
	Definir numero, i, factorial Como Entero
	Escribir 'Ingresa un n�mero entero para calcular su factorial:'
	Leer numero
	factorial <- 1
	Para i<-1 Hasta numero Hacer
		factorial <- factorial*i
	FinPara
	Escribir 'El factorial de ', numero, ' es: ', factorial
FinAlgoritmo

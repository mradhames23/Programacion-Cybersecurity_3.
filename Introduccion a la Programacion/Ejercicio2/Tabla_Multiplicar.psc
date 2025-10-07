Algoritmo Tabla_Multiplicar
	Definir numero, i, resultado Como Entero
	Escribir 'Ingresa un número para mostrar su tabla de multiplicar:'
	Leer numero
	i <- 1
	Repetir
		resultado <- numero*i
		Escribir numero, ' x ', i, ' = ', resultado
		i <- i+1
	Hasta Que i>10
FinAlgoritmo

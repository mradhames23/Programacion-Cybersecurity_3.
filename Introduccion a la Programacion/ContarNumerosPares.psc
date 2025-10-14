Algoritmo ContarNumerosPares
	Definir vector Como Entero
	Dimensionar vector(10)
	Definir i Como Entero
	Definir contador_pares Como Entero
	contador_pares <- 0
	Escribir '--- Conteo de Números Pares en un Vector (10 posiciones) ---'
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir 'Ingrese el número para la posición ', i, ':'
		Leer vector[i]
	FinPara
	Escribir '------------------------------------------------------------'
	Escribir 'Iniciando conteo de números pares...'
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Si (vector[i] MOD 2)=0 Entonces
			contador_pares <- contador_pares+1
		FinSi
	FinPara
	Escribir '------------------------------------------------------------'
	Escribir 'Análisis completado.'
	Escribir 'De los 10 números ingresados, hay un total de ', contador_pares, ' números pares. ?'
	Escribir '------------------------------------------------------------'
FinAlgoritmo

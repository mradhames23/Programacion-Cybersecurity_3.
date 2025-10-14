Algoritmo SumarElementosVector
	Definir numeros Como Entero
	Dimensionar numeros(10)
	Definir i Como Entero
	Definir suma_total Como Entero
	suma_total <- 0
	Escribir '--- Suma de Elementos de un Vector (10 posiciones) ---'
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir 'Ingrese el número para la posición ', i, ':'
		Leer numeros[i]
		suma_total <- suma_total+numeros[i]
	FinPara
	Escribir '--------------------------------------------'
	Escribir 'Los 10 números han sido almacenados y sumados.'
	Escribir 'La suma total de todos los elementos del vector es: ', suma_total, ' ??'
	Escribir '--------------------------------------------'
FinAlgoritmo

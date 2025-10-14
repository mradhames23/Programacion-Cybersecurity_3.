Algoritmo AlmacenarYMostrarVector
	Definir numeros Como Entero
	Dimensionar numeros(5)
	Definir i Como Entero
	Escribir '--- Almacenamiento y Lectura de Vector ---'
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir 'Ingrese el número para la posición ', i, ':'
		Leer numeros[i]
	FinPara
	Escribir '--------------------------------------------'
	Escribir 'Valores almacenados en el vector:'
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir 'Posición ', i, ': ', numeros[i]
	FinPara
	Escribir '--------------------------------------------'
FinAlgoritmo

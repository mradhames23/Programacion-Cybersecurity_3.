Algoritmo BuscarNumeroEnVector
	Definir vector Como Entero
	Dimensionar vector(8)
	Definir i, num_buscar Como Entero
	Definir encontrado Como Lógico
	encontrado <- Falso
	i <- 1
	Escribir '--- Búsqueda de Número en el Vector (8 posiciones) ---'
	Escribir 'Por favor, ingrese 8 números enteros:'
	Para i<-1 Hasta 8 Con Paso 1 Hacer
		Escribir 'Elemento ', i, ':'
		Leer vector[i]
	FinPara
	Escribir '--------------------------------------------------------'
	Escribir 'Ingrese el número que desea buscar en el vector:'
	Leer num_buscar
	i <- 1
	Mientras (i<=8) Y (encontrado=Falso) Hacer
		Si vector[i]=num_buscar Entonces
			encontrado <- Verdadero
		FinSi
		i <- i+1
	FinMientras
	Escribir '--------------------------------------------------------'
	Si encontrado Entonces
		Escribir '? ¡Número Encontrado! El ', num_buscar, ' se encuentra en la posición ', i-1, '.'
	SiNo
		Escribir '? Número No Encontrado. El ', num_buscar, ' no está en el vector.'
	FinSi
	Escribir '--------------------------------------------------------'
FinAlgoritmo

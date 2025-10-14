Algoritmo PromedioDeCalificaciones
	Definir calificaciones Como Real
	Dimensionar calificaciones(5)
	Definir i Como Entero
	Definir suma_total Como Real
	Definir promedio_general Como Real
	Definir NUM_ESTUDIANTES Como Entero
	NUM_ESTUDIANTES <- 5
	suma_total <- 0
	Escribir '--- Cálculo del Promedio General de Calificaciones (5 Estudiantes) ---'
	Para i<-1 Hasta NUM_ESTUDIANTES Con Paso 1 Hacer
		Escribir 'Ingrese la calificación del estudiante ', i, ':'
		Leer calificaciones[i]
		suma_total <- suma_total+calificaciones[i]
	FinPara
	promedio_general <- suma_total/NUM_ESTUDIANTES
	Escribir '--------------------------------------------------------'
	Escribir 'Suma total de las calificaciones: ', suma_total
	Escribir 'Número de estudiantes: ', NUM_ESTUDIANTES
	Escribir '--------------------------------------------------------'
	Escribir 'El promedio general del grupo es: ', promedio_general, ' ?'
	Escribir '--------------------------------------------------------'
FinAlgoritmo

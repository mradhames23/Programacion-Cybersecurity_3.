Función resultado <- Promedio(nota1,nota2,nota3)
	resultado <- (nota1+nota2+nota3)/3
FinFunción

Algoritmo CalificarEstudiante
	Definir n1, n2, n3 Como Real
	Definir prom Como Real
	Escribir '--- Cálculo de Promedio de Notas ---'
	Escribir 'Ingrese la primera nota:'
	Leer n1
	Escribir 'Ingrese la segunda nota:'
	Leer n2
	Escribir 'Ingrese la tercera nota:'
	Leer n3
	prom <- Promedio(n1,n2,n3)
	Escribir '------------------------------------'
	Escribir 'El promedio de las tres notas es: ', prom
	Si prom>=70 Entonces
		Escribir '¡Felicitaciones! El estudiante ha APROBADO. ?'
	SiNo
		Escribir 'Lo sentimos. El estudiante ha REPROBADO. ?'
	FinSi
	Escribir '------------------------------------'
FinAlgoritmo

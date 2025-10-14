Función el_mayor <- MayorNumero(num1,num2,num3)
	Definir el_mayor Como Real
	Si num1>=num2 Y num1>=num3 Entonces
		el_mayor <- num1
	SiNo
		Si num2>=num1 Y num2>=num3 Entonces
			el_mayor <- num2
		SiNo
			el_mayor <- num3
		FinSi
	FinSi
FinFunción

Algoritmo EncontrarElMayor
	Definir a, b, c Como Real
	Definir maximo Como Real
	Escribir '--- Encontrar el Número Mayor ---'
	Escribir 'Ingrese el primer número:'
	Leer a
	Escribir 'Ingrese el segundo número:'
	Leer b
	Escribir 'Ingrese el tercer número:'
	Leer c
	maximo <- MayorNumero(a,b,c)
	Escribir '--------------------------------'
	Escribir 'Los números ingresados fueron: ', a, ', ', b, ' y ', c
	Escribir 'El número mayor es: ', maximo, ' ??'
	Escribir '--------------------------------'
FinAlgoritmo

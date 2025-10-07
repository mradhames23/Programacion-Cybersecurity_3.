Algoritmo PagasMas_PagasMenos
	Definir montoCompra, montoPagar, descuento Como Real
	Escribir 'Por favor, ingresa el monto total de la compra:'
	Leer montoCompra
	Si montoCompra>500 Entonces
		descuento <- montoCompra*0.10
		montoPagar <- montoCompra-descuento
		Escribir '¡Felicidades! Se aplicó un 10% de descuento.'
		Escribir 'Total Original: ', montoCompra
		Escribir 'Descuento aplicado: ', descuento
		Escribir 'El total final a pagar es: ', montoPagar
	SiNo
		montoPagar <- montoCompra
		Escribir 'El monto no supera los $500, no se aplica descuento.'
		Escribir 'El monto final a pagar es: ', montoPagar
	FinSi
FinAlgoritmo

Función resultado_validacion <- ValidarPassword(clave)
	Si Longitud(clave)>8 Entonces
		resultado_validacion <- Verdadero
	SiNo
		resultado_validacion <- Falso
	FinSi
FinFunción

Algoritmo ComprobarContrasena
	Definir password Como Cadena
	Definir es_valida Como Lógico
	Escribir '--- Validación de Contraseña ---'
	Escribir 'Ingrese su contraseña (debe tener más de 8 caracteres):'
	Leer password
	es_valida <- ValidarPassword(password)
	Si es_valida Entonces
		Escribir '? ¡Contraseña Válida! Tiene más de 8 caracteres.'
	SiNo
		Escribir '? Contraseña Inválida. Debe tener más de 8 caracteres.'
		Escribir 'Longitud actual: ', Longitud(password), ' caracteres.'
	FinSi
	Escribir '--------------------------------'
FinAlgoritmo

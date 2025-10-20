Algoritmo SistemaDeMonitoreoDeAccesos
	Definir usuarios, servidores Como Cadena
	Definir intentos, ip, tipo, hora Como Cadena
	Definir n, opcion Como Entero
	Dimensionar usuarios(10)
	Dimensionar servidores(10)
	Dimensionar intentos(10,10)
	Dimensionar ip(10,10)
	Dimensionar tipo(10,10)
	Dimensionar hora(10,10)
	n <- 0
	Repetir
		Limpiar Pantalla
		Escribir '===== SISTEMA DE MONITOREO DE ACCESOS ====='
		Escribir '1. Registrar intento de acceso'
		Escribir '2. Mostrar reporte general'
		Escribir '3. Generar alertas'
		Escribir '4. Salir'
		Escribir 'Seleccione una opción: 'Sin Saltar
		Leer opcion
		Según opcion Hacer
			1:
				RegistrarIntentos(usuarios,servidores,intentos,ip,tipo,hora,n)
			2:
				MostrarReporte(usuarios,servidores,intentos,ip,tipo,hora,n)
				Esperar Tecla
			3:
				GenerarAlertas(usuarios,servidores,tipo,n)
				Esperar Tecla
			4:
				Escribir 'Saliendo del sistema...'
			De Otro Modo:
				Escribir 'Opción no válida.'
		FinSegún
	Hasta Que opcion=4
FinAlgoritmo

Función RegistrarIntentos (usuarios,servidores,intentos,ip,tipos,hora,n)
	Definir usuario, servidor, ipTemp, tipoTemp, horaTemp Como Cadena
	Definir i Como Entero
	Escribir 'Ingrese nombre de usuario: 'Sin Saltar
	Leer usuario
	Escribir 'Ingrese nombre del servidor: 'Sin Saltar
	Leer servidor
	Escribir 'Ingrese dirección IP: 'Sin Saltar
	Leer ipTemp
	Escribir 'Ingrese tipo de intento (Correcto/Fallido): 'Sin Saltar
	Leer tipoTemp
	Escribir 'Ingrese hora del intento (HH:MM): 'Sin Saltar
	Leer horaTemp
	n <- n+1
	usuarios[n] <- usuario
	servidores[n] <- servidor
	intentos[n,1]<-'Intento '+ConvertirATexto(n)
	ip[n,1]<-ipTemp
	hora[n,1]<-horaTemp
	Escribir '? Intento registrado exitosamente.'
	Esperar Tecla
FinFunción

Función MostrarReporte(usuarios,servidores,intentos,ip,tipo,hora,n)
	Definir i Como Entero
	Si n=0 Entonces
		Escribir 'No hay intentos registrados.'
	FinSi
	Escribir ''
	Escribir '===== REPORTE DE INTENTOS DE ACCESO ====='
	Para i<-1 Hasta n Con Paso 1 Hacer
		Escribir 'Intento #', i
		Escribir ' Usuario: ', usuarios[i]
		Escribir ' Servidor: ', servidores[i]
		Escribir ' IP: ', ip[i,1]
		Escribir ' Tipo: ', tipo[i,1]
		Escribir ' Hora: ', hora[i,1]
		Escribir '----------------------------------------'
	FinPara
FinFunción

Función GenerarAlertas(usuarios,servidores,tipo,n)
	Definir i, conteoFallidos Como Entero
	Definir alerta Como Lógico
	alerta <- Falso
	conteoFallidos <- 0
	Si n=0 Entonces
		Escribir 'No hay datos registrados.'
	FinSi
	Escribir ''
	Escribir '===== ALERTAS DE SEGURIDAD ====='
	Para i<-1 Hasta n Con Paso 1 Hacer
		Si tipo[i,1]='Fallido' Entonces
			conteoFallidos <- conteoFallidos+1
			Escribir '??  Intento fallido detectado:'
			Escribir '  Usuario: ', usuarios[i]
			Escribir '  Servidor: ', servidores[i]
			alerta <- Verdadero
		FinSi
	FinPara
	Si alerta=Verdadero Entonces
		Escribir ''
		Si conteoFallidos>=3 Entonces
			Escribir '?? Alerta crítica: múltiples intentos fallidos detectados (', conteoFallidos, ').'
		SiNo
			Escribir '?? Se detectaron ', conteoFallidos, ' intentos fallidos.'
		FinSi
	SiNo
		Escribir '? No se detectaron amenazas.'
	FinSi
FinFunción

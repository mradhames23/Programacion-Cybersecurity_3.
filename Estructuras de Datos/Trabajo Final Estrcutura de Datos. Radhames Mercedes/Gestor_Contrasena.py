import re
import getpass
import string
import random
import os

# Archivo donde se almacenarán los datos
ARCHIVO = "usuarios.txt"

# Listas para almacenar usuarios y contraseñas
usuarios = []
contrasenas = []

# -----------------------------------------------------
# Función: CargarDatos
# Carga los usuarios y contraseñas desde el archivo
# -----------------------------------------------------
def CargarDatos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 2:
                    usuarios.append(datos[0])
                    contrasenas.append(datos[1])
        print(f"📂 Datos cargados correctamente desde {ARCHIVO}.")
    else:
        print("ℹ️ No hay datos guardados aún. Se creará un archivo nuevo al registrar usuarios.")

# -----------------------------------------------------
# Función: GuardarDatos
# Guarda los usuarios y contraseñas en el archivo
# -----------------------------------------------------
def GuardarDatos():
    with open(ARCHIVO, "w") as f:
        for i in range(len(usuarios)):
            f.write(f"{usuarios[i]},{contrasenas[i]}\n")
    print("💾 Datos guardados correctamente.")

# -----------------------------------------------------
# Función: VerificarContraseña
# Analiza la fuerza de una contraseña
# -----------------------------------------------------
def VerificarContraseña(contra):
    largo = len(contra) >= 8
    mayus = re.search(r"[A-Z]", contra)
    minus = re.search(r"[a-z]", contra)
    num = re.search(r"[0-9]", contra)
    simbolo = re.search(r"[!@#$%^&*(),.?\":{}|<>]", contra)

    return largo and mayus and minus and num and simbolo

# -----------------------------------------------------
# Función: RegistrarUsuario
# Registra un nuevo usuario si no existe y la contraseña es fuerte
# -----------------------------------------------------
def RegistrarUsuario():
    usuario = input("Ingrese un nombre de usuario: ")

    if usuario in usuarios:
        print("⚠️ Ese usuario ya existe. Intente con otro.")
        return

    contra = getpass.getpass("Ingrese una contraseña: ")

    if VerificarContraseña(contra):
        usuarios.append(usuario)
        contrasenas.append(contra)
        GuardarDatos()
        print("✅ Usuario registrado correctamente con una contraseña segura.")
    else:
        print("❌ Contraseña débil. Debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo.")

# -----------------------------------------------------
# Función: GenerarAlertas
# Muestra los usuarios con contraseñas débiles
# -----------------------------------------------------
def GenerarAlertas():
    print("\n🔎 Verificando contraseñas...")
    alertas = 0
    for i in range(len(contrasenas)):
        if not VerificarContraseña(contrasenas[i]):
            print(f"⚠️ Contraseña débil detectada en el usuario: {usuarios[i]}")
            alertas += 1
    if alertas == 0:
        print("✅ Todas las contraseñas son seguras.")

# -----------------------------------------------------
# Función: GenerarContrasenaSegura
# Genera una contraseña aleatoria y fuerte
# -----------------------------------------------------
def GenerarContrasenaSegura():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    segura = ''.join(random.choice(caracteres) for _ in range(12))
    print(f"🔐 Contraseña segura sugerida: {segura}")

# -----------------------------------------------------
# Menú principal
# -----------------------------------------------------
def Menu():
    CargarDatos()  # Cargar datos al inicio

    while True:
        print("\n--- GESTOR DE CONTRASEÑAS SEGURAS ---")
        print("1. Registrar usuario")
        print("2. Verificar contraseñas")
        print("3. Generar contraseña segura")
        print("4. Mostrar todos los usuarios registrados")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            RegistrarUsuario()
        elif opcion == "2":
            GenerarAlertas()
        elif opcion == "3":
            GenerarContrasenaSegura()
        elif opcion == "4":
            if usuarios:
                print("\n👥 Usuarios registrados:")
                for u in usuarios:
                    print(f"- {u}")
            else:
                print("No hay usuarios registrados aún.")
        elif opcion == "5":
            print("👋 Saliendo del gestor. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# -----------------------------------------------------
# Ejecutar el programa
# -----------------------------------------------------
Menu()

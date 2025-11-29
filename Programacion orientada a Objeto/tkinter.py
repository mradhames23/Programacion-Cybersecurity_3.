import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Bienvenida")
ventana.geometry("300x150")

# Crear Label (mensaje)
mensaje = tk.Label(ventana, text="¡Bienvenido a la aplicación!", font=("Arial", 14))
mensaje.pack(pady=20)

# Ejecutar ventana
ventana.mainloop()
# Clase Estudiante
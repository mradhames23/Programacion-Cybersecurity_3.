import tkinter as tk

# 1. Crear ventana
ventana = tk.Tk()
ventana.title("Ejemplo básico")

# 2. Crear widget (etiqueta)
etiqueta = tk.Label(ventana, text="¡Hola, colega!")

# 3. Mostrar widget
etiqueta.pack(pady=20, padx=20) # Añade un poco de espacio

# 4. Iniciar el bucle de eventos
ventana.mainloop()


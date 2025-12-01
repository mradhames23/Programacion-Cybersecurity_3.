import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text="Texto ingresado: " + texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Mostrar Texto")
ventana.geometry("400x300")

# Entry
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Botón
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack(pady=5)

# Label donde se mostrará el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 16))
etiqueta_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

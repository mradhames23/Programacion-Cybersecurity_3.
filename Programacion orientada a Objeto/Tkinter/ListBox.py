import tkinter as tk

def agregar_elemento():
    nuevo = entry_elemento.get()
    if nuevo.strip() != "":
        lista.insert(tk.END, nuevo)
        entry_elemento.delete(0, tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Lista de elementos")
ventana.geometry("400x300")

# Listbox
lista = tk.Listbox(ventana, width=30, height=10)
lista.pack(pady=10)

# Entry para escribir el nuevo elemento
entry_elemento = tk.Entry(ventana, width=25)
entry_elemento.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar elemento", command=agregar_elemento)
boton_agregar.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

import tkinter as tk

def sumar():
    try:
        n1 = float(entry_num1.get())
        n2 = float(entry_num2.get())
        resultado = n1 + n2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Error: Ingresa números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Sencilla")
ventana.geometry("400x275")

# Label y Entry para el primer número
label1 = tk.Label(ventana, text="Número 1:")
label1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)

# Label y Entry para el segundo número
label2 = tk.Label(ventana, text="Número 2:")
label2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)

# Botón para sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=10)

# Label para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 16))
label_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

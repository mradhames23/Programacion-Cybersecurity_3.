import tkinter as tk

def iniciar_dibujo(event):
    global x_anterior, y_anterior
    x_anterior = event.x
    y_anterior = event.y

def dibujar(event):
    global x_anterior, y_anterior
    canvas.create_line(x_anterior, y_anterior, event.x, event.y, fill="black", width=2)
    x_anterior = event.x
    y_anterior = event.y

# Crear ventana
ventana = tk.Tk()
ventana.title("Dibujar en Canvas")
ventana.geometry("500x400")

# Crear Canvas
canvas = tk.Canvas(ventana, bg="white", width=480, height=350)
canvas.pack(pady=10)

# Eventos del mouse
canvas.bind("<Button-1>", iniciar_dibujo)       # Cuando se presiona el botón del mouse
canvas.bind("<B1-Motion>", dibujar)             # Mientras se mantiene presionado y se mueve

ventana.mainloop()

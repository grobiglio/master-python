from tkinter import *

# Crear la ventana raíz
ventana = Tk()

# Título de la ventana
ventana.title("Interfaz gráfica con Python")

# Icono de la ventana
ventana.iconbitmap("./21-Tkinter/imagenes/descarga.ico")

# Cambio el tamaño de la ventana
ventana.geometry ("750x450")

# Bloquear el tamaño de la ventana
ventana.resizable(0,0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
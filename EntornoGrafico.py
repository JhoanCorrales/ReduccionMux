import tkinter as tk
from tkinter import messagebox
import Main

def calcular():
    entrada_texto = entrada.get()
    resultado = Main.calcular_min_terminos(entrada_texto)  # Llama a la función en Main.py
    
    if "Error" in resultado:
        messagebox.showerror("Error", resultado)  # Muestra un mensaje de error si ocurre algún problema
    else:
        resultado_label.config(text=resultado)  # Actualiza la etiqueta con el resultado completo

# Crear la ventana principal de Tkinter
ventana_principal = tk.Tk()
ventana_principal.geometry("1330x730")
ventana_principal.title("Reduccion de multiplexor(MUX)")

# Campo de entrada
entrada_label = tk.Label(ventana_principal, text="Ingrese los índices de los min términos:")
entrada_label.place(x=20, y=20)

entrada = tk.Entry(ventana_principal)
entrada.place(x=250, y=20, width=200)  # Campo de entrada con un ancho de 200 píxeles

# Botón para calcular
boton = tk.Button(ventana_principal, text="Calcular", command=calcular)
boton.place(x=480, y=17)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana_principal, text="", justify="left")
resultado_label.place(x=20, y=100)


ventana_principal.mainloop()
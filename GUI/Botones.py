import tkinter as tk
import sys
import os
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main

def calcular(entrada, resultado_label):
    entrada_texto = entrada.get()
    resultado = Main.calcular_min_terminos(entrada_texto)
    
    if "Error" in resultado:
        messagebox.showerror("Error", resultado)
    else:
        resultado_label.config(text=resultado)

def configurar_botones(ventana, entrada):
    # Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana, text="", justify="left")
    resultado_label.place(x=20, y=100)
    
    # Botón para calcular
    boton = tk.Button(ventana, text="Calcular", command=lambda: calcular(entrada, resultado_label))
    boton.place(x=480, y=17)

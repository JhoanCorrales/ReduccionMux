import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main

def calcular(entrada_min_terminos, label_resultado, campo_entrada, boton_calcular, label_entrada_texto):
    texto_entrada = entrada_min_terminos.get()
    resultado = Main.calcular_min_terminos(texto_entrada)
    
    # Eliminar los widgets de entrada, el botón y la etiqueta de entrada
    campo_entrada.destroy()
    boton_calcular.destroy()
    label_entrada_texto.destroy()
    label_resultado.place(relx=0.5, y=150, anchor='center')

    if "Error" in resultado:
        messagebox.showerror("Error", resultado)
    else:
        label_resultado.config(text=f"Resultado: {resultado}")


def configurar_botones(ventana, entrada_min_terminos, label_entrada_texto):
    label_resultado = tk.Label(ventana, text=":D", font=("Arial", 12), bg="white")
    label_resultado.place(relx=0.5, y=300, anchor='center')
    
    boton_calcular = tk.Button(ventana, text="Calcular", command=lambda: calcular(entrada_min_terminos, label_resultado, entrada_min_terminos, boton_calcular, label_entrada_texto))
    boton_calcular.place(relx=0.5, y=240, anchor='center')
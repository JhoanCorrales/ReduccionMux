import tkinter as tk
from tkinter import messagebox
from Layout import dibujar_multiplexor 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main

def reiniciar(ventana, label_resultado, boton_reiniciar, canvas_frame):
    label_resultado.destroy()
    canvas_frame.destroy()
    label_entrada_texto = tk.Label(ventana, text="Por favor ingrese los índices de los min términos:", font=("Arial", 20), bg="black", fg="white")
    label_entrada_texto.config(bg="black", fg="white")
    label_entrada_texto.place(relx=0.5, y=150, anchor='center')

    entrada_min_terminos = tk.Entry(ventana)
    entrada_min_terminos.config(bg="black", fg="white")
    entrada_min_terminos.place(relx=0.5, y=190, anchor='center', width=300)

    configurar_botones(ventana, entrada_min_terminos, label_entrada_texto)
    boton_reiniciar.destroy()


def calcular(entrada_min_terminos, label_resultado, campo_entrada, boton_calcular, label_entrada_texto, ventana):
    texto_entrada = entrada_min_terminos.get()
    resultado, terminos, num_control = Main.calcular_min_terminos(texto_entrada)

    if "Error" in resultado:
        messagebox.showerror("Error", resultado)
    else:
        # Eliminar widgets anteriores
        campo_entrada.destroy()
        boton_calcular.destroy()
        label_entrada_texto.destroy()

        # Mostrar el resultado en la etiqueta
        label_resultado.place(relx=0.1, rely=0.26, anchor='nw')
        label_resultado.config(text=f"{resultado}", bg="black", fg="white")

        # Crear el frame que contendrá el canvas y las barras de desplazamiento
        canvas_frame = tk.Frame(ventana, bg="black")
        canvas_frame.place(relx=0.80, rely=0.1, anchor='ne', width=400, height=400)  # Ajustar tamaño según sea necesario

        # Crear el canvas con el multiplexor
        canvas = tk.Canvas(canvas_frame, width=400, height=400, bg='black')

        # Añadir las barras de desplazamiento al canvas
        scrollbar_y = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)

        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        canvas.pack(side="left", expand=True, fill="both")

        # Determinar el tamaño del canvas según la cantidad de entradas
        num_entradas = len(terminos)
        canvas_altura = 400 + (num_entradas - 10) * 20 if num_entradas > 10 else 400
        canvas.config(scrollregion=(0, 0, 400, canvas_altura))  # Tamaño dinámico del área de scroll

        # Llamar a la función para dibujar el multiplexor con los términos como nombres de las entradas
        dibujar_multiplexor(canvas, num_entradas, terminos, num_control)

        boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=lambda: reiniciar(ventana, label_resultado, boton_reiniciar, canvas_frame))
        boton_reiniciar.place(relx=0.165, rely=0.42, anchor='nw')


def configurar_botones(ventana, entrada_min_terminos, label_entrada_texto):
    label_resultado = tk.Label(ventana, bg="white")

    boton_calcular = tk.Button(ventana, text="Calcular", command=lambda: calcular(entrada_min_terminos, label_resultado, entrada_min_terminos, boton_calcular, label_entrada_texto, ventana))
    boton_calcular.place(relx=0.5, y=240, anchor='center')
import tkinter as tk
from tkinter import messagebox
from Layout import dibujar_multiplexor 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main

def reiniciar(ventana, label_resultado, boton_reiniciar, canvas_frame_multiplexor, canvas_frame_resultado):
    label_resultado.destroy()
    canvas_frame_multiplexor.destroy()
    canvas_frame_resultado.destroy()
    
    label_entrada_texto = tk.Label(ventana, text="Por favor ingrese los índices de los min términos:", font=("Arial", 20), bg="black", fg="white")
    label_entrada_texto.config(bg="black", fg="white")
    label_entrada_texto.place(relx=0.5, y=150, anchor='center')

    entrada_min_terminos = tk.Entry(ventana)
    entrada_min_terminos.config(bg="black", fg="white")
    entrada_min_terminos.place(relx=0.5, y=190, anchor='center', width=300)

    configurar_botones(ventana, entrada_min_terminos, label_entrada_texto)
    boton_reiniciar.destroy()


def validar_min_terminos(min_terminos):
    for term in min_terminos.split(","):
        if not term.strip().isdigit():  # Verificar que sea un número
            return False
        if int(term.strip()) < 0:  # Asegúrate de que no sea negativo
            return False
    return True

def calcular(entrada_min_terminos, label_resultado, campo_entrada, boton_calcular, label_entrada_texto, ventana):
    texto_entrada = entrada_min_terminos.get()

    if not validar_min_terminos(texto_entrada):
        messagebox.showerror("Error", "Los min terminos deben ser numeros no negativos separados por comas.")
        return

    try:
        resultado, terminos, num_control = Main.calcular_min_terminos(texto_entrada)
    except ValueError as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error inesperado: {str(e)}")
        return

    if "Error" in resultado:
        messagebox.showerror("Error", resultado)
    else:
        campo_entrada.destroy()
        boton_calcular.destroy()
        label_entrada_texto.destroy()

        # Mostrar el resultado en la etiqueta, creando un frame con canvas y scrollbars
        canvas_frame_resultado = tk.Frame(ventana, bg="black")
        canvas_frame_resultado.place(relx=0.1, rely=0.26, anchor='nw', width=400, height=200)  # Ajustar tamaño según sea necesario

        # Crear canvas con el resultado y agregar barras deslizantes
        canvas_resultado = tk.Canvas(canvas_frame_resultado, width=400, height=200, bg='black')

        scrollbar_y_resultado = tk.Scrollbar(canvas_frame_resultado, orient="vertical", command=canvas_resultado.yview)
        scrollbar_x_resultado = tk.Scrollbar(canvas_frame_resultado, orient="horizontal", command=canvas_resultado.xview)

        canvas_resultado.configure(yscrollcommand=scrollbar_y_resultado.set, xscrollcommand=scrollbar_x_resultado.set)

        scrollbar_y_resultado.pack(side="right", fill="y")
        scrollbar_x_resultado.pack(side="bottom", fill="x")
        canvas_resultado.pack(side="left", expand=True, fill="both")

        # Agregar el texto del resultado al canvas
        canvas_resultado.create_text(10, 10, anchor="nw", text=f"{resultado}", fill="white")
        canvas_resultado.config(scrollregion=canvas_resultado.bbox("all"))  # Ajustar el área de scroll al contenido

        # Crear el frame para el multiplexor con scrollbars
        canvas_frame_multiplexor = tk.Frame(ventana, bg="black")
        canvas_frame_multiplexor.place(relx=0.80, rely=0.1, anchor='ne', width=400, height=400)  # Ajustar tamaño según sea necesario

        # Crear el canvas con el multiplexor
        canvas_multiplexor = tk.Canvas(canvas_frame_multiplexor, width=400, height=400, bg='black')

        # Añadir las barras de desplazamiento al canvas del multiplexor
        scrollbar_y_multiplexor = tk.Scrollbar(canvas_frame_multiplexor, orient="vertical", command=canvas_multiplexor.yview)
        scrollbar_x_multiplexor = tk.Scrollbar(canvas_frame_multiplexor, orient="horizontal", command=canvas_multiplexor.xview)

        canvas_multiplexor.configure(yscrollcommand=scrollbar_y_multiplexor.set, xscrollcommand=scrollbar_x_multiplexor.set)

        scrollbar_y_multiplexor.pack(side="right", fill="y")
        scrollbar_x_multiplexor.pack(side="bottom", fill="x")
        canvas_multiplexor.pack(side="left", expand=True, fill="both")

        # Determinar el tamaño del canvas según la cantidad de entradas
        num_entradas = len(terminos)
        canvas_altura = 400 + (num_entradas - 10) * 20 if num_entradas > 10 else 400
        canvas_multiplexor.config(scrollregion=(0, 0, 400, canvas_altura))  # Tamaño dinámico del área de scroll

        dibujar_multiplexor(canvas_multiplexor, num_entradas, terminos, num_control)

        boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=lambda: reiniciar(ventana, label_resultado, boton_reiniciar, canvas_frame_multiplexor, canvas_frame_resultado))
        boton_reiniciar.place(relx=0.165, rely=0.42, anchor='nw')


def configurar_botones(ventana, entrada_min_terminos, label_entrada_texto):
    label_resultado = tk.Label(ventana, bg="white")

    boton_calcular = tk.Button(ventana, text="Calcular", command=lambda: calcular(entrada_min_terminos, label_resultado, entrada_min_terminos, boton_calcular, label_entrada_texto, ventana))
    boton_calcular.place(relx=0.5, y=240, anchor='center')
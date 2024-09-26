import tkinter as tk

def dibujar_multiplexor(canvas, num_entradas, terminos_entradas):
    #                  (VSup_I)  (VInf_I) , (VInf_D) (VSupD)
    puntos_trapecio = [100, 100, 100, 300, 250, 240, 250, 160]  # Coordenadas de los vértices
    canvas.create_polygon(puntos_trapecio, outline="black", fill="lightgray", width=2)
    
    # Altura de la primera entrada (ajustada en función de la cantidad de entradas)
    altura_inicial = 110
    separacion_entradas = 20  # Espacio entre cada entrada

    # Dibujar las líneas de entrada según el número de entradas
    for i in range(num_entradas):
        y_pos = altura_inicial + i * separacion_entradas
        canvas.create_line(50, y_pos, 100, y_pos, fill="black", width=2)
        canvas.create_text(40, y_pos, text=terminos_entradas[i], anchor='e')  # Etiquetas de entradas según términos calculados

    # Dibujar la línea de salida
    canvas.create_line(250, 200, 350, 200, fill="black", width=2)  # Salida
    canvas.create_text(360, 200, text="Salida", anchor='w')

    # Dibujar el control de selección
    canvas.create_line(200, 50, 200, 100, fill="black", width=2)
    canvas.create_text(200, 40, text="Control S", anchor='s')
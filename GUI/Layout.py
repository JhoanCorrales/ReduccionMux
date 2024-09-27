def dibujar_multiplexor(canvas, num_entradas, terminos_entradas, num_control):
    # Altura dinámica del multiplexor según el número de entradas
    altura_multiplexor = 200 + (num_entradas - 10) * 20 if num_entradas > 10 else 200

    letras_control = ["B", "C", "D", "E", "F", "G", "H"]
    
    canvas.create_line(200, 30, 200, 200, fill="white", width=2)
    canvas.create_line(200, 30, 300, 30, fill="white", width=2)
    canvas.create_text(210, 10, text="Lineas de control (Sn-2)", anchor='w', fill="white")
    for i in range(num_control):
        y_pos = 30 + i * 30  # Espaciado entre líneas de control
        if i < len(letras_control):
            canvas.create_text(310, y_pos, text=f"{letras_control[i]}", anchor='w', fill="red")  # Etiquetas con letras
        else:
            canvas.create_text(310, y_pos, text=f"S{i}", anchor='w', fill="white")  # Fallback a etiquetas S


    puntos_trapecio = [100, 100, 100, 100 + altura_multiplexor, 250, 100 + altura_multiplexor - 60, 250, 160]
    canvas.create_polygon(puntos_trapecio, outline="white", fill="lightgrey", width=2)


    altura_inicial = 110
    separacion_entradas = 20

    # Dibujar las líneas de entrada
    for i in range(num_entradas):
        y_pos = altura_inicial + i * separacion_entradas
        canvas.create_line(50, y_pos, 100, y_pos, fill="white", width=2)
        canvas.create_text(40, y_pos, text=terminos_entradas[i], anchor='e', fill="white")  # Etiquetas de las entradas

    # Dibujar la línea de salida centrada
    centro_vertical = (100 + (100 + altura_multiplexor)) // 2
    canvas.create_line(250, centro_vertical, 350, centro_vertical, fill="white", width=2)
    canvas.create_text(360, centro_vertical, text="Salida", anchor='w', fill="white")
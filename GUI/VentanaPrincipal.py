import tkinter as tk

from Botones import configurar_botones

# Crear la ventana principal de Tkinter
ventana_principal = tk.Tk()
ventana_principal.geometry("1330x730")
ventana_principal.title("Reducción de multiplexor (MUX)")
ventana_principal.config(bg="black")


# Campo de entrada
entrada_label = tk.Label(ventana_principal, text="Ingrese los índices de los min términos:")
entrada_label.place(x=20, y=20)

entrada = tk.Entry(ventana_principal)
entrada.place(x=250, y=20, width=200)  # Campo de entrada con un ancho de 200 píxeles

# Configurar los botones
configurar_botones(ventana_principal, entrada)

# Ejecutar la ventana
ventana_principal.mainloop()
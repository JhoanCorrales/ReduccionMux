import tkinter as tk
from PIL import Image, ImageTk
from Botones import configurar_botones

# Crear la ventana principal de Tkinter
ventana_principal = tk.Tk()
ventana_principal.geometry("1350x730")
ventana_principal.resizable(0,0)
ventana_principal.title("Reducción de multiplexor (MUX)")
ventana_principal.iconbitmap("C:\\Users\\corra\\OneDrive\\Documentos\\Visual Studio\\Python\\ReduccionMux\\ReduccionMux\\GUI\\Image\\ventana_icono.ico")

imagen = Image.open("C:\\Users\\corra\\OneDrive\\Documentos\\Visual Studio\\Python\\ReduccionMux\\ReduccionMux\\GUI\\Image\\FondoVentana.jpg")
imagen = imagen.resize((1350, 730), Image.LANCZOS)

# Convierte la imagen en formato RGBA para la manipulacion de la transparencia
imagen = imagen.convert("RGBA")
nueva_imagen = Image.new("RGBA", imagen.size, (255, 255, 255, 0))

# Combinar la imagen original con la imagen semi-transparente
imagen_transparente = Image.alpha_composite(imagen, nueva_imagen)
fondo_img = ImageTk.PhotoImage(imagen_transparente)

# Crear un Label para contener la imagen de fondo
fondo_label = tk.Label(ventana_principal, image=fondo_img)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Campo de entrada
entrada_label = tk.Label(ventana_principal, text="Por favor ingrese los indices de los min terminos:", font=("Arial", 20), bg='white')
entrada_label.place(relx=0.5, y=150, anchor='center')

entrada_input = tk.Entry(ventana_principal)
entrada_input.place(relx=0.5, y=190, anchor='center', width=300)

configurar_botones(ventana_principal, entrada_input, entrada_label)

# Asegurar que el fondo se mantiene detrás de los widgets
fondo_label.lower()

# Ejecutar la ventana
ventana_principal.mainloop()
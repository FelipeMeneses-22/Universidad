# Ejercicio 2: Crear una ventana con un campo de texto donde 
# el usuario pueda ingresar su nombre y un botón para mostrar un saludo personalizado.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 15/11/2024
# ----------------------------------------

import tkinter as tk

# Función para mostrar el saludo personalizado

def saludar():
    nombre = entry_nombre.get()  # Obtener el nombre del campo de texto
    label_saludo.config(text="Hola chamo " + nombre )  # Mostrar el saludo

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo Personalizado")

# Etiqueta para el campo de texto
label_instrucciones = tk.Label(ventana, text="Ingresa tu nombre:")
label_instrucciones.pack()

# Campo de texto para ingresar el nombre
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Botón para mostrar el saludo
button_saludar = tk.Button(ventana, text="Saludar", command=saludar)
button_saludar.pack()

# Etiqueta para mostrar el saludo
label_saludo = tk.Label(ventana, text="")
label_saludo.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()
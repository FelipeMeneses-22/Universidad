#Ejercicio 3: crear un sistema que capture tres notas y genere el promedio de las notas , al final 
#Debe entregar un mensaje personalizado con las notas el promedio y el nombre del estudiante 

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 15/11/2024
# ----------------------------------------

import tkinter as tk

# Función para calcular el promedio y mostrar el mensaje
def calcular_promedio():
    try:
        nombre = entry_nombre.get()  # Obtener el nombre del estudiante
        nota1 = float(entry_nota1.get())  # Obtener la primera nota
        nota2 = float(entry_nota2.get())  # Obtener la segunda nota
        nota3 = float(entry_nota3.get())  # Obtener la tercera nota
        
        promedio = (nota1 + nota2 + nota3) / 3  # Calcular el promedio
        
        # Mostrar el mensaje con el nombre, las notas y el promedio
        label_resultado.config(
            text=f"Estudiante: {nombre}\nNotas: {nota1}, {nota2}, {nota3}\nPromedio: {promedio:.2f}"
        )
    except ValueError:
        label_resultado.config(text="Por favor ingresa notas válidas.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Promedio")

# Etiqueta para el nombre
label_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
label_nombre.pack()

# Campo de texto para el nombre
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Etiquetas y campos para las tres notas
label_nota1 = tk.Label(ventana, text="Ingresa la primera nota:")
label_nota1.pack()

entry_nota1 = tk.Entry(ventana)
entry_nota1.pack()

label_nota2 = tk.Label(ventana, text="Ingresa la segunda nota:")
label_nota2.pack()

entry_nota2 = tk.Entry(ventana)
entry_nota2.pack()

label_nota3 = tk.Label(ventana, text="Ingresa la tercera nota:")
label_nota3.pack()

entry_nota3 = tk.Entry(ventana)
entry_nota3.pack()

# Botón para calcular el promedio
button_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
button_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()

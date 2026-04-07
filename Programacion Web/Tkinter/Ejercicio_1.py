# Ejercicio 1:Calculadora simple con dos números y con clases
# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 15/11/2024
# ----------------------------------------


# importamos la libreria de tkinter
import tkinter as tk

import tkinter as tk

# Función para sumar los dos números
def sumar():
    try:
        num1 = float(entry_num1.get())  # Obtener el primer número
        num2 = float(entry_num2.get())  # Obtener el segundo número
        resultado = num1 + num2  # Realizar la suma
        label_resultado.config(text="Resultado: " + str(resultado))  # Mostrar el resultado
    except ValueError:
        label_resultado.config(text="Por favor ingrese números válidos")  # Manejar errores de entrada

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora - Suma")

# Etiquetas y campos de entrada
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack()

# Botón para realizar la suma
button_sumar = tk.Button(ventana, text="Sumar", command=sumar)
button_sumar.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()
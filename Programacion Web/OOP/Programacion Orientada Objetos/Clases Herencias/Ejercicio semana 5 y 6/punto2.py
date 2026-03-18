import tkinter as tk
import threading
import time

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Elevador")

# Variables del elevador
elevador_piso_actual = 1
puertas_abiertas = False
elevador_moviendose = False
modo_emergencia = False
log_text = None

# Función para actualizar el log de eventos
def actualizar_log(mensaje):
    global log_text
    log_text.insert(tk.END, f"{mensaje}\n")
    log_text.see(tk.END)

# Función para mover el elevador a un piso específico
def mover_elevador(piso_destino):
    global elevador_piso_actual, elevador_moviendose, puertas_abiertas, modo_emergencia

    if modo_emergencia:
        actualizar_log("¡Emergencia activada! El elevador no se puede mover.")
        return

    if puertas_abiertas:
        actualizar_log("Las puertas están abiertas. ¡Cierra las puertas antes de mover el elevador!")
        return

    if elevador_moviendose:
        actualizar_log("El elevador ya está en movimiento. Espera a que llegue.")
        return

    elevador_moviendose = True
    actualizar_log(f"Elevador moviéndose del piso {elevador_piso_actual} al piso {piso_destino}...")
    
    while elevador_piso_actual != piso_destino:
        time.sleep(1)
        if elevador_piso_actual < piso_destino:
            elevador_piso_actual += 1
        else:
            elevador_piso_actual -= 1
        
        actualizar_log(f"Elevador en el piso {elevador_piso_actual}...")
    
    actualizar_log(f"El elevador ha llegado al piso {piso_destino}.")
    elevador_moviendose = False

# Función para abrir y cerrar puertas
def abrir_puertas():
    global puertas_abiertas, elevador_moviendose
    if elevador_moviendose:
        actualizar_log("No se pueden abrir las puertas mientras el elevador se mueve.")
        return
    
    if puertas_abiertas:
        actualizar_log("Las puertas ya están abiertas.")
    else:
        puertas_abiertas = True
        actualizar_log("Puertas abiertas.")

def cerrar_puertas():
    global puertas_abiertas
    if puertas_abiertas:
        puertas_abiertas = False
        actualizar_log("Puertas cerradas.")
    else:
        actualizar_log("Las puertas ya están cerradas.")

# Función para manejar la llamada a un piso
def llamada_piso(piso):
    threading.Thread(target=mover_elevador, args=(piso,)).start()

# Función para activar la emergencia
def activar_emergencia():
    global modo_emergencia
    modo_emergencia = True
    actualizar_log("¡Emergencia activada! El elevador no se moverá.")

# Función para desactivar la emergencia
def desactivar_emergencia():
    global modo_emergencia
    modo_emergencia = False
    actualizar_log("Emergencia desactivada. El elevador puede funcionar nuevamente.")

# Crear botones para cada piso (12 pisos)
for i in range(1, 13):  # 12 pisos
    boton_piso = tk.Button(ventana, text=f"Ir al piso {i}", command=lambda i=i: llamada_piso(i))
    boton_piso.pack(pady=5)

# Crear botones para abrir y cerrar las puertas
boton_abrir_puertas = tk.Button(ventana, text="Abrir puertas", command=abrir_puertas)
boton_abrir_puertas.pack(pady=5)

boton_cerrar_puertas = tk.Button(ventana, text="Cerrar puertas", command=cerrar_puertas)
boton_cerrar_puertas.pack(pady=5)

# Crear botones para emergencia
boton_emergencia = tk.Button(ventana, text="Activar emergencia", command=activar_emergencia)
boton_emergencia.pack(pady=5)

boton_desactivar_emergencia = tk.Button(ventana, text="Desactivar emergencia", command=desactivar_emergencia)
boton_desactivar_emergencia.pack(pady=5)

# Cuadro de texto para mostrar el log de eventos
log_text = tk.Text(ventana, height=15, width=50)
log_text.pack(pady=10)

# Iniciar el loop principal de la ventana
ventana.mainloop()






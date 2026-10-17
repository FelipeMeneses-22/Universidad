import pika
import json

# Conectarse al broker RabbitMQ
conexion = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

canal = conexion.channel()

# Crear la cola donde se enviaran los generos
canal.queue_declare(queue="generos")

# Solicitar los datos del genero
id_genero = input("Ingrese el ID del genero: ")
decrip = input("Ingrese la descripcion del genero: ")

# Validar las longitudes
if len(id_genero) > 10:
    print("El ID no puede superar los 10 caracteres")

elif len(decrip) > 250:
    print("La descripcion no puede superar los 250 caracteres")

else:
    # Crear el mensaje
    genero = {
        "id_genero": id_genero,
        "decrip": decrip
    }

    # Convertir el genero a JSON
    mensaje = json.dumps(genero)

    # Enviar el mensaje al broker
    canal.basic_publish(
        exchange="",
        routing_key="generos",
        body=mensaje
    )

    print("Genero enviado al broker:", genero)

# Cerrar la conexion
conexion.close()
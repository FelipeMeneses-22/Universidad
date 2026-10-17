import pika
import json
import sqlite3

# Base de datos local (se crea sola si no existe)
bd = sqlite3.connect("generos.db")
cursor = bd.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS genero (
        id_genero VARCHAR(10) PRIMARY KEY,
        decrip VARCHAR(250) NOT NULL
    )
    """
)
bd.commit()

# Conectarse al broker RabbitMQ
conexion = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
canal = conexion.channel()

# Declarar la misma cola que usa el productor
canal.queue_declare(queue="generos")


def procesar_mensaje(ch, method, properties, body):
    """Se ejecuta cada vez que llega un mensaje a la cola."""
    try:
        genero = json.loads(body)
        id_genero = genero["id_genero"]
        decrip = genero["decrip"]

        print("Genero recibido:", genero)

        # Guardar en la base de datos
        cursor.execute(
            "INSERT INTO genero (id_genero, decrip) VALUES (?, ?)",
            (id_genero, decrip),
        )
        bd.commit()
        print(f"Genero '{id_genero}' guardado en la base de datos")

    except sqlite3.IntegrityError:
        print(f"El genero '{id_genero}' ya existe, se omite")
    except (json.JSONDecodeError, KeyError) as error:
        print("Mensaje invalido:", error)

    # Confirmar a RabbitMQ que el mensaje fue procesado
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Suscribirse a la cola
canal.basic_consume(
    queue="generos",
    on_message_callback=procesar_mensaje,
    auto_ack=False,
)

print("Esperando generos... (CTRL+C para salir)")

try:
    canal.start_consuming()
except KeyboardInterrupt:
    print("\nConsumidor detenido")
finally:
    conexion.close()
    bd.close()

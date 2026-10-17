import pika
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Conectarse a Firestore con la clave descargada de Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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

        # Guardar en Firestore: coleccion "generos", un documento por genero
        db.collection("generos").document(id_genero).set({
            "id_genero": id_genero,
            "decrip": decrip,
        })
        print(f"Genero '{id_genero}' guardado en Firestore")

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

import pika
import json
import random
import time

# Catalogo de generos para generar datos automaticamente
GENEROS = [
    ("ACC", "Accion"),
    ("AVE", "Aventura"),
    ("COM", "Comedia"),
    ("DRA", "Drama"),
    ("TER", "Terror"),
    ("CIF", "Ciencia ficcion"),
    ("ROM", "Romance"),
    ("ANI", "Animacion"),
    ("DOC", "Documental"),
    ("MUS", "Musical"),
    ("SUS", "Suspenso"),
    ("FAN", "Fantasia"),
]

# Segundos de espera entre cada mensaje
INTERVALO = 0.1

# Conectarse al broker RabbitMQ
conexion = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
canal = conexion.channel()

# Misma cola que usa el consumidor
canal.queue_declare(queue="generos")

print("Enviando generos automaticamente... (CTRL+C para detener)")

contador = 1
try:
    while True:
        codigo, nombre = random.choice(GENEROS)

        genero = {
            # El sufijo numerico evita IDs repetidos y se mantiene <= 10 caracteres
            "id_genero": f"{codigo}{contador}",
            "decrip": f"{nombre} (mensaje automatico #{contador})",
        }

        canal.basic_publish(
            exchange="",
            routing_key="generos",
            body=json.dumps(genero),
        )
        print("Genero enviado al broker:", genero)

        contador += 1
        time.sleep(INTERVALO)

except KeyboardInterrupt:
    print("\nProductor detenido")
finally:
    conexion.close()

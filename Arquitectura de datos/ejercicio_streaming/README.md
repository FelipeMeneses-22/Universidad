# Ejercicio de Streaming con RabbitMQ

Ejemplo de procesamiento de datos en tiempo real con el patrón **productor / consumidor**.
Un productor envía géneros (`id_genero` y `decrip`) a una cola de **RabbitMQ**, y un consumidor
los recibe y los guarda en una base de datos (**SQLite** o **Firestore**).

```
productor  ──►  RabbitMQ (cola "generos")  ──►  consumidor  ──►  SQLite / Firestore
```

## Archivos

| Archivo | Descripción |
|---|---|
| `productor.py` | Productor manual: pide el ID y la descripción por teclado y envía un género. |
| `productor_automatico.py` | Productor automático: genera y envía géneros solos cada cierto intervalo. |
| `consumidor.py` | Consumidor que guarda los géneros en SQLite (`generos.db`). |
| `consumidor_firestore.py` | Consumidor que guarda los géneros en Firestore (colección `generos`). |
| `serviceAccountKey.json` | Clave de Firebase (solo para el consumidor de Firestore). **No se sube a GitHub.** |

## Requisitos

- Python 3.10 o superior
- Docker (para levantar RabbitMQ)
- Librerías de Python:

```
pip install pika firebase-admin
```

(`firebase-admin` solo es necesaria para `consumidor_firestore.py`).

## 1. Levantar RabbitMQ

```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

- Puerto `5672`: conexión de los programas Python.
- Puerto `15672`: panel web en http://localhost:15672 (usuario `guest`, contraseña `guest`).

Para comprobar que está corriendo: `docker ps`.
Si el contenedor ya existe y está detenido: `docker start rabbitmq`.

## 2. Ejecutar con SQLite

Abrir **dos terminales** en la carpeta del proyecto.

**Terminal 1: consumidor**

```
python consumidor.py
```

**Terminal 2: productor** (elegir uno)

```
python productor.py              # manual: pide los datos por teclado
python productor_automatico.py   # automático: envía un género cada 2 segundos
```

Los géneros quedan guardados en el archivo `generos.db`, tabla `genero`
(se puede abrir con DB Browser for SQLite).

## 3. Ejecutar con Firestore

### Preparar Firebase (una sola vez)

1. Entrar a https://console.firebase.google.com y abrir el proyecto.
2. En **Firestore Database** pulsar **Crear base de datos** (edición Standard, modo de prueba).
3. Ir a **Configuración del proyecto → Cuentas de servicio → Generar nueva clave privada**.
4. Guardar el archivo descargado en esta carpeta con el nombre `serviceAccountKey.json`.

### Correr

**Terminal 1: consumidor**

```
python consumidor_firestore.py
```

**Terminal 2: productor**

```
python productor_automatico.py
```

Los datos aparecen en vivo en **Firestore Database → Datos**, dentro de la colección `generos`,
con un documento por género (por ejemplo `ACC1`, `COM2`).

## Cómo funciona

1. El productor crea un mensaje JSON, por ejemplo `{"id_genero": "ACC1", "decrip": "Accion"}`,
   y lo publica en la cola `generos`.
2. RabbitMQ guarda el mensaje en la cola hasta que alguien lo consuma.
3. El consumidor recibe el mensaje, lo guarda en la base de datos y le confirma a RabbitMQ
   (`basic_ack`) que fue procesado. Si no confirma, RabbitMQ lo reenvía.

Validaciones del productor manual: `id_genero` hasta 10 caracteres y `decrip` hasta 250.

## Ver los mensajes en RabbitMQ

En http://localhost:15672, pestaña **Queues and Streams**, abrir la cola `generos`:

- **Ready:** mensajes esperando a ser consumidos.
- **Unacked:** mensajes entregados pero sin confirmar.
- **Total:** suma de ambos.

Si el consumidor está corriendo, el contador se queda en 0 porque los mensajes se procesan al instante.
Para verlos acumularse, detener el consumidor, ejecutar el productor unos segundos y revisar la cola.

## Velocidad del productor automático

En `productor_automatico.py` se cambia la variable `INTERVALO` (segundos entre mensajes):

```python
INTERVALO = 2     # un mensaje cada 2 segundos
INTERVALO = 0.1   # 10 mensajes por segundo
```

## Problemas comunes

| Problema | Solución |
|---|---|
| `ConnectionRefusedError` al ejecutar | RabbitMQ no está corriendo. Revisar con `docker ps` o ejecutar `docker start rabbitmq`. |
| `FileNotFoundError: serviceAccountKey.json` | El archivo no está en la carpeta del proyecto o tiene otro nombre. |
| `JSONDecodeError` al leer la clave | El archivo `serviceAccountKey.json` está vacío; usar la clave real descargada de Firebase. |
| Firestore solo muestra IDs que empiezan con `ACC` | Es normal: se ordenan alfabéticamente. Bajar con el scroll de la columna de documentos. |
| La cola siempre muestra 0 | Es normal con el consumidor activo (ver sección anterior). |

## Seguridad

`serviceAccountKey.json` da acceso total al proyecto de Firebase. No se debe subir a GitHub
ni compartir. Si se usa Git, agregarlo al `.gitignore`:

```
serviceAccountKey.json
```

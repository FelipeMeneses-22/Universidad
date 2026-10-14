import os, re, time, random, requests
from datetime import datetime, timezone
import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://rickandmortyapi.com/api/character"
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB = os.getenv("MONGO_DB", "rick_morty_etl")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "characters_raw")

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
}
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "rick_morty_dw")


def extraer_personajes():
    """Extrae todos los personajes con reintentos ante errores HTTP 429."""
    personajes = []
    url = API_URL

    with requests.Session() as session:
        while url:
            data = None

            for intento in range(5):
                try:
                    respuesta = session.get(url, timeout=30)

                    if respuesta.status_code == 429:
                        retry_after = respuesta.headers.get("Retry-After")

                        try:
                            espera = max(60, int(retry_after))
                        except (TypeError, ValueError):
                            espera = min(30 * (2 ** intento), 300)

                        print(
                            f"API limitada. Intento {intento + 1}/5. "
                            f"Esperando {espera} segundos..."
                        )
                        time.sleep(espera + random.uniform(1, 3))
                        continue

                    respuesta.raise_for_status()
                    data = respuesta.json()
                    break

                except requests.RequestException as error:
                    if intento == 4:
                        raise RuntimeError(
                            f"Error al consultar la API: {error}"
                        ) from error

                    espera = min(10 * (2 ** intento), 120)
                    print(f"Error de conexión: {error}")
                    time.sleep(espera)

            if data is None:
                raise RuntimeError(
                    f"No se pudo descargar la página: {url}"
                )

            personajes.extend(data["results"])
            url = data["info"]["next"]

            print(f"Personajes descargados: {len(personajes)}")

            if url:
                time.sleep(3)

    ids = [p["id"] for p in personajes]

    if len(ids) != len(set(ids)):
        raise ValueError("La API devolvió IDs duplicados.")

    print(f"EXTRACCIÓN: {len(personajes)} personajes")
    return personajes


def cargar_mongodb(personajes):
    """Almacena los documentos originales de la API."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        client.admin.command("ping")
        collection = client[MONGO_DB][MONGO_COLLECTION]
        collection.delete_many({})
        if personajes:
            collection.insert_many(personajes)
        total = collection.count_documents({})
        print(f"MONGODB: {total} documentos almacenados")
        return total
    finally:
        client.close()


def obtener_id(url):
    """Extrae el ID numérico al final de una URL de la API."""
    if not url:
        return None
    match = re.search(r"/(\d+)/?$", url.strip())
    return int(match.group(1)) if match else None


def limpiar_texto(valor):
    """Normaliza textos y convierte vacíos en None."""
    if valor is None:
        return None
    texto = str(valor).strip()
    return texto if texto else None


def convertir_fecha(valor):
    """Convierte ISO 8601 a datetime compatible con MySQL."""
    if not valor:
        return None
    try:
        fecha = datetime.fromisoformat(valor.replace("Z", "+00:00"))
        if fecha.tzinfo is not None:
            fecha = fecha.astimezone(timezone.utc).replace(tzinfo=None)
        return fecha
    except (ValueError, TypeError):
        return None


def transformar(personajes):
    """Prepara dimensiones, personajes y relaciones en español."""
    ubicaciones = {}
    episodios = {}
    lista_personajes = []
    personaje_episodios_set = set()

    for p in personajes:
        origin = p.get("origin") or {}
        current = p.get("location") or {}
        origin_id = obtener_id(origin.get("url"))
        current_id = obtener_id(current.get("url"))

        for loc_id, loc in ((origin_id, origin), (current_id, current)):
            if loc_id is not None:
                ubicaciones[loc_id] = {
                    "ubicacion_id": loc_id,
                    "nombre": limpiar_texto(loc.get("name")) or "Unknown",
                    "url": limpiar_texto(loc.get("url")),
                }

        personaje_id = int(p["id"])
        lista_personajes.append({
            "personaje_id": personaje_id,
            "nombre": limpiar_texto(p.get("name")) or "Unknown",
            "estado": limpiar_texto(p.get("status")),
            "especie": limpiar_texto(p.get("species")),
            "tipo_personaje": limpiar_texto(p.get("type")),
            "genero": limpiar_texto(p.get("gender")),
            "origen_id": origin_id,
            "ubicacion_id": current_id,
            "url_imagen": limpiar_texto(p.get("image")),
            "url_api": limpiar_texto(p.get("url")),
            "creado_en": convertir_fecha(p.get("created")),
        })

        for episode_url in p.get("episode") or []:
            episode_id = obtener_id(episode_url)
            if episode_id is not None:
                episodios[episode_id] = {
                    "episodio_id": episode_id,
                    "url": episode_url,
                }
                personaje_episodios_set.add((personaje_id, episode_id))

    relaciones = [
        {"personaje_id": cid, "episodio_id": eid}
        for cid, eid in sorted(personaje_episodios_set)
    ]

    resultado = {
        "ubicaciones": list(ubicaciones.values()),
        "episodios": list(episodios.values()),
        "personajes": lista_personajes,
        "personaje_episodios": relaciones,
    }

    print(
        "TRANSFORM:",
        f"{len(resultado['personajes'])} personajes,",
        f"{len(resultado['ubicaciones'])} ubicaciones,",
        f"{len(resultado['episodios'])} episodios,",
        f"{len(relaciones)} relaciones",
    )
    return resultado


def crear_esquema(config):
    """Crea la base de datos y las tablas relacionales en español."""
    conn = mysql.connector.connect(**config)
    try:
        cur = conn.cursor()
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DATABASE}` "
            "CHARACTER SET utf8mb4 "
            "COLLATE utf8mb4_unicode_ci"
        )
        cur.execute(f"USE `{MYSQL_DATABASE}`")
        
        sentencias = [
            """
            CREATE TABLE IF NOT EXISTS ubicaciones (
                ubicacion_id INT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                url VARCHAR(500)
            ) ENGINE=InnoDB
            """,
            """
            CREATE TABLE IF NOT EXISTS episodios (
                episodio_id INT PRIMARY KEY,
                url VARCHAR(500) NOT NULL
            ) ENGINE=InnoDB
            """,
            """
            CREATE TABLE IF NOT EXISTS personajes (
                personaje_id INT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                estado VARCHAR(30),
                especie VARCHAR(100),
                tipo_personaje VARCHAR(255),
                genero VARCHAR(30),
                origen_id INT NULL,
                ubicacion_id INT NULL,
                url_imagen VARCHAR(500),
                url_api VARCHAR(500),
                creado_en DATETIME NULL,

                CONSTRAINT fk_personaje_origen
                    FOREIGN KEY (origen_id)
                    REFERENCES ubicaciones(ubicacion_id),

                CONSTRAINT fk_personaje_ubicacion
                    FOREIGN KEY (ubicacion_id)
                    REFERENCES ubicaciones(ubicacion_id)
            ) ENGINE=InnoDB
            """,
            """
            CREATE TABLE IF NOT EXISTS personaje_episodios (
                personaje_id INT NOT NULL,
                episodio_id INT NOT NULL,

                PRIMARY KEY (personaje_id, episodio_id),

                CONSTRAINT fk_pe_personaje
                    FOREIGN KEY (personaje_id)
                    REFERENCES personajes(personaje_id),

                CONSTRAINT fk_pe_episodio
                    FOREIGN KEY (episodio_id)
                    REFERENCES episodios(episodio_id)
            ) ENGINE=InnoDB
            """,
        ]
        
        for sql in sentencias:
            cur.execute(sql)
            
        conn.commit()
        cur.close()
        print(f"MYSQL: esquema {MYSQL_DATABASE} listo en español")
    finally:
        conn.close()


def cargar_mysql(datos):
    """Carga tablas en español respetando claves foráneas."""
    config = {**MYSQL_CONFIG, "database": MYSQL_DATABASE}
    conn = mysql.connector.connect(**config)
    try:
        cur = conn.cursor()

        # 1. Ubicaciones
        cur.executemany(
            """
            INSERT INTO ubicaciones (ubicacion_id, nombre, url)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nombre = VALUES(nombre),
                url = VALUES(url)
            """,
            [(x["ubicacion_id"], x["nombre"], x["url"]) for x in datos["ubicaciones"]],
        )

        # 2. Episodios
        cur.executemany(
            """
            INSERT INTO episodios (episodio_id, url)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE url = VALUES(url)
            """,
            [(x["episodio_id"], x["url"]) for x in datos["episodios"]],
        )

        # 3. Personajes
        cur.executemany(
            """
            INSERT INTO personajes (
                personaje_id, nombre, estado, especie,
                tipo_personaje, genero, origen_id,
                ubicacion_id, url_imagen, url_api, creado_en
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nombre = VALUES(nombre),
                estado = VALUES(estado),
                especie = VALUES(especie),
                tipo_personaje = VALUES(tipo_personaje),
                genero = VALUES(genero),
                origen_id = VALUES(origen_id),
                ubicacion_id = VALUES(ubicacion_id),
                url_imagen = VALUES(url_imagen),
                url_api = VALUES(url_api),
                creado_en = VALUES(creado_en)
            """,
            [
                (
                    x["personaje_id"], x["nombre"], x["estado"],
                    x["especie"], x["tipo_personaje"], x["genero"],
                    x["origen_id"], x["ubicacion_id"],
                    x["url_imagen"], x["url_api"], x["creado_en"],
                )
                for x in datos["personajes"]
            ],
        )

        # 4. Relaciones (personaje_episodios)
        cur.executemany(
            """
            INSERT IGNORE INTO personaje_episodios (personaje_id, episodio_id)
            VALUES (%s, %s)
            """,
            [(x["personaje_id"], x["episodio_id"]) for x in datos["personaje_episodios"]],
        )

        conn.commit()
        print("MYSQL: carga completada correctamente")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def validar():
    """Compara conteos y verifica integridad referencial en español."""
    mongo = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        mongo_count = mongo[MONGO_DB][MONGO_COLLECTION].count_documents({})
    finally:
        mongo.close()

    conn = mysql.connector.connect(**MYSQL_CONFIG, database=MYSQL_DATABASE)
    try:
        cur = conn.cursor()
        conteos = {}
        for tabla in ("personajes", "ubicaciones", "episodios", "personaje_episodios"):
            cur.execute(f"SELECT COUNT(*) FROM {tabla}")
            conteos[tabla] = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*)
            FROM personajes c
            LEFT JOIN ubicaciones o ON c.origen_id = o.ubicacion_id
            WHERE c.origen_id IS NOT NULL AND o.ubicacion_id IS NULL
        """)
        origenes_huerfanos = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*)
            FROM personajes c
            LEFT JOIN ubicaciones l ON c.ubicacion_id = l.ubicacion_id
            WHERE c.ubicacion_id IS NOT NULL AND l.ubicacion_id IS NULL
        """)
        ubicaciones_huerfanas = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*)
            FROM personaje_episodios ce
            LEFT JOIN episodios e ON ce.episodio_id = e.episodio_id
            WHERE e.episodio_id IS NULL
        """)
        episodios_huerfanos = cur.fetchone()[0]

        print("\n--- RESULTADO DE VALIDACIÓN ---")
        print("MongoDB documentos:", mongo_count)
        for tabla, cantidad in conteos.items():
            print(f"MySQL {tabla}: {cantidad}")
        print("Orígenes sin referencia:", origenes_huerfanos)
        print("Ubicaciones sin referencia:", ubicaciones_huerfanas)
        print("Episodios sin referencia:", episodios_huerfanos)

        if conteos["personajes"] != mongo_count:
            print("ADVERTENCIA: no coinciden los personajes.")
        elif any((origenes_huerfanos, ubicaciones_huerfanas, episodios_huerfanos)):
            print("ADVERTENCIA: hay relaciones huérfanas.")
        else:
            print("VALIDACIÓN BÁSICA: correcta")

        cur.close()
    finally:
        conn.close()


def main():
    # EXTRACT
    personajes = extraer_personajes()

    # LOAD 1: almacenamiento raw en MongoDB
    cargar_mongodb(personajes)

    # TRANSFORM: leer de MongoDB y transformar con nomenclatura en español
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        documentos = list(client[MONGO_DB][MONGO_COLLECTION].find({}, {"_id": 0}))
    finally:
        client.close()

    datos = transformar(documentos)

    # LOAD 2: crear esquema y cargar tablas en MySQL
    crear_esquema(MYSQL_CONFIG)
    cargar_mysql(datos)

    # VALIDATE
    validar()


if __name__ == "__main__":
    try:
        main()
    except (requests.RequestException, Error, ValueError) as exc:
        print(f"ERROR ETL: {exc}")
        raise
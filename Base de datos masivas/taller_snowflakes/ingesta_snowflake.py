import snowflake.connector
import os
import getpass

# --- CONFIGURACIÓN DE PARÁMETROS DE CONEXIÓN ---
SNOWFLAKE_USER = 'JFELIPE3944@GMAIL.COM'                  # el que te muestre CURRENT_USER() en la Worksheet
SNOWFLAKE_ACCOUNT = 'DQKYQGS-OW76232'   # ej: ORGANIZACION-CUENTA
SNOWFLAKE_WAREHOUSE = 'TALLER_WH'
SNOWFLAKE_DATABASE = 'TALLER_PYTHON_DB'
SNOWFLAKE_SCHEMA = 'ANALYTICS'

CSV_FILE_PATH = 'ventas_productos.csv'


def ejecutar_pipeline_ingesta():
    conn = None
    cursor = None
    try:
        password = getpass.getpass("Contraseña de Snowflake: ")

        print("1. Estableciendo conexión con Snowflake...")
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=password,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cursor = conn.cursor()
        print("   ✓ Conexión exitosa a Snowflake.")

        # 2. Subir el CSV al Stage interno (PUT)
        print(f"2. Subiendo archivo '{CSV_FILE_PATH}' al Stage Interno '@MI_STAGE_CSV'...")
        ruta = os.path.abspath(CSV_FILE_PATH).replace("\\", "/")
        cursor.execute(f"PUT 'file://{ruta}' @MI_STAGE_CSV OVERWRITE = TRUE")
        print("   ✓ Archivo subido exitosamente al Stage.")

        # 3. Cargar del Stage a la tabla (COPY INTO)
        print("3. Ejecutando COPY INTO para poblar la tabla VENTAS...")
        cursor.execute("TRUNCATE TABLE VENTAS")  # permite re-ejecutar sin duplicar
        copy_query = """
            COPY INTO VENTAS
            FROM @MI_STAGE_CSV/ventas_productos.csv
            FILE_FORMAT = (
                TYPE = 'CSV'
                FIELD_DELIMITER = ','
                SKIP_HEADER = 1
                FIELD_OPTIONALLY_ENCLOSED_BY = '"'
            )
            ON_ERROR = 'CONTINUE'
            FORCE = TRUE;
        """
        cursor.execute(copy_query)
        print("   ✓ Carga de datos completada con éxito.")

        # 4. Validar la ingesta
        print("4. Verificando los datos cargados...")
        cursor.execute("SELECT COUNT(*) AS TOTAL_REGISTROS, SUM(MONTO_TOTAL) AS VENTA_TOTAL FROM VENTAS;")
        resultado = cursor.fetchone()
        print(f"   📊 Resumen Carga -> Total Registros: {resultado[0]}, Venta Total Sumada: ${resultado[1]:,.2f}")

        # 5. Reporte por categoría
        print("\n5. Reporte de Ventas por Categoría:")
        cursor.execute("""
            SELECT CATEGORIA, SUM(CANTIDAD) AS UNIDADES, SUM(MONTO_TOTAL) AS TOTAL
            FROM VENTAS
            GROUP BY CATEGORIA
            ORDER BY TOTAL DESC;
        """)
        filas = cursor.fetchall()
        print(f"   {'Categoría':<15} | {'Unidades':<10} | {'Monto Total':<12}")
        print("   " + "-" * 42)
        for fila in filas:
            print(f"   {fila[0]:<15} | {fila[1]:<10} | ${fila[2]:<12,.2f}")

        # 6. RETO: producto más vendido por unidades
        print("\n6. Producto más vendido (por cantidad de unidades):")
        cursor.execute("""
            SELECT PRODUCTO, SUM(CANTIDAD) AS UNIDADES_VENDIDAS
            FROM VENTAS
            GROUP BY PRODUCTO
            ORDER BY UNIDADES_VENDIDAS DESC
            LIMIT 1;
        """)
        producto, unidades = cursor.fetchone()
        print(f"   🏆 {producto} -> {unidades} unidades vendidas")

    except Exception as e:
        print(f"❌ Error durante el proceso: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("\n7. Conexión cerrada correctamente.")


if __name__ == '__main__':
    ejecutar_pipeline_ingesta()
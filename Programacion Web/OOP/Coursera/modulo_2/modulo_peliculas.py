# Ejercicio nivel 2: Agenda de peliculas.
# Módulo de cálculos.
#
# Temas:
# * Variables.
# * Tipos de datos.
# * Expresiones aritmeticas.
# * Instrucciones basicas y consola.
# * Dividir y conquistar: funciones y paso de parametros.
# * Especificacion y documentacion.
# * Instrucciones condicionales.
# * Diccionarios.
# @author: Cupi2

# ----------------------------------------
# *author : Juan Felipe Meneses Rodriguez
# *Estudio: Semestre II / Ingenieria en sistemas
# *Fecha creación : 20/10/2024
# ----------------------------------------

# NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
# Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
# - nombre (str): Nombre de la pelicula agendada.
# - genero (str): Generos de la pelicula separados por comas.
# - duracion (int): Duracion en minutos de la pelicula
# - anio (int): Anio de estreno de la pelicula
# - clasificacion (str): Clasificacion de restriccion por edad
# - hora (int): Hora de inicio de la pelicula
# - dia (str): Indica que día de la semana se planea ver la película


def crear_pelicula(
    nombre: str,
    genero: str,
    duracion: int,
    anio: int,
    clasificacion: str,
    hora: int,
    dia: str,
) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información
    inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """
    pelicula = {}
    pelicula["nombre"] = nombre
    pelicula["genero"] = genero
    pelicula["duracion"] = duracion
    pelicula["anio"] = anio
    pelicula["clasificacion"] = clasificacion
    pelicula["hora"] = hora
    pelicula["dia"] = dia
    return pelicula


def encontrar_pelicula(
    nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict
) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la
    pelicula cuyo nombre es dado por parametro.
    Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro.
        None si no se encuentra una pelicula con ese nombre.
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    i = 0
    length = len(lista_peliculas)
    encontrado = False
    while (i < length) and not (encontrado):
        pelicula = lista_peliculas[i]
        if pelicula["nombre"] == nombre_pelicula:
            encontrado = True
        elif (i == (length - 1)) and not (encontrado):
            pelicula = None
        i += 1
    return pelicula


def encontrar_pelicula_mas_larga(
    p1: dict, p2: dict, p3: dict, p4: dict, p5: dict
) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
    parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    i = 0
    mayor = 0
    length = len(lista_peliculas)
    while i < length:
        pelicula = lista_peliculas[i]
        if pelicula["duracion"] > mayor:
            mayor = pelicula["duracion"]
            pelicula_mayor = pelicula
        i += 1
    return pelicula_mayor


def duracion_promedio_peliculas(
    p1: dict, p2: dict, p3: dict, p4: dict, p5: dict
) -> str:
    """#Calcula la duracion promedio de las peliculas que entran por parametro.
        #Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas.
        #Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    i = 0
    total = 0
    length = len(lista_peliculas)
    while i < length:
        pelicula = lista_peliculas[i]
        total += pelicula["duracion"]
        i += 1
    promedio = total // length
    horas = promedio // 60
    if horas < 10:
        hora_formato = "0" + str(horas)
    else:
        hora_formato = str(horas)
    if promedio % 60 < 10:
        min_formato = "0" + str(promedio % 60)
    else:
        min_formato = str(promedio % 60)
    return f"{hora_formato}:{min_formato}"


def encontrar_estrenos(
    p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int
) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
        posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida.
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    cadena_nombres = ""
    cant_peli_validas = 0
    i = 0
    length = len(lista_peliculas)
    while i < length:
        pelicula = lista_peliculas[i]
        if pelicula["anio"] > anio:
            if cant_peli_validas == 0:
                nombre = pelicula["nombre"]
                cadena_nombres += f"{nombre}"
                cant_peli_validas = 1
            else:
                nombre = pelicula["nombre"]
                cadena_nombres += f", {nombre}"
        i += 1
    if cant_peli_validas == 0:
        cadena_nombres == "Ninguna"
    return cadena_nombres


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    cant_peli_validas = 0
    i = 0
    length = len(lista_peliculas)
    while i < length:
        pelicula = lista_peliculas[i]
        if pelicula["clasificacion"] == "18+":
            cant_peli_validas += 1
        i += 1
    return cant_peli_validas


def rango_duracion_pelicula(pelicula: dict) -> tuple:
    hora_inicio = pelicula["hora"]
    hora_final = hora_inicio
    duracion = pelicula["duracion"]
    horas = duracion // 60
    hora_final += horas * 100
    minutos = duracion % 60
    str_hora_inicio = str(hora_inicio)
    str_minuto_inicio = f"{str_hora_inicio[-2]}{str_hora_inicio[-1]}"
    minutos = int(str_minuto_inicio) + minutos
    horas = minutos // 60
    hora_final += horas * 100
    minutos = minutos % 60
    hora_final += minutos
    return hora_inicio, hora_final


def reagendar_pelicula(
    peli: dict,
    nueva_hora: int,
    nuevo_dia: str,
    control_horario: bool,
    p1: dict,
    p2: dict,
    p3: dict,
    p4: dict,
    p5: dict,
) -> bool:
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
        si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula,
        y en caso de que el usuario haya pedido control horario verifica que se cumplan
        las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    i = 0
    length = len(lista_peliculas)
    se_pudo = True
    # Control horario
    if control_horario:
        if 559 < nueva_hora < 2300:
            if peli["genero"] in "drama":
                if nuevo_dia == "viernes":
                    se_pudo = False
            if peli["genero"] in "documental":
                if nueva_hora < 2159:
                    se_pudo = False
    # Reagendar
    while (i < length) and se_pudo:
        pelicula = lista_peliculas[i]
        if pelicula["dia"] == nuevo_dia:
            rango_pelicula = rango_duracion_pelicula(pelicula)
            peli_copy = peli.copy()
            peli_copy["hora"] = nueva_hora
            rango_peli = rango_duracion_pelicula(peli_copy)
            if not (
                (rango_pelicula[0] > rango_peli[1])
                or (rango_pelicula[1] < rango_peli[0])
            ):
                se_pudo = False
        i += 1
    return se_pudo


def clasificacion_a_numero(peli: dict) -> int:
    if peli["clasificacion"] == "todos":
        edad = 0
    elif peli["clasificacion"] == "7+":
        edad = 7
    else:
        edad = peli["clasificacion"][0:2]
        edad = int(edad)
    return edad


def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la
        pelicula que entra igualmente por parametro.
        Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    se_puede = True
    if edad_invitado < 18:
        if (peli["genero"] in "terror") and (edad_invitado < 15):
            se_puede = False
        if not (peli["genero"] in "familiar") and (edad_invitado < 11):
            se_puede = False
        if edad_invitado < clasificacion_a_numero(peli):
            if not (autorizacion_padres):
                se_puede = False
            if peli["genero"] in "documental":
                se_puede = False
    return se_puede

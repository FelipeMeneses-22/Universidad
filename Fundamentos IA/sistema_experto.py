# -*- coding: utf-8 -*-
# Base de Conocimientos: Lista de Reglas
reglas = [
    {"si": ["tiene_pelo", "da_leche"], "entonces": "es_mamifero"},
    {"si": ["tiene_dos_patas", "pone_huevos","hace_cuak"], "entonces": "es_pato"},
    {"si": ["tiene_plumas", "vuela", "pone_huevos"], "entonces": "es_ave"},
    {"si": ["es_mamifero", "come_carne"], "entonces": "es_carnivoro"},
    {"si": ["es_pato", "levita"], "entonces": "es_ornitorrinco"},
    {"si": ["es_carnivoro", "tiene_color_pardo", "tiene_rayas_negras"], "entonces": "es_tigre"}
]

# Base de Hechos (inicialmente vacía)
hechos = []

print("Sistema Experto: Identificación de Animales")
print("Responde 'si' o 'no' a las siguientes preguntas:\n")

# BANDERA para controlar si debemos seguir preguntando
preguntar = True

# Bucle principal: mientras haya motivos para preguntar o inferir
while preguntar:
    # FASE 1: INFERENCIA (Encadenamiento hacia Adelante)
    # Intento aplicar todas las reglas con los hechos que tengo
    cambio = True
    while cambio:
        cambio = False
        for regla in reglas:
            # Verifica si TODAS las condiciones de la regla están en los hechos
            # y si la conclusión AÚN NO está en los hechos (para no repetir)
            if all(condicion in hechos for condicion in regla["si"]):
                if regla["entonces"] not in hechos:
                    hechos.append(regla["entonces"])
                    print(f"[Sistema infirió: {regla['si']} -> {regla['entonces']}]")
                    cambio = True

    # FASE 2: PREGUNTAS AL USUARIO
    # Ahora busco reglas que casi se cumplan, pero les falta 1 hecho.
    # Recorro todas las reglas y todas sus condiciones.
    hecho_agregado = False
    for regla in reglas:
        for condicion in regla["si"]:
            # Solo me interesan condiciones que NO sean conclusiones de otras reglas (hechos básicos)
            # y que aún no las conozca (no estén en la base de hechos).
            # Además, evito preguntar por conclusiones (que empiezan con "es_")
            if condicion not in hechos and not condicion.startswith('es_'):
                respuesta = input(f"¿El animal {condicion.replace('_', ' ')}? (si/no): ").lower().strip()
                if respuesta == 'si':
                    hechos.append(condicion)
                    print(f"Hecho agregado: '{condicion}'")
                    hecho_agregado = True
                    # Si agregué un hecho, debo romper los bucles y volver a FASE 1 (Inferir)
                    break # Rompe el bucle interno 'for condicion in regla["si"]:'
        if hecho_agregado:
            break # Rompe el bucle externo 'for regla in reglas:' para volver a inferir

    # CRITERIO DE PARADA: Si en toda la FASE 2 no agregué NINGÚN hecho nuevo,
    # es porque no hay más preguntas útiles que hacer. Salimos del bucle principal.
    if not hecho_agregado:
        preguntar = False

# Mostrar el resultado final
print("\n" + "="*50)
print("--- CONCLUSIÓN FINAL ---")
# Busco todas las conclusiones a las que llegó el sistema (hechos que empiezan con 'es_')
conclusiones = [hecho for hecho in hechos if hecho.startswith('es_')]

if conclusiones:
    print(f"¡El animal probablemente es un {conclusiones[-1].replace('es_', '')}!")
else:
    print("No pude identificar al animal con certeza.")

print(f"\nTodos los hechos conocidos: {hechos}")
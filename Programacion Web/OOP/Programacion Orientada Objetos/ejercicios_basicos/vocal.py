
# Vocal mas comun
# * Crea un función que reciba un texto y retorne la vocal que
#  * más veces se repita.
#  * Ten cuidado con algunos casos especiales.
#  * Si no hay vocales podrá devolver vacío.

# Declaramos las vocales  
vocales = {
    "a":0,
    "e":0,
    "i":0,
    "0":0,
    "u":0,
}

# Escrribimos el texto
texto = input("Escribe algo = ")

for letras in texto:
    texto = texto.lower()
    if letras in texto:
        vocales[letras] =+1
        
vocal_comun =""
conteo = 0

for vocal in vocales:
    if vocales[vocal] > conteo:
        conteo = vocales[vocal]
        vocal_comun = vocal
        
print(f"La vocal más común es: '{vocal_comun}'")
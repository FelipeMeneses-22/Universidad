# Ejercicio 1
class Persona:
    def __init__(self, nombre, edad, ocupacion) -> None:
        # Declaramos los atributos de la clase
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def descripcion(self) -> str:
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad} y trabajo como leñador"

persona = Persona("Felipe", 22, "Leñador")

print(persona.descripcion())

def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    # Definimos las palabras clave que le gustan a Pedro
    palabras_clave = ["programacion", "matematica", "filosofia", "literatura"]
    
    # Contador para las materias que le gustan a Pedro
    contador = 0
    
    # Lista de las materias a evaluar
    materias = [nombre_materia_1, nombre_materia_2, nombre_materia_3]
    
    # Recorremos cada materia y contamos si contiene alguna de las palabras clave
    for materia in materias:
        for palabra in palabras_clave:
            if palabra in materia:
                contador += 1
                break  # Si encuentra una palabra clave, no es necesario seguir buscando en la misma materia

    return contador

# Ejemplos de uso
print(conteo_de_materias("matematica avanzada", "historia", "filosofia moderna"))  # Retorna 2
print(conteo_de_materias("programacion en python", "arte", "literatura universal"))  # Retorna 2
print(conteo_de_materias("quimica", "biologia", "matematica discreta"))  # Retorna 1
print(conteo_de_materias("fisica", "tecnologia", "dibujo") )  # Retorna 0
## CLASE ESTUDIANTE: CREA UNA CLASE ESTUDIANTE QUE TENGA LOS ATRIBUTOS NOMBRE, EDAD, GRADO Y PROMEDIO. AÑADE UN MÉTODO ACTUALIZAR_PROMEDIO QUE ACEPTE UNA NUEVA CALIFICACIÓN Y ACTUALICE EL PROMEDIO. LUEGO, CREA OTRO MÉTODO DETALLES_ESTUDIANTE QUE DEVUELVA UNA DESCRIPCIÓN DEL ESTUDIANTE.


class Estudiante:
    def __init__(self, nombre, edad, grado, promedio) -> None:
        self.nombre = nombre
        self.edad = int(edad)
        self.grado = grado
        self.promedio = float(promedio)

    def actualizarPromedio(self):
        calificaciones = []
        #Formamos un ciclo de 3 notas
        for i in range(3):
            try:
                print("____________________________________________________________\n")
                total = float(input(f"            Actualización de promedio\n            Ingrese nota {i+1} :  "))
                calificaciones.append(total)
                
            except ValueError:
                print("            Ingrese una calificación valida.")


        resultado = sum(calificaciones) / len(calificaciones)
        self.promedio = (resultado + self.promedio)/2 
        
        if self.promedio <= 5:
            print(f"____________________________________________________________\n\
                llorelo, Perdiste con {self.promedio}")
        else:
            print(f"            Vamos donde las puticas a celebrar - Ganaste con {self.promedio}")
            

    def __str__(self):
        return f"____________________________________________________________\n \n\
            Datos del estudiante \n\
            Nombre : {self.nombre} \n\
            Edad : {self.edad} \n\
            grado : {self.grado} \n\
            promedio : {self.promedio} \n\
                                "

print("____________________________________________________________\n")

nombre = input("            Ingresa el nombre del estudiante : ")
edad = input("            Ingresa la edad del estudiante : ")
grado = input("            Ingrese el grado academico : ")
promedio = input("            Ingrese el promedio por el cual calificar : ")


edu = Estudiante(nombre,edad,grado,promedio)

print(edu.__str__())

print(edu.actualizarPromedio())

print(edu.__str__())
#Ejercicio 4: Sistema de reservas de hotel
#Enunciado: Desarrolla un sistema de gestión de reservas de hotel. Crea una clase Habitacion con los atributos número de habitación y capacidad. La clase HabitacionVIP hereda de Habitacion y añade un atributo adicional de servicios extra. Implementa setters y getters para los atributos. El menú debe permitir:
#
#Registrar habitaciones.
#Registrar habitaciones VIP.
#Mostrar todas las habitaciones.
#Mostrar habitaciones VIP con sus servicios extra.
#Clases involucradas:
#
#Habitacion: número de habitación, capacidad.
#HabitacionVIP: hereda de Habitacion y añade servicios extra.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 17/10/2024
# ----------------------------------------

class Habitacion: # clase
    def __init__(self, num_habitacion, capacidad) -> None:
        self.num_habitacion = num_habitacion
        self.capacidad = capacidad

    def __str__(self) -> str:
        return f"Numero de la habitacion : {self.num_habitacion}, Capacidad de la habitacion : {self.capacidad}"
    
    @property # getter
    def getHabitacion(self):
        return self.num_habitacion
    
    def setHabitacion(self, num_habitacion): # setter
        self._num_habitacion = num_habitacion

class HabitacionVip(Habitacion):
    def __init__(self, num_habitacion, servicio_extra,capacidad, ) -> None:
        super().__init__(num_habitacion, capacidad)
        self.servicio_extra = servicio_extra
    
    def __str__(self) -> str: # heredamos la descripcion de las habitaciones
        return f"{super().__str__()} Nivel : {self.servicio_extra}"

    @property # getter
    def getServicio_extra(self):
        return self.servicio_extra
    
    def setservicio_extra(self, servicio_extra): # setter
        self._num_servicio_extra = servicio_extra

class sistemaHotel:
    def __init__(self) -> None:
        self.listaHabitacion = [] # Lista vacia de las habitaciones

    def guardarRegistro(self, habitacion):
        self.listaHabitacion.append(habitacion) # Agregamos los datos del cliente

    def registratHabitacion(self):
        # Formulario de registro
        print("____________________________________________")
        n_habitacion = input("    Ingrese numero de la habitacion : ")
        capacidad = int(input("    Ingrese la capacidad de la habitacion : "))
        categoria = input("    ¿Su habitacion tiene servicio extra? (s/n) : ").lower()

        # Condicional para saber si es vip o no
        if categoria == "s":
            clase = input("    ¿Que clase de servicio? VIP - Master :").lower()
            habitacion = HabitacionVip(n_habitacion,clase,capacidad,)
            self.guardarRegistro(habitacion)
            print("-----Habitacion creada con exito-----")
        elif categoria == "n":
            habitacion = Habitacion(n_habitacion, capacidad)
            self.guardarRegistro(habitacion)
                

    # metodo que muestra las habitaciones registradas
    def mostrarHabitacion(self):
        if self.listaHabitacion:
            for habitacion in self.listaHabitacion:
                print (habitacion)
                
        else:
            print("No hay habitaciones D:")
                


    # menu
    def main (self):
        while True:
            while True:
                try:
                    opcionPanel = int(input("____________________________________________\n \n\
    Sistema de Gestión de habitaciones \n \n\
        1. Registrar Habitacion Normal - VIP \n\
        2. Mostrar habitaciones Actuales \n \n\
        3. Salir \n \n\
    Su opcion: "))
                    if 1 <= opcionPanel <= 3:
                        break
                    else:
                        print("\n    Opcion ingresada no valida.")
                except ValueError:
                    print("\n    Caracter ingresado no valido.")

            if opcionPanel == 1:
                self.registratHabitacion()
            elif opcionPanel == 2:
                self.mostrarHabitacion()
            elif opcionPanel == 3:
                print("____________________________________________\n\
    Saliste del panel, ten un buen dia. \n\
____________________________________________ \n \n")
                break
    
h = sistemaHotel()
h.main()
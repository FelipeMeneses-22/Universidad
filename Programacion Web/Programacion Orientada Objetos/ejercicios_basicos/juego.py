
# Juegos ataque y defensa por turnos 
#  1 . cada jugador comienza con 50 puntos de vida = HECHO
#  2 . de forma aletoria se decide quien comienza la ronda atacando si usario a o usuario b = HECHO
#  3 . en cada turno cada usuario elegirá sin mostrarle al contrincante un numero del 1 a 5  = HECHO
#  4 . si el usuario a ataca con el numero 3 y el b coloca en defensa el numero 3 el usuario b no será dañado HECHO
#  5 . si en cambio no adivina el numero se restara 10 puntos de vida al usuario que estaba defendiendo HECHO
#  6 . en cada ronda cambiar de turno entre atacante y defensa , termina cuando alguno de los dos caiga en combate 

# vida de los jugadores definidos de forma global jugadores
vida_1 = 50
vida_2 = 50

# elegimos de forma "aleatoria"
print("----------------------------------------------------------")
print("Elige que jugador inicia primero si jugador 1 o 2")

try:
    empieza = int(input('ingrese el numero de jugador = '))
except ValueError:
    print(" Tiene que ser un numero 1 o 2 noo una letraq")

# iniciamos un bucle donde las vidas de los jugadores hasta llegar a cero se termina el bucle
print("----------------------------------------------------------")
while vida_1 > 0 and vida_2>0:
    
    # iniciamos una condicional donde si iniia el jugador 1 ataca 
    if empieza == 1:
        #informamos que el jygador 1 ataca
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("Empieza el jugador 1 ")
        #se ingresa el numero de ataque y defensa del 1 a 5
        try:
            ataque = int(input("jugador 1 : Ingrese el numero de ataque entre 1 a 5 = "))
            defensa = int(input("Jugador 2 : Ingrese el numero de defensa entre 1 a 5 = "))
        except ValueError:
            print("que no ponga letras mano, solo numbers")

            # si el ataque y la defensa son iguales entonces se defiende el jugador 2
        if ataque == defensa:
                print("el jugador 2 se defendio")
            #si no son iguales se le restan 10 al jugador 2
        else: 
            vida_2 -=10
            print("el jugador 2 perdio 10 de vida")
            print("-------------------------------------")
    else:
        print("-------------------------------------")
        # aca empieza el jugador 2
        print("empieza el jugador 2")
        try:
            #el juadaor 2  empieza eligiendo el numero de ataque 
            ataque = int(input("Ingrese el numero de ataque entre 1 a 5 = "))
            # aca el jugador 1 ingresa el numero defensa
            defensa = int(input("Ingrese el numero de defensa entre 1 a 5 = "))
        except ValueError:
            print("Digale a su amigo que no ponga letras")
        # una condicional que si el ataque y la defensa son iguales se anula el ataque
        if ataque == defensa:
            print("el jugador 1 se defendio")
        else:
        # Condicional donde si el ataque es mas alto que la defensa se le resta 10 de vida al jugador 1
            vida_1 -=10
            print("El jugador 1 perdio 10 de vida")
            
    #conteo de puntos de vida
        print("-------------------------------------")
    print(f"vida del jugador 1 : {vida_1} ---- vida del jugaor 2 : {vida_2}")
    print(f"El ganador es {empieza}")
    
    #se rotan los turnos
    empieza =1 if empieza == 2 else 2
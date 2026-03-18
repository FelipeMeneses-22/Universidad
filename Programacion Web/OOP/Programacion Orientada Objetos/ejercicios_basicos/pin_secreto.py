
# Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario 'login correcto'. Sino, 'llamando al policía'.i

pin_secreto = 123
intentos = 3

# se crea un bucle donde se repite hasta que la contraseña sea correcta
while intentos < 0  :
    # le pedimos al usuario que ingrese un pin
    pin = input("ingrese la contraseña : ")
    
    # abrimos una condicional donde si el pin es correcto, muestre el mensaje
    if pin == pin_secreto:
        print("Login correcto")
        
        # Detenemos el bucle 
        break
    # cerramos la condicional restandole un intento por cada pin incorrecto
    else:
        intentos -= 1
        print("llama a la policia bro")
        
        #el bucle es infinito al parecer, no se por que si tiene el break

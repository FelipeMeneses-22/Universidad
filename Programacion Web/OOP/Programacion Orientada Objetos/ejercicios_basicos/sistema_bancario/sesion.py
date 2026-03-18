
usuario_prueba = "felipe"
password_prueba = 123

# ingreso de usuario
def login():
    # ingrese el usuario ya estableceido
    usuario = input("Ingrese el usuario : ")
    #su contraseña ya establecida
    password = int(input("Ingrese la contraseña : "))
    
    #condicional donde confirmamos que el usuario y la contraseña sean correctos
    if usuario == usuario_prueba and password == password_prueba:
        # si es correcto inicia sesion
        print(" Inicio de sesión ")
        return True
    else:
        # si es falso cierra sesion
        print(" Error al ingresar")
        return False 
from pokemons import *
from funs import *
from gba import *

salir = False

while salir == False:
    limpiar()
    user_inicio = menu_principal()

    if user_inicio == '1': # Usuario
        print("En construccion USUARIOS...")
        salir_usuarios = False
        while salir_usuarios == False:
            limpiar()
            user_option_user = menu_usuario()
            if user_option_user == '1': # Login
                print("En construccion...login")
            elif user_option_user == '2': # logout
                print("En construccion...logout")
            elif user_option_user == '3': # alta
                print("En construccion...altas")
            elif user_option_user == '4': # baja
                print("En construccion...bajas")
            elif user_option_user.upper() == 'Q': # exit
                print("Cerrando menu users...")
                wait = input("")
                salir_usuarios = True
    
    elif user_inicio == '2': # Juego
        game()
        wait = input(" ")
        limpiar()

    elif user_inicio.upper() == 'Q': # Usuario
        print("Cerrando aplicacion...")
        salir = True
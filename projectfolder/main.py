import datetime
import bcrypt

from pokemons import *
from funs import *
from gba import *

salir = False

# contraseñas usadas "1234"

server_token = None
user_token = {"expired_date": datetime.datetime.today(), "token": "invite"}

while salir == False:
    limpiar()
    user_inicio = menu_principal()
    if user_inicio == '1': # Usuario
        salir_usuarios = False
        server_token = None
        user_token = {"expired_date": datetime.datetime.today(), "token": "invite"}
        while salir_usuarios == False:
            limpiar()
            user_option_user = menu_usuario()
            if user_option_user == '1': # Crear usuario
                print("MENU CREAR USUARIO")
                user_name = input("User name: ")
                users = read_json("users.json")
                users_names = [user["name"] for user in users["data"]]
                try:
                    users_names.index(user_name)
                    print("El usuario ya existe")
                except ValueError:
                    user_pwd = input("Password: ")
                    users = read_json("users.json")
                    new_user = {"name": user_name, "pwd": bcrypt.hashpw(user_pwd.encode(), bcrypt.gensalt()).decode(), "user_since": datetime.date.today().isoformat()}
                    users["data"].append(new_user)
                    create_user(users, "users.json")
                    print("Usuario creado")
            elif user_option_user == '2': # log in
                print("-----------------------")
                print("MENU LOG IN")
                user_name = input("Name: ")
                user_pwd = input("Password: ")
                users = read_json("users.json")
                encontrado = False
                user_token = {"expired_date": datetime.datetime.today(), "token": "invite"}
                server_token = None
                for user in users["data"]:
                    if user["name"] == user_name:
                        encontrado = True
                        if bcrypt.checkpw(user_pwd.encode(), user["pwd"].encode()):
                            print("Log in...")
                            user_token = {"expired_date": datetime.datetime.today(), "token": bcrypt.hashpw(user_pwd.encode(), bcrypt.gensalt())}
                            server_token = user_token["token"] # Asignamos server_token para que tenga acceso a la zona restringida
                        else:
                            print("Password incorrecto")
                if encontrado == False:
                    print("Usuario no encontrado")
            elif user_option_user.upper() == 'Q': # exit
                print("Cerrando menu users...")
                wait = input("")
                salir_usuarios = True
    elif user_inicio == '2': # Juego
        if user_token:
            if (user_token["expired_date"] + datetime.timedelta(seconds=30)) > datetime.datetime.today():
                #if bcrypt.checkpw(server_token.encode(), user_token["token"]):
                if user_token["token"] == server_token:
                    print("-----------------------")
                    print("ZONA RESTRINGIDA")
                    print("Acceso permitido...")
                    print("Disfruta del juego...!!!")
                    user = input("")
                    game()
                    wait = input(" ")
                    limpiar()
        print("No estas logueado")
    elif user_inicio.upper() == 'Q': # Usuario
        print("Cerrando aplicacion...")
        salir = True
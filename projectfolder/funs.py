#from pokemons import *
import random
import os

title_game = " POKEMON ".center(50, "#")
texto_1 = "Oak: Bienvenido al MUNDO POKEMON!!!\nTienes que seleccionar 3 Pokemon para poder combatir contra tu contrincante...."

def limpiar():
	os.system("clear")

def menu_principal():
    print(" MENU PRINCIPAL ".center(50, "#"))
    print("1. Usuario")
    print("2. Jugar POKEMON")
    print("Q. Quitar")
    print("----------------")
    user = input("Opcion: ")
    return user

def menu_usuario():
    print(" MENU USUARIOS ".center(50, "#"))
    print("1. Login")
    print("2. Alta usuario")
    print("3. Baja usuario")
    print("4. Cambiar contraseña")
    print("Q. Quitar")
    print("----------------")
    user = input("Opcion: ")
    return user

def validate_inicio(valor, total_pokemons):
    try:
        entero = int(valor)
        if entero >= 1 and entero <= total_pokemons:
            validate = True
            return validate
        else:
            pass
            validate = False
            return validate
    except ValueError:
        pass
        validate = False
        return validate

def inicio(pokemons_list):
    limpiar()
    print(title_game)
    select_pokemon = 3
    pokemons_playerA = []
    pokemons_playerB = []
    print(texto_1)
    wait = input(" ")
    rest_pokemons = pokemons_list.copy()
    print(f"Pokemons disponibles : ({len(pokemons_list)})")
    #[print(f"{i+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for i, pokemon in enumerate(rest_pokemons)]
    wait = input(" ")
    for i in range (select_pokemon):
        validate = False
        while validate == False:
            limpiar()
            print(title_game)
            [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(rest_pokemons)]
            user = input(f"Pokemon numero {i+1}: ")
            validate = validate_inicio(user, len(rest_pokemons))
            if not validate:
                print('\nLo siento, el valor no es valido, vuelva a intentarlo...')
                wait = input("")
        user = int(user)
        pokemons_playerA.append(rest_pokemons[user-1])
        rest_pokemons.pop(user-1)
        limpiar()
        print(title_game)
        print("Tu rival ha elegido a...")
        rival = random.randrange(len(rest_pokemons))
        print(rest_pokemons[rival-1])
        pokemons_playerB.append(rest_pokemons[rival-1])
        rest_pokemons.pop(rival-1)
        print("----------------")
        wait = input(" ")
    limpiar()
    print(title_game)
    print("TUS POKEMONS: ")
    [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(pokemons_playerA)]
    print("----------------")
    print("POKEMONS DEL RIVAL")
    [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(pokemons_playerB)]
    print("----------------")
    wait = input(" ")
    return(pokemons_playerA, pokemons_playerB)

def menu_combat():
    validate = False
    while validate == False:
        limpiar()
        print("----------------")
        print("1. Atacar")
        print("2. Cambiar Pokemon")
        option_menu_combat = input("Opcion: ")
        if option_menu_combat == '1' or option_menu_combat == '2':
            validate = True
            option_menu_combat = int(option_menu_combat)-1
        else:
            print('\nLo siento, el valor no es valido, vuelva a intentarlo...')
            wait = input("")
    return option_menu_combat

def combat(pokemon_atack, pokemon_defen):
    validate = False
    while validate == False:
        print("----------------")
        print(f"Ataca: {pokemon_atack.name}")
        print("Elige un ataque de tu pokemon:")
        for i, attack in enumerate(pokemon_atack.attacks):
            print(f"{i+1}. {attack}")
        user = input("Opcion: ")
        validate = validate_inicio(user, len(pokemon_atack.attacks))
        if not validate:
                print('\nLo siento, el valor no es valido, vuelva a intentarlo...')
                wait = input("")
    user = int(user)-1
    pokemon_defen.recive_damage(pokemon_atack.attacks[user])
    print("----------------")
    print(pokemon_defen)

def change_pokemon(pokemons_player, pokemon_atack):
    rest_pokemons = pokemons_player.copy()
    rest_pokemons.remove(pokemon_atack)
    validate = False
    while validate == False:
        print("----------------")
        print("Tus pokemos:")
        [print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(rest_pokemons)]
        user = input("Pokemon: ")
        validate = validate_inicio(user, len(rest_pokemons))
        if not validate:
            print('\nLo siento, el valor no es valido, vuelva a intentarlo...')
            wait = input("")
    user = int(user)-1
    pokemon_change = rest_pokemons[user]
    print("----------------")
    print(f"Has cambiado a {rest_pokemons[user]}")
    return pokemon_change

def turno_pj(pokemons_player, pokemon_atack, pokemon_defen, cont_turnos, option_submenu_ok):
    limpiar()
    print("----------------")
    print(f"TURNO:{cont_turnos} --- {pokemon_atack.name}")
    option_menu_combat = menu_combat()
    if option_menu_combat == 0: # atacar
        combat(pokemon_atack, pokemon_defen)
        option_submenu_ok = False
    elif option_menu_combat == 1:   # cambiar de Pokemon
        pokemon_atack = change_pokemon(pokemons_player, pokemon_atack)
        option_submenu_ok = False
    return option_submenu_ok, pokemon_atack


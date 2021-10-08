#from pokemons import *
import random

texto_1 = "Oak: Bienvenido al MUNDO POKEMON!!!\nTienes que seleccionar 3 Pokemon para poder combatir contra tu contrincante...."

def inicio(pokemons_list):
    print("----------------")
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
        [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(rest_pokemons)]
        user = int(input(f"Pokemon numero {i+1}: "))
        pokemons_playerA.append(rest_pokemons[user-1])
        rest_pokemons.pop(user-1)
        print("----------------")
        rival = random.randrange(len(rest_pokemons))
        print(rest_pokemons[rival-1])
        pokemons_playerB.append(rest_pokemons[rival-1])
        rest_pokemons.pop(rival-1)
        print("----------------")
    print("Tus Pokemons: ")
    [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(pokemons_playerA)]
    print("----------------")
    print("Pokemosn del rival")
    [print(f"{j+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for j, pokemon in enumerate(pokemons_playerB)]
    print("----------------")
    return(pokemons_playerA, pokemons_playerB)

def menu_combat():
    print("1. Atacar")
    print("2. Cambiar Pokemon")
    option_menu_combat = int(input("Opcion: "))-1
    return option_menu_combat

def combat(pokemon_atack, pokemon_defen):
    print("----------------")
    print(f"Ataca: {pokemon_atack.name}")
    print("Elige un ataque de tu pokemon:")
    for i, attack in enumerate(pokemon_atack.attacks):
        print(f"{i+1}. {attack}")
    user = int(input("Opcion: ")) - 1
    pokemon_defen.recive_damage(pokemon_atack.attacks[user])
    print("----------------")
    print(pokemon_defen)

def change_pokemon(pokemons_player, pokemon_atack):
    rest_pokemons = pokemons_player.copy()
    rest_pokemons.remove(pokemon_atack)
    print("----------------")
    print("Tus pokemos:")
    [print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(rest_pokemons)]
    user = int(input("Pokemon: "))-1
    pokemon_change = rest_pokemons[user]
    print("----------------")
    print(f"Has cambiado a {rest_pokemons[user]}")
    return pokemon_change

def turno_pj(pokemons_player, pokemon_atack, pokemon_defen, cont_turnos, option_submenu_ok):
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


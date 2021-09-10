#from pokemons import *

texto_1 = "Oak: Bienvenido al MUNDO POKEMON!!!\nTienes que seleccionar 3 Pokemon para poder combatir contra tu contrincante...."

def inicio(pokemons_list):
    print("----------------")
    print(texto_1)
    wait = input(" ")
    rest_pokemons = pokemons_list.copy()
    print(f"Pokemons disponibles : ({len(pokemons_list)})")
    [print(f"{i+1}. {pokemon.name} - HP: {pokemon.HP} - {pokemon.element}") for i, pokemon in enumerate(rest_pokemons)]
    wait = input(" ")
    print("----------------")

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


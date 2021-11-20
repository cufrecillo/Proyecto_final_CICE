from pokemons import *
from funs import *

def game():

    pokemons_playerA, pokemons_playerB = inicio(pokemons)
    pokemon_a = random.choice(pokemons_playerA)
    pokemon_b = random.choice(pokemons_playerB)
    limpiar()
    print(title_game)
    print("LOS POKEMONS QUE VAN A COMENZAR SON...")
    print(pokemon_a)
    print("----------------")
    print(pokemon_b)
    wait = input(" ")

    cont_turnos = 0
    pokemon_alive = True

    while pokemon_alive:
        limpiar()
        cont_turnos += 1

        option_submenu_ok = True
        while option_submenu_ok:
            option_submenu_ok, pokemon_a = turno_pj(pokemons_playerA, pokemon_a, pokemon_b, cont_turnos, option_submenu_ok)
        if pokemon_b.is_alive == False:
            pokemon_alive = False
        else:
            option_submenu_ok = True
            while option_submenu_ok:
                option_submenu_ok, pokemon_b = turno_pj(pokemons_playerB, pokemon_b, pokemon_a, cont_turnos, option_submenu_ok)
            if pokemon_a.is_alive == False:
                pokemon_alive = False
    if pokemon_a.is_alive:
        print("\nHas ganado!!!!")
    else:
        print("\nPerdiste la partida, vuelve a intentarlo")




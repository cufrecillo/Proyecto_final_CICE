from pokemons import *
from funs import *

print(" POKEMON ".center(50, "#"))
# inicio(pokemons)
# CREAR OPCION AL INICIO PARA ELEGIR POKEMONS

# pokemons_playerA = [charmander, squirtle, meganium]
# pokemons_playerB = [bulbasaur, vulpix, golduck]

pokemons_playerA, pokemons_playerB = inicio(pokemons)

pokemon_a = random.choice(pokemons_playerA)
pokemon_b = random.choice(pokemons_playerB)
print(pokemon_a)
print("----------------")
print(pokemon_b)

cont_turnos = 0
pokemon_alive = True

while pokemon_alive:
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




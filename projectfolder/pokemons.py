import random
from funs import *

elements = ["fire", "grass", "water"]
# fire > grass
# grass > water
# water > fire
# if > 1.5 // if < 0.5
#     fire grass water
# Fire    1   1.5   0.5
# GRass  0.5   1    1.5
# water  1.5   0.5   1

class Pokemon:

    count = 0

    @classmethod
    def set_count(cls):
        cls.count += 1

    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []
        self.is_alive = True
        Pokemon.set_count()

    def __str__(self):
        if self.is_alive == True:
            return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"
        else:
            return f"El pokemon {self.name} fue derrotado..."

    def learn(self, attack):
        return self.attacks.append(attack)

    def recive_damage(self, attack):
        damage = random.randint(0, attack.damage)
        print(attack.element)
        print(self.element)
        if self.element == attack.element:
            damage_final = damage
            self.HP -= damage_final
        else:
            if attack.element == "fire":
                if self.element == "grass":
                    damage_final = damage *1.5
                    self.HP -= damage_final
                elif self.element == "water":
                    damage_final = damage *0.5
                    self.HP -= damage_final
            elif attack.element == "grass":
                if self.element == "water":
                    damage_final = damage *1.5
                    self.HP -= damage_final
                elif self.element == "fire":
                    damage_final = damage *0.5
                    self.HP -= damage_final
            elif attack.element == "water":
                if self.element == "fire":
                    damage_final = damage *1.5
                    self.HP -= damage_final
                elif self.element == "grass":
                    damage_final = damage *0.5
                    self.HP -= damage_final
        print(f"{self.name} recibe un daño de: {damage_final}")
        if self.HP <= 0:
            self.is_alive = False

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: {self.damage}"

# elements = ["fire", "grass", "water"]
# POKEMONS
charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)
vulpix = Pokemon("Vulpix", elements[0], 100)
golduck = Pokemon("Golduck", elements[2], 150)
meganium = Pokemon("Meganium", elements[1], 170)

# ATTACKS
flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor_leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 35)

charmander.learn(flamethrower)
charmander.learn(razor_leaf)
bulbasaur.learn(razor_leaf)
bulbasaur.learn(surf)
squirtle.learn(surf)
vulpix.learn(flamethrower)
golduck.learn(surf)
golduck.learn(razor_leaf)
meganium.learn(razor_leaf)

pokemons = [charmander, squirtle, bulbasaur, vulpix, golduck, meganium]
print(Pokemon.count)
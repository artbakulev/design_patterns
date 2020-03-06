import random

from Strategy.abstract import Weapon, Hero

SWORD = Weapon('sword', random.randint(10, 100))
BOW = Weapon('bow', random.randint(10, 100))
BOOMERANG = Weapon('boomerang', random.randint(10, 100))

SWORDSMAN = Hero('SWORDSMAN', 100, SWORD)
ARCHER = Hero('ARCHER', 100, BOW)
BOOMERANGER = Hero('BOOMERANGER', 100, BOOMERANG)

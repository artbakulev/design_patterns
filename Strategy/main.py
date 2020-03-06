from Strategy.abstract import Battle
from Strategy.concrete import SWORDSMAN, ARCHER, BOOMERANGER

if __name__ == '__main__':
    battle = Battle(SWORDSMAN, ARCHER, BOOMERANGER)
    battle.running()

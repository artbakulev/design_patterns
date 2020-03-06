import random


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.alive = True
        self.weapon: [Weapon, None] = None

    def get_damage(self, hp):
        if self.hp <= hp:
            self.hp = 0
            self.alive = False
        else:
            self.hp -= hp
        return self.hp

    @property
    def is_alive(self) -> bool:
        return self.alive

    def say_hello(self):
        print(f'Hello! I\'m {self.name}!')


class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def hit(self, character: Character) -> int:
        return character.get_damage(self.__damage)

    @property
    def damage(self):
        return self.__damage

    @property
    def name(self):
        return self.__name


class Hero(Character):
    def __init__(self, name, hp, weapon: Weapon):
        super().__init__(name, hp)
        self.__weapon = weapon

    def hit(self, character: Character):
        hp = self.__weapon.hit(character)
        print(f'{self.name} hit {character.name} with {self.__weapon.name}, '
              f'{hp} hp left')


class Battle:
    def __init__(self, *heroes):
        self.heroes = list(heroes)
        self.is_running = False

    def pre_checks(self):
        if len(self.heroes) < 2:
            raise Exception('Not enough heroes')

    def running(self):
        self.pre_checks()

        self.is_running = True
        while self.is_running:
            random.shuffle(self.heroes)
            attacker = self.heroes[1]
            defender = self.heroes[0]
            attacker.hit(defender)
            if not defender.is_alive:
                self.heroes = self.heroes[1:]
            if len(self.heroes) == 1:
                self.is_running = False
                print(f'{self.heroes[0].name} won!')


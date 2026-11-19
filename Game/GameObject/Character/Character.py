from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.GameObject.UI.Inventory import Inventory
from Game.Action.Attack import Attack


class Character(GameObject):
    def __init__(self, name, hp: HP, level: Level, weapon: Weapon):
        self.name = name
        self.__hp = hp
        self.__level = level
        self.__weapon = weapon
        self.__inventory = Inventory()

    @property
    def hp(self) -> HP:
        return self.__hp

    @property
    def level(self) -> Level:
        return self.__level

    # TODO Weapon 없을떈?/...
    @property
    def weapon(self) -> Weapon:
        return self.__weapon

    @property
    def inventory(self) -> Inventory:
        return self.__inventory

    def attack(self, enemy: Monster) -> bool:
        if enemy == None:
            return False

        log_damage = Attack(self, enemy).execute()

from Game.GameObject.Character.Character import Character
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.Element import Element


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, HP(100), Level(), Weapon("화염검", 10, 0, Element.FIRE))

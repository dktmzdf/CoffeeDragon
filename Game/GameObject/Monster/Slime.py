from Game.GameObject.Monster.Monster import Monster
from Game.GameObject.Item.Weapon import Weapon
from Game.Attribute.HP import HP
from Game.Element import Element


class Slime(Monster):
    def __init__(self):
        super().__init__("슬라임", HP(30), Element.GRASS, 10, Weapon("물의 창", 15, 0, Element.WATER))

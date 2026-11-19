from Game.GameObject.Monster.Monster import Monster
from Game.GameObject.Item.Item import Item
from Game.Attribute.HP import HP
from Game.Element import Element


class Golem(Monster):
    def __init__(self):
        super().__init__("골렘", HP(80), Element.GRASS, 30, Item("강화석"))

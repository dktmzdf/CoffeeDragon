from Game.GameObject.Character.Monster.Monster import Monster
from Game.GameObject.Item.Item import Item
from Game.Attribute.HP import HP
from Game.Element import Element


class Golem(Monster):
    """골렘: 체력 120, 풀 속성, 경험치 90.

    처치하면 무기 강화 재료인 '강화석'을 드랍한다."""
    def __init__(self):
        """골렘 능력치 설정"""
        super().__init__("골렘", HP(120), Element.GRASS, 90, Item("강화석"))

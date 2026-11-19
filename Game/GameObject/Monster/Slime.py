from Game.GameObject.Monster.Monster import Monster
from Game.GameObject.Item.Weapon import Weapon
from Game.Attribute.HP import HP
from Game.Element import Element


class Slime(Monster):
    """슬라임: 체력 40, 풀 속성, 경험치 60.

    처치하면 '물의 창'(물 속성 무기)을 드랍한다."""
    def __init__(self):
        """슬라임 능력치 설정"""
        super().__init__(
            "슬라임", HP(40), Element.GRASS, 60, Weapon("물의 창", 60, 0, Element.WATER)
        )

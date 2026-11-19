from Game.GameObject.Character.Character import Character
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.Element import Element


class Warrior(Character):
    """전사 캐릭터 (Character IS-A).

    체력 100, 시작 무기는 '화염검'(공격력 30, 불 속성)."""

    def __init__(self, name):
        """전사 능력치와 시작 무기 설정"""
        super().__init__(name, HP(100), Level(), Weapon("화염검", 30, 0, Element.FIRE))

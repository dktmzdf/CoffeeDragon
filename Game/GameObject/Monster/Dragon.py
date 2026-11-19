from Game.GameObject.Monster.Monster import Monster
from Game.Attribute.HP import HP
from Game.Element import Element


class Dragon(Monster):
    """드래곤(보스): 체력 300, 불 속성, 경험치 500.

    보스라서 드랍 아이템이 없다. 불 속성이라 물 속성 무기에 2배 데미지를 받는다."""
    def __init__(self):
        # 보스: 드랍 없음
        """드래곤 능력치 설정"""
        super().__init__("드래곤", HP(300), Element.FIRE, 500)

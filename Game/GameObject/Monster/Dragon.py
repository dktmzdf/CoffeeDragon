from Game.GameObject.Monster.Monster import Monster
from Game.Attribute.HP import HP
from Game.Element import Element


class Dragon(Monster):
    def __init__(self):
        # 보스: 드랍 없음
        super().__init__("드래곤", HP(300), Element.FIRE, 100)

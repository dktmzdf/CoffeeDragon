from Game.GameObject.Monster import Monster
from Game.GameObject.Character import Character


# 나중에 Charater로 수정
class Attack:
    def __init__(self, causer: Character, target: Monster):
        self.causer = causer
        self.target = target

    @property
    def damage(self) -> int:
        base_dmg = self.causer.weapon.power
        weapon_element = self.causer.weapon.element

        # 최종 대미지 = 베이스(무기의 강화까지된) 대미지 * 속성 배율
        calc_damage = base_dmg * weapon_element.multiplier(self.target.element)
        return calc_damage

    def execute(self) -> int:
        dmg = self.damage
        self.target.hp.damage(self.damage)
        return dmg

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

    def execute(self) -> str:
        dmg = self.damage
        self.target.damage(self.causer, self.damage)

        return self.attack_log()

    def attack_log(self) -> str:
        weapon_element = self.causer.weapon.element.multiplier(self.target.element)
        out_log = f"{self.causer.name}의 {self.causer.weapon.name}[{self.causer.weapon.element.element_name}] 공격! {self.target.name}에게 {self.damage} 피해 (x{weapon_element})"
        return out_log

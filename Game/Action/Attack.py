from Game.GameObject.Character.Monster import Monster
from Game.GameObject.Character import Character


# 나중에 Charater로 수정
class Attack:
    """공격 한 번을 나타내는 클래스.

    공격자(causer)의 무기와 대상(target)의 속성으로 데미지를 계산한다.
    최종 데미지 = 무기 공격력(강화 포함) * 속성 배율.
    execute()로 대상에게 데미지를 주고 공격 로그를 반환한다."""
    def __init__(self, causer: Character, target: Monster):
        """공격자와 대상 설정"""
        self.causer = causer
        self.target = target

    @property
    def damage(self) -> int:
        """최종 데미지 계산"""
        base_dmg = self.causer.weapon.power
        weapon_element = self.causer.weapon.element

        # 최종 대미지 = 베이스(무기의 강화까지된) 대미지 * 속성 배율
        calc_damage = base_dmg * weapon_element.multiplier(self.target.element)
        return calc_damage

    def execute(self) -> str:
        """데미지 적용 후 로그 반환"""
        dmg = self.damage
        self.target.damage(self.causer, self.damage)

        return self.attack_log()

    def attack_log(self) -> str:
        """공격 로그 문자열"""
        weapon_element = self.causer.weapon.element.multiplier(self.target.element)
        out_log = f"{self.causer.name}의 {self.causer.weapon.name}[{self.causer.weapon.element.element_name}] 공격! {self.target.name}에게 {self.damage} 피해 (x{weapon_element})"
        return out_log

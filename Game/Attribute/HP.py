from Game.Attribute.Attribute import Attribute


class HP(Attribute):
    """체력 능력치 (Attribute IS-A).

    데미지를 받으면 줄어들고 0 이하로는 내려가지 않는다.
    처음 최대 체력(base_hp)을 기억해 두고, 레벨이 오르면
    최대 체력 = base_hp + (레벨 - 1) * 20 으로 늘어난다."""
    def __init__(self, max_HP):
        """최대 체력으로 가득 찬 상태로 생성"""
        super().__init__(max_HP, max_HP)
        self.base_hp = max_HP

    def damage(self, amount):
        """체력 감소"""
        self.change_current(-amount)

    def heal_hp(self, amount):
        """체력 회복"""
        self.change_current(amount)

    def is_alive(self) -> bool:
        """체력이 0보다 크면 True"""
        return self.get_current_value > 0

    def level_up_change_hp(self, level: int):
        """레벨에 맞게 최대 체력 갱신"""
        self.change_max_value(self.base_hp + (level - 1) * 20)

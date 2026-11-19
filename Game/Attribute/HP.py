from Game.Attribute.Attribute import Attribute


class HP(Attribute):
    def __init__(self, max_HP):
        super().__init__(max_HP, max_HP)
        self.base_hp = max_HP

    def damage(self, amount):
        self.change_current(-amount)

    def heal_hp(self, amount):
        self.change_current(amount)

    def is_alive(self) -> bool:
        return self.get_current_value > 0

    def level_up_change_hp(self, level: int):
        self.change_max_value(self.base_hp + (level - 1) * 20)

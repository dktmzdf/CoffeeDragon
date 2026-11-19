from Game.Attribute.Attribute import Attribute


class HP(Attribute):
    def __init__(self, max_HP):
        super().__init__(max_HP, max_HP)

    def damage(self, amount):
        self.change_current(-amount)

    def heal_hp(self, amount):
        self.change_current(amount)

    @property
    def is_alive(self) -> bool:
        return self.get_current_value > 0

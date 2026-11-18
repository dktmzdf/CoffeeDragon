import Attribute

class HP(Attribute):
    def __init__(self, max_HP):
        super().__init__(max_HP, max_HP)

    def damage(self, amount):
        change_current(-amount)

    def heal_hp(self, amount):
        change_current(amount)
        
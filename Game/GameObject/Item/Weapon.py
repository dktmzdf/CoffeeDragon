from Game.GameObject.Item.Item import Item
from Game.Element import Element


class Weapon(Item):
    def __init__(self, name, base_power: int, enhance: int, element: Element):
        super().__init__(name)
        self.__base_power = base_power
        self.__enhance = enhance
        self.__element = element

    @property
    def base_power(self) -> int:
        return self.__base_power

    @property
    def power(self) -> int:
        return self.__base_power + (5 *self.__enhance)

    @property
    def enhance(self) -> int:
        return self.__enhance

    @property
    def element(self) -> Element:
        return self.__element

    def upgrade(self):
        self.enhance += 1

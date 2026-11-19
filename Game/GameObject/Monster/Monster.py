from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.Element import Element
from Game.GameObject.Item.Item import Item


class Monster(GameObject):
    def __init__(self, name: str, hp: HP, element: Element, exp_reward: int, drop: Item | None = None):
        super().__init__(name)
        self.__hp = hp
        self.__element = element
        self.exp_reward = exp_reward
        self.__drop_item = []
        if drop is not None:
            self.__drop_item.append(drop)

    @property
    def hp(self) -> HP:
        return self.__hp

    @property
    def element(self) -> Element:
        return self.__element

    @property
    def drop_item(self) -> list[Item]:
        return self.__drop_item

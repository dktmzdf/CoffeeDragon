from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.Element import Element
from Game.GameObject.Item.Item import Item


class Monster(GameObject):
    def __init__(self, hp: HP, element: Element, drop: Item):
        self.__hp = hp
        self.__element = element
        self.__drop_item = []
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

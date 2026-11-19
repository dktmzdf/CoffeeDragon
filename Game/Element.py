from enum import Enum, auto


class Element(Enum):
    WATER = auto()
    FIRE = auto()
    GRASS = auto()

    @property
    def counter(self) -> "Element":
        """이기는 속성"""
        return _COUNTERS[self][0]

    @property
    def reverse_counter(self) -> "Element":
        """지는 속성"""
        return _COUNTERS[self][1]

    @property
    def element_name(self):

        return _NAME[self]

    def multiplier(self, element: Element) -> float:
        if self.counter == element:
            return 2.0
        elif self.reverse_counter == element:
            return 0.5

        return 1


# 상성표: Enum 밖에 둬야 멤버로 안 잡힘
_COUNTERS = {
    Element.WATER: (Element.FIRE, Element.GRASS),
    Element.FIRE: (Element.GRASS, Element.WATER),
    Element.GRASS: (Element.WATER, Element.FIRE),
}

_NAME = {
    Element.WATER: "물",
    Element.FIRE: "불",
    Element.GRASS: "풀",
}

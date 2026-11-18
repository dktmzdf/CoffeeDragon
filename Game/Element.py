from enum import Enum, auto


class Element(Enum):
    WATER = auto()
    FIRE = auto()
    GRASS = auto()

    @property
    def counter(self) -> "Element":
        """내가 이기는 속성"""
        return _COUNTERS[self][0]

    @property
    def reverse_counter(self) -> "Element":
        """나를 이기는 속성"""
        return _COUNTERS[self][1]


# 상성표: Enum 밖에 둬야 멤버로 안 잡힘
_COUNTERS = {
    Element.WATER: (Element.FIRE, Element.GRASS),
    Element.FIRE: (Element.GRASS, Element.WATER),
    Element.GRASS: (Element.WATER, Element.FIRE),
}

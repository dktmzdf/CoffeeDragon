from enum import Enum, auto


class Element(Enum):
    """속성(물/불/풀) Enum.

    상성은 물 > 불 > 풀 > 물 순환 구조다.
    이기는 속성을 공격하면 2.0배, 지는 속성을 공격하면 0.5배, 그 외는 1배 데미지.
    상성표(_COUNTERS)와 표시 이름(_NAME)은 Enum 멤버로 잡히지 않도록 클래스 밖에 둔다."""
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

        """화면 표시용 한글 이름"""
        return _NAME[self]

    def multiplier(self, element: Element) -> float:
        """상대 속성에 대한 데미지 배율"""
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

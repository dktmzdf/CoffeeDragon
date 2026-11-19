from Game.GameObject.Item.Item import Item
from Game.Element import Element


class Weapon(Item):
    """무기 아이템 (Item IS-A, Element HAS-A).

    기본 공격력, 강화 수치, 속성을 가진다.
    실제 공격력 = 기본 공격력 + 강화 수치 * 5.
    강화된 무기는 이름 앞에 "+N"이 붙는다 (예: "+1 물의 창")."""
    def __init__(self, name, base_power: int, enhance: int, element: Element):
        """기본 공격력, 강화 수치, 속성 설정"""
        super().__init__(name)
        self.__base_power = base_power
        self.__enhance = enhance
        self.__element = element

    @property
    def base_power(self) -> int:
        """강화 전 기본 공격력"""
        return self.__base_power

    @property
    def power(self) -> int:
        """강화가 반영된 공격력"""
        return self.__base_power + (5 * self.__enhance)

    @property
    def enhance(self) -> int:
        """강화 수치"""
        return self.__enhance

    @property
    def element(self) -> Element:
        """무기 속성"""
        return self.__element

    @property
    def name(self) -> str:
        """강화 수치가 붙은 이름"""
        out_name = (
            f"+{self.__enhance} {super().name}"
            if self.__enhance != 0
            else f"{super().name}"
        )

        return out_name

    def upgrade(self):
        """강화 +1"""
        self.__enhance += 1

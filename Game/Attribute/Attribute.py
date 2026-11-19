from abc import ABC


class Attribute(ABC):
    """최소값~최대값 범위를 갖는 능력치의 추상 부모 클래스.

    현재값은 change_current로만 바뀌며, 항상 [min, max] 범위로 고정(clamp)된다.
    HP 같은 수치형 능력치가 이 클래스를 상속해 공통 범위 처리를 재사용한다."""
    def __init__(
        self, max_value: float, current_value: float | None = None, min_value: float = 0
    ):
        """현재값 생략 시 최대값으로 시작"""
        self.__min_value = min_value
        self.__max_value = max_value
        self.__current_value = max_value if current_value is None else current_value

    @property
    def get_max_value(self):
        """최대값"""
        return self.__max_value

    @property
    def get_current_value(self):
        """현재값"""
        return self.__current_value

    @property
    def get_min_value(self):
        """최소값"""
        return self.__min_value

    def change_current(self, delta: float):
        """현재값을 delta만큼 변경 (범위 고정)"""
        self.__current_value = max(
            self.__min_value, min(self.__current_value + delta, self.__max_value)
        )

    def change_max_value(self, new_max_value: float):
        """최대값 변경"""
        self.__max_value = new_max_value

    def change_min_value(self, new_min_value: float):
        """최소값 변경"""
        self.__min_value = new_min_value

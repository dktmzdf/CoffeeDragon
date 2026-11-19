class Level:
    """캐릭터의 레벨과 경험치.

    레벨 1, 경험치 0에서 시작한다.
    현재 레벨 x 100 만큼 경험치가 모이면 레벨 업하고, 남은 경험치는 이월된다.
    한 번에 많은 경험치를 얻으면 여러 번 연속으로 레벨 업할 수 있다."""
    def __init__(self):
        """Lv.1, EXP 0으로 시작"""
        self.__level: int = 1
        self.__exp: int = 0

    @property
    def get_level(self):
        """현재 레벨"""
        return self.__level

    @property
    def level(self):
        """현재 레벨"""
        return self.__level

    @property
    def get_exp(self):
        """현재 경험치"""
        return self.__exp

    @property
    def exp(self):
        """현재 경험치"""
        return self.__exp

    @property
    def level_max_exp(self):
        """레벨 업에 필요한 경험치"""
        return self.__level * 100

    def gain(self, amount) -> bool:
        """
        레벨 업을 하면 True 아니면 False
        """
        self.__exp += amount

        # 레벨업함?
        is_level_up = self.level_max_exp <= self.__exp

        if is_level_up:
            # 무지막지한 경험치 먹었을때 예외처리
            while self.level_max_exp <= self.__exp:
                self.__level_up()

        return is_level_up

    def __level_up(self):
        """필요 경험치를 빼고 레벨 +1"""
        self.__exp -= self.level_max_exp
        self.__level += 1

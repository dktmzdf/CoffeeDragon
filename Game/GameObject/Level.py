class Level:
    def __init__(self):
        self.__level: int = 1
        self.__exp: int = 0

    @property
    def get_level(self):
        return self.__level

    @property
    def get_exp(self):
        return self.__exp

    @property
    def level_max_exp(self):
        return self.__level * self.__exp
    
    def gain(self, amount) -> bool:
        """
            레벨 업을 하면 True 아니면 False
        """
        self.__exp += amount

        #레벨업함?
        is_level_up = self.level_max_exp <= self.__exp

        if is_level_up:
            #무지막지한 경험치 먹었을때 예외처리
            while self.level_max_exp <= self.__exp:
                self.level_up()

        return is_level_up


    def __level_up(self):
        self.__level += 1
        self.__exp -= self.level_max_exp
        
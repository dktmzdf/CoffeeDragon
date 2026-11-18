class Attribute:
    def __init__(self, max_value: float, current_value: float | None = None, min_value: float = 0):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__current_value = max_value if current_value is None else current_value

    @property
    def get_max_value(self):
        return self.__max_value

    @property
    def get_current_value(self):
        return self.__current_value

    @property
    def get_min_value(self):
        return self.__min_value

    def change_current(self, delta: float):
        self.current_value = max(self.__min_value, min(self.__current_value + delta, self.__max_value))

    def change_max_value(self, new_max_value: float):
        self.__max_value = new_max_value

    def change_min_value(self, new_min_value: float):
        self.__min_value = new_min_value
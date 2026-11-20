from abc import abstractmethod

from Game.GameObject.Character.Character import Character


class Hero(Character):
    @abstractmethod
    def __init__(self, name, hp, level, weapon):
        """직업별 생성자에서 시작 능력치와 장비를 정한다."""
        super().__init__(name, hp, level, weapon)

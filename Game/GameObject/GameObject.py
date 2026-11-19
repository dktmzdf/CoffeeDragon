from abc import ABC


class GameObject(ABC):
    """게임에 등장하는 모든 객체(캐릭터, 몬스터)의 추상 부모 클래스.

    공통으로 이름(name)만 가진다."""
    def __init__(self, name):
        """이름 설정"""
        self.name = name

    def get_name(self):
        """이름 반환"""
        return self.name

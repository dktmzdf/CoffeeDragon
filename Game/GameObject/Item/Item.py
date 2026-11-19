from uuid import uuid4


class Item:
    """모든 아이템의 부모 클래스.

    이름과 고유 uuid를 가진다.
    uuid 덕분에 이름이 같은 아이템도 인벤토리에서 서로 다른 아이템으로 구분된다."""
    def __init__(self, name):
        """이름 설정, uuid 발급"""
        self.__name = name
        self.__item_uuid = uuid4()

    def get_item_uuid(self):
        """고유 uuid"""
        return self.__item_uuid

    @property
    def uuid(self):
        """고유 uuid"""
        return self.__item_uuid

    @property
    def name(self):
        """아이템 이름"""
        return self.__name

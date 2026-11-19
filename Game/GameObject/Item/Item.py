from uuid import uuid4


class Item:
    def __init__(self, name):
        self.__name = name
        self.__item_uuid = uuid4()

    def get_item_uuid(self):
        return self.__item_uuid

    @property
    def uuid(self):
        return self.__item_uuid

    @property
    def name(self):
        return self.__name

from uuid import uuid4

class Item:
    def __init__(self, name):
        self.name = name
        self.__item_uuid = uuid4()

    def get_item_uuid(self):
        return self.__item_uuid


    @property
    def get_name(self):
        return self.name

    @property
    def get_uuid(self):
        return self.uuid
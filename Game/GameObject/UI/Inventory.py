class Inventory:

    # 인벤토리 자체 최대 갯수
    INVENTORY_LIMIT = 1000

    def __init__(self):
        self.owner: "Character" = None
        self.inventory = {}

    def set_inventory_owner(self, owner: "Character"):
        self.owner = owner

    @property
    def capacity(self):
        return self.INVENTORY_LIMIT

    # 넣기
    # 빼기
    # 카운트
    # 제한
    @property
    def is_set_owner(self):
        return self.owner is not None

    @property
    def inventory_limit(self) -> bool:
        if len(self.inventory) >= self.INVENTORY_LIMIT:
            return True

        return False

    def add_item_inventory(self, item: "Item") -> bool:
        if self.is_set_owner == false:
            return False

        if self.inventory_limit:
            return False

        self.inventory[item.uuid] = item

        return True

    def remove_item_inventroy_for_name(self, name: str) -> bool:
        if self.is_set_owner == false:
            return False

        for key, value in self.inventory:
            if value.name == name:
                self.inventory.pop(key)
                return True

        return False

    def remove_item_inventroy(self, item: "Item") -> bool:
        if self.is_set_owner == false:
            return False

        self.inventory.pop(item.uuid)

        return True

    # TODO get_item_for_name으로 바꿀것
    def take(self, name: str) -> "Item":
        if self.is_set_owner == false:
            return False

        for key, value in self.inventory:
            if value.name == name:
                return value

        return None

    def items(self):
        return [key for key, value in self.inventory.items()]

    def add(self, item: "Item"):
        add_item_inventory(item)

    # 나중 구현
    def take__(self, item: "Item") -> "Item":
        raise NotImplementedError("take는 아직 구현 안 됨")

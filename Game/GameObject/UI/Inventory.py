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

    def add_item_inventory(self, item: "Item"):

        if self.is_set_owner == False:
            return

        if self.inventory_limit:
            return

        self.inventory[item.uuid] = item

        return f"'{item.name}' 흭득!"

    def remove_item_inventroy_for_name(self, name: str) -> bool:
        if self.is_set_owner == False:
            return False

        for key, value in self.inventory.items():
            if value.name == name:
                self.remove_item_inventroy(value)
                return True

        return False

    def remove_item_inventroy(self, item: "Item") -> bool:
        if self.is_set_owner == False:
            return False

        self.inventory.pop(item.uuid)

        return True

    def take(self, name: str) -> "Item":
        if self.is_set_owner == False:
            return False

        for key, value in self.inventory:
            if value.name == name:
                return value

        return None

    @property
    def items(self):
        return self.inventory.items()

    def add(self, item: "Item"):
        self.add_item_inventory(item)

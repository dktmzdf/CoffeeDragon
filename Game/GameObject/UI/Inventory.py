class Inventory:
    """캐릭터의 아이템 보관함.

    아이템을 uuid 키로 dict에 저장하므로 이름이 같은 아이템도 따로 보관된다.
    주인(owner)이 정해져야 넣기/빼기가 동작하고, 최대 INVENTORY_LIMIT개까지 담는다."""

    # 인벤토리 자체 최대 갯수
    INVENTORY_LIMIT = 1000

    def __init__(self):
        """빈 인벤토리 생성"""
        self.owner: "Character" = None
        self.inventory = {}

    def set_inventory_owner(self, owner: "Character"):
        """주인 캐릭터 설정"""
        self.owner = owner

    @property
    def capacity(self):
        """최대 보관 개수"""
        return self.INVENTORY_LIMIT

    # 넣기
    # 빼기
    # 카운트
    # 제한
    @property
    def is_set_owner(self):
        """주인이 정해졌으면 True"""
        return self.owner is not None

    @property
    def inventory_limit(self) -> bool:
        """가득 찼으면 True"""
        if len(self.inventory) >= self.INVENTORY_LIMIT:
            return True

        return False

    def add_item_inventory(self, item: "Item"):
        """아이템을 넣고 획득 로그 반환"""
        if self.is_set_owner == False:
            return

        if self.inventory_limit:
            return

        self.inventory[item.uuid] = item

        return f"'{item.name}' 흭득!"

    def remove_item_inventroy_for_name(self, name: str) -> bool:
        """이름으로 아이템 하나 제거"""
        if self.is_set_owner == False:
            return False

        for key, value in self.inventory.items():
            if value.name == name:
                self.remove_item_inventroy(value)
                return True

        return False

    def remove_item_inventroy(self, item: "Item") -> bool:
        """해당 아이템 제거"""
        if self.is_set_owner == False:
            return False

        self.inventory.pop(item.uuid)

        return True

    def take(self, name: str) -> "Item":
        """이름으로 아이템 찾기"""
        if self.is_set_owner == False:
            return False

        for key, value in self.inventory:
            if value.name == name:
                return value

        return None

    @property
    def items(self):
        """아이템 목록"""
        return self.inventory.items()

    def add(self, item: "Item"):
        """아이템 넣기"""
        self.add_item_inventory(item)

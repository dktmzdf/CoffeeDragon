from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.GameObject.UI.Inventory import Inventory
from Game.GameObject.Item import Item
from Game.Action.Attack import Attack
from Game.GameObject.Monster.Monster import Monster


class Character(GameObject):
    """플레이어 캐릭터의 부모 클래스 (GameObject IS-A).

    체력(HP), 레벨(Level), 장착 무기(Weapon), 인벤토리(Inventory)를 HAS-A로 가진다.
    몬스터 공격, 무기 교체, 강화석으로 무기 강화, 경험치 획득을 담당한다.
    레벨이 오르면 최대 체력도 함께 늘어난다."""
    def __init__(self, name, hp: HP, level: Level, weapon: Weapon):
        """체력, 레벨, 무기 설정 및 인벤토리 생성"""
        self.name = name
        self.__hp = hp
        self.__level = level
        if weapon is not None:
            self.__weapon = weapon
        self.__inventory = Inventory()
        self.__inventory.set_inventory_owner(self)

    @property
    def hp(self) -> HP:
        """체력"""
        return self.__hp

    @property
    def level(self) -> Level:
        """레벨"""
        return self.__level

    # TODO Weapon 없을떈?/...
    @property
    def weapon(self) -> Weapon:
        """장착 무기"""
        return self.__weapon

    @property
    def inventory(self) -> Inventory:
        """인벤토리"""
        return self.__inventory

    def attack(self, enemy: Monster | None) -> list[str] | bool:
        """적 공격 후 전투 로그 반환"""
        if enemy is None:
            return False
        if not enemy.hp.is_alive():
            return []

        out_logs = [Attack(self, enemy).execute()]
        monster_death_log = enemy.check_alive(self)
        if monster_death_log != []:
            for log in reversed(monster_death_log):
                out_logs.append(log)
        return out_logs

    def equip_new(self, item: Item):
        """현재 무기를 인벤토리에 넣고 새 무기 장착"""
        if self.__weapon is not None:
            # 벗고 넣고 장착
            unequipment_item = self.weapon
            self.__weapon = None
            self.inventory.add(unequipment_item)
            self.inventory.remove_item_inventroy(item)
            self.__weapon = item

        else:
            self.__weapon = item

    def equip(self, item_name: str):
        """이름으로 인벤토리 무기 장착"""
        if item_name == "":
            return False

        for key, value in self.inventory.items_new():
            if value.name == item_name:
                self.equip_new(value)
                return True

    def upgrade_weapon(self):
        """강화석을 써서 무기 강화"""
        if self.inventory.remove_item_inventroy_for_name("강화석"):
            self.weapon.upgrade()
            return True
        else:
            print("강화석이 없습니다.")
            return False

    def gain_exp(self, exp: int):
        """경험치 획득, 레벨 업 시 최대 체력 증가"""
        if self.level.gain(exp):
            self.hp.level_up_change_hp(self.level.get_level)

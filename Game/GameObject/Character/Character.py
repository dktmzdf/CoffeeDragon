from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.GameObject.UI.Inventory import Inventory
from Game.GameObject.Item import Item
from Game.Action.Attack import Attack
from Game.GameObject.Monster.Monster import Monster


class Character(GameObject):
    def __init__(self, name, hp: HP, level: Level, weapon: Weapon):
        self.name = name
        self.__hp = hp
        self.__level = level
        if weapon is not None:
            self.__weapon = weapon
        self.__inventory = Inventory()
        self.__inventory.set_inventory_owner(self)

    @property
    def hp(self) -> HP:
        return self.__hp

    @property
    def level(self) -> Level:
        return self.__level

    # TODO Weapon 없을떈?/...
    @property
    def weapon(self) -> Weapon:
        return self.__weapon

    @property
    def inventory(self) -> Inventory:
        return self.__inventory

    def attack(self, enemy: Monster | None) -> list[str] | bool:
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
        if item_name == "":
            return False

        for key, value in self.inventory.items_new():
            if value.name == item_name:
                self.equip_new(value)
                return True

    def upgrade_weapon(self):
        if self.inventory.remove_item_inventroy_for_name("강화석"):
            self.weapon.upgrade()
            return True
        else:
            print("강화석이 없습니다.")
            return False

    def gain_exp(self, exp: int):
        if self.level.gain(exp):
            self.hp.level_up_change_hp(self.level.get_level)

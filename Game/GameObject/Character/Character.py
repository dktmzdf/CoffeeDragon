from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.GameObject.Level import Level
from Game.GameObject.Item.Weapon import Weapon
from Game.GameObject.UI.Inventory import Inventory
from Game.GameObject.Item import Item
from Game.Action.Attack import Attack


class Character(GameObject):
    def __init__(self, name, hp: HP, level: Level, weapon: Weapon):
        self.name = name
        self.__hp = hp
        self.__level = level
        if weapon is not None:
            self.__weapon = weapon
        self.__inventory = Inventory()

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

    def attack(self, enemy: Monster) -> bool:
        if enemy is None:
            return False

        log_damage = Attack(self, enemy).execute()

    def equip(self, item: Item):
        if self.equip is not None:
            # 벗고 넣고 장착
            unequipment_item = self.weapon
            self.weapon = None
            self.inventory.add(unequipment_item)
            self.weapon = item

        else:
            self.weapon = item

    def upgrade_weapon(self):
        if self.inventory.remove_item_inventroy_for_name("강화석"):
            self.weapon.upgrade()
        else:
            print("강화석이 없습니다.")

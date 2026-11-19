from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.Element import Element
from Game.GameObject.Item.Item import Item


class Monster(GameObject):
    def __init__(
        self,
        name: str,
        hp: HP,
        element: Element,
        exp_reward: int,
        drop: Item | None = None,
    ):
        super().__init__(name)
        self.__hp = hp
        self.__element = element
        self.exp_reward = exp_reward
        self.__drop_item = []
        if drop is not None:
            self.__drop_item.append(drop)

    @property
    def hp(self) -> HP:
        return self.__hp

    @property
    def element(self) -> Element:
        return self.__element

    @property
    def drop_item(self) -> list[Item]:
        return self.__drop_item

    # 드랍하는건 Observer패턴으로 변경
    def damage(self, causer: "Character", damage: float):
        if self.hp.is_alive():
            self.hp.damage(damage)

    def check_alive(self, causer: "Character"):
        if self.hp.is_alive() == False:
            return self.death(causer)

        return ""

    def death(self, causer: "Character"):
        out_logs = []
        # 아이템 넣기
        for d in self.drop_item:
            out_logs.append(causer.inventory.add_item_inventory(d))
        causer.gain_exp(self.exp_reward)

        out_logs.append(f"{self.name} 처치! EXP +{self.exp_reward}")
        return out_logs

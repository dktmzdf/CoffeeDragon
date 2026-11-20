from Game.GameObject.GameObject import GameObject
from Game.Attribute.HP import HP
from Game.Element import Element
from Game.GameObject.Item.Item import Item
from Util.GameLog import GameLog


class Monster(Character):
    """몬스터의 부모 클래스 (Character IS-A).

    체력(HP), 속성(Element), 처치 시 주는 경험치, 드랍 아이템(Item HAS-A)을 가진다.
    체력이 0이 되면 death()에서 공격한 캐릭터에게 드랍 아이템과 경험치를 주고
    처치 로그를 GameLog에 기록한다."""

    def __init__(
        self,
        name: str,
        hp: HP,
        element: Element,
        exp_reward: int,
        drop: Item | None = None,
    ):
        """체력, 속성, 경험치, 드랍 아이템 설정"""
        super().__init__(name)
        self.__hp = hp
        self.__element = element
        self.exp_reward = exp_reward
        self.__drop_item = []
        if drop is not None:
            self.__drop_item.append(drop)

    @property
    def hp(self) -> HP:
        """체력"""
        return self.__hp

    @property
    def element(self) -> Element:
        """속성"""
        return self.__element

    @property
    def drop_item(self) -> list[Item]:
        """드랍 아이템 목록"""
        return self.__drop_item

    # 드랍하는건 Observer패턴으로 변경
    def damage(self, causer: "Character", damage: float):
        """살아 있으면 체력 감소"""
        if self.hp.is_alive():
            self.hp.damage(damage)

    def check_alive(self, causer: "Character"):
        """죽었으면 처치 처리"""
        if self.hp.is_alive() == False:
            self.death(causer)

    def death(self, causer: "Character"):
        """드랍 아이템, 경험치 지급 후 처치 로그 기록"""
        GameLog().add(f"{self.name} 처치! EXP +{self.exp_reward}")
        # 아이템 넣기
        for d in self.drop_item:
            if causer.inventory.add_item_inventory(d):
                GameLog().add(f"'{d.name}' 획득!")
        causer.gain_exp(self.exp_reward)

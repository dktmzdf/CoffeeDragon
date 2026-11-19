from Game.GameObject.Character.Character import Character
from Game.GameObject.Character.Monster.Monster import Monster
from Game.GameObject.Character.Monster.Slime import Slime
from Game.GameObject.Character.Monster.Golem import Golem
from Game.GameObject.Character.Monster.Dragon import Dragon
from Util.GameLog import GameLog


class GameLoop:
    """턴제 게임 루프.

    단계별로 몬스터가 한 마리씩 등장하고, 플레이어와 몬스터가 번갈아 행동한다.
    매 턴 플레이어가 행동(공격, 무기 교체, 강화, 상태 보기)을 고르고,
    몬스터가 살아 있으면 반격한다.
    몬스터를 잡으면 다음 단계로, 캐릭터가 쓰러지면 게임 오버.
    모든 단계를 깨면 클리어."""

    def __init__(self, hero: Character):
        """캐릭터와 단계별 몬스터 설정"""
        self.hero = hero
        # TODO 4단계 전투: 단계/몬스터 구성과 밸런스 정하기
        self.stages: list[Monster] = [Slime(), Golem(), Dragon()]

    def run(self):
        """모든 단계를 순서대로 진행"""
        for stage, monster in enumerate(self.stages, 1):
            GameLog().add(f"===== {stage}단계: {monster.name} 등장! =====")
            if not self.battle(monster):
                GameLog().add("게임 오버...")
                GameLog().flush()
                return
        GameLog().add("모든 단계 클리어!")
        GameLog().flush()

    def battle(self, monster: Monster) -> bool:
        """한 몬스터와 전투. 이기면 True, 지면 False"""
        turn = 1
        while monster.hp.is_alive():
            GameLog().add(f"--- {turn}턴 ---")
            if not self.player_turn(monster):
                continue  # 턴을 소모하지 않는 행동
            if monster.hp.is_alive():
                self.monster_turn(monster)
            if not self.hero.hp.is_alive():
                return False
            turn += 1
        return True

    def player_turn(self, monster: Monster) -> bool:
        """플레이어 행동. 턴을 소모하면 True"""
        choice = self.game_input("1.공격 2.무기 교체 3.강화 4.상태 > ")
        if choice == "1":
            self.hero.attack(monster)
            return True
        if choice == "2":
            # TODO 무기 교체/강화가 턴을 소모할지 정하기
            for item in self.hero.inventory.items:
                GameLog().add(item.name)
            self.hero.equip(self.game_input("장착할 무기 이름 > "))
            return False
        if choice == "3":
            self.hero.upgrade_weapon()
            return False
        if choice == "4":
            self.show_status(monster)
            return False
        GameLog().add("잘못된 입력")
        return False

    def monster_turn(self, monster: Monster):
        """몬스터 반격"""
        # TODO 몬스터 공격력, 반격 데미지 계산, 로그 출력
        pass

    def show_status(self, monster: Monster):
        """캐릭터와 몬스터 상태 출력"""
        hero = self.hero
        GameLog().add(
            f"{hero.name} Lv.{hero.level.level} HP {hero.hp.get_current_value}/{hero.hp.get_max_value} "
            f"무기 {hero.weapon.name}[{hero.weapon.element.element_name}] 공격력 {hero.weapon.power}"
        )
        GameLog().add(f"인벤토리 {[i.name for i in hero.inventory.items]}")
        GameLog().add(
            f"{monster.name} HP {monster.hp.get_current_value}/{monster.hp.get_max_value}"
        )

    def game_input(self, msg: str):
        GameLog().flush()
        return input(msg).strip()

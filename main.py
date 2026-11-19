from Game.GameObject.Character.Hero.Warrior import Warrior
from Game.GameObject.Character.Monster.Slime import Slime
from Game.GameObject.Character.Monster.Golem import Golem
from Game.GameObject.Character.Monster.Dragon import Dragon
from Game.GameLoop import GameLoop


def report():
    """과제 시나리오 실행: 슬라임 -> 골렘 -> 무기 교체/강화 -> 보스전"""
    


def main():
    """진입점"""
    GameLoop(Warrior("아서")).run()


if __name__ == "__main__":
    main()

from Game.GameObject.Character.Warrior import Warrior
from Game.GameObject.Monster.Slime import Slime
from Game.GameObject.Monster.Golem import Golem
from Game.GameObject.Monster.Dragon import Dragon


def report():
    hero = Warrior("아서")

    # 1) 슬라임 사냥
    for line in hero.attack(Slime()):
        print(line)
    print([i.name for i in hero.inventory.items])
    print("---")

    # 2) 골렘 사냥 (쓰러질 때까지 공격)
    golem = Golem()
    while golem.hp.is_alive():
        for line in hero.attack(golem):
            print(line)
    print("---")

    # 3) 보스전 준비: 무기 교체 + 강화
    print(
        hero.equip("물의 창"), hero.weapon.name, [i.name for i in hero.inventory.items]
    )
    print(hero.upgrade_weapon(), hero.weapon.name, hero.weapon.power)
    print("---")

    # 4) 보스전
    boss = Dragon()
    turn = 0
    while boss.hp.is_alive():
        turn += 1
        hero.attack(boss)
    print(f"{turn}턴 만에 보스 처치! Lv.{hero.level.level}, EXP {hero.level.exp}")


def main():
    report()


if __name__ == "__main__":
    main()

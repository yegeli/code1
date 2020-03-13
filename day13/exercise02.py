"""
    手雷爆炸了,伤害玩家生命(血量减少,闪现红屏),伤害敌人生命(血量减少,头顶爆字)
    要求：
        可能还增加其他事物，但是不能修改手雷代码.
            房子、鸭子...

    体会：
        封装：分
        继承：隔
        多态：做
"""


class Granade:
    """
        手雷
    """

    def explode(self, target):
        # 调用的是攻击目标
        # 传入的是一种攻击目标
        if isinstance(target, AttackTarget):
            target.damage()


class AttackTarget:
    """
        攻击目标
    """

    def damage(self):
        pass


# ----------------------------------
class Player(AttackTarget):

    def damage(self):
        return 1


class Enemy(AttackTarget):

    def damage(self):
        return 2

g01 = Granade()
p01 = Player()
e01 = Enemy()
print(g01.explode(e01))

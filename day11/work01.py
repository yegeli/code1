"""
3. 面向对象
     1)创建技能类(技能名称,攻击比率,消耗法力,持续时间)
                         0 - 2  0 - 80  0 - 120
       保证数据范围
     2)将工资计算器v2,改写为面向对象版本.
       体会面向过程与面向对象的区别
"""
class Skill:
    name = "dsafa"
    def __init__(self, name=''):
        self.name = name
        Skill.name = 'yege'
        print(Skill.name)

td = Skill()

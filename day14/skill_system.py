"""

    技能系统

        封装：创建了DamageEffect、DizzinessEffect、LowerDeffenseEffect、SkillDeployer
        继承：创建了SkillImpactEffect
             隔离了SkillDeployer与具体技能影响的变化
        多态：SkillDeployer调用SkillImpactEffect的impact方法
             DamageEffect、DizzinessEffect、LowerDeffenseEffect重写SkillImpactEffect的impact方法
             添加到SkillDeployer的都是重写后的impact

        开闭原则：增加其他技能,只需要创建新类,SkillDeployer无需改变。
        单一职责：
            SkillDeployer：技能释放器
            DamageEffect：扣血技能
            DizzinessEffect：眩晕技能
            LowerDeffenseEffect：降低技能
        依赖倒置：SkillDeployer 调用 SkillImpactEffect,没有调用具体技能效果类
        组合复用：SkillDeployer 通过组合关系调用 技能效果
        何处使用继承？何处使用组合？
            继承：SkillImpactEffect 统一 DamageEffect、DizzinessEffect、LowerDeffenseEffect
            组合：SkillDeployer 连接 技能效果
"""

class SkillImpactEffect:
    def impact(self):
        pass


class DamageEffect(SkillImpactEffect):
    def __init__(self, value=0):
        self.value = value

    def impact(self):
        print("扣你",self.value,"血量")


class DizzinessEffect(SkillImpactEffect):
    def __init__(self, duration=0):
        self.duration = duration

    def impact(self):
        print("眩晕", self.duration, "秒")


class LowerDeffenseEffect(SkillImpactEffect):
    def __init__(self, value=0,duration=0):
        self.duration = duration
        self.value = value

    def impact(self):
        super().impact()
        print("降低", self.duration, "防御力","持续", self.value, "秒")



class SkillDeployer:
    def __init__(self, name=""):
        self.name = name
        self.__config_file = {
            "降龙十八掌":["DizzinessEffect(15)","DamageEffect(500)"],
            "六脉神剑":["LowerDeffenseEffect(100,10)","DamageEffect(500)"]
        }
        effect_names = self.__config_file[self.name]
        # "DizzinessEffect(15)"  ----->DizzinessEffect(15)
        self.__effect_objects=[eval(item) for item in effect_names]
        # self.__effect_objects = []
        # for item in effect_names:
        #     self.__effect_objects.append(eval(item))

    def deploy(self):
        print(self.name,"打死你")
        for item in self.__effect_objects:
            item.impact()




xlsbz = SkillDeployer("降龙十八掌")
xlsbz.deploy()
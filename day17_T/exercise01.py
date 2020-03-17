"""
    解题步骤：
        1.根据需求写出函数
        2.将变化与稳定的代码单独定义在函数中
        3.定义参数隔离变化
        4.将稳定与变化的函数组合在一起实现需求
"""

class Wife:
    def __init__(self, name="", height=0, weight=0, face_core=0, money=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.face_score = face_core
        self.money = money
    def __str__(self):
        return "%s---%d---%d---%d---%d" %(self.name,self.height,self.weight,self.face_score,self.money)



list_wifes = [
    Wife("双儿",171,100,96,6000),
    Wife("小郡主",162,90,86,20000),
    Wife("方怡",151,95,88,30000),
    Wife("凤姐",150,188,30,500),
    Wife("沐剑屏",163,80,90,10000),
    Wife("阿珂",164,161,100,6000),
    Wife("建宁",176,100,93,3000),
]

# 练习1：
#     需求1：在老婆列表中查找高度大于170的所有老婆
#     需求2：在老婆列表中查找颜值小于90的所有老婆

# 1.需求函数
# def find_height():
#     for i in list_wifes:
#         if i.height >170:
#             yield i
#
# def find_face():
#     for i in list_wifes:
#         if i.face_score < 90:
#             yield i

# 2.封装 ：分---->将变化与稳定的代码单独定义在函数中，变化函数
def find_h(i):
    return  i.height >170

def find_f(i):
    return i.face_score < 90

# 3.继承 ：隔---->通过参数隔离它们的变化，形参（抽象）
def find(target):
    for i in list_wifes:
        if target(i):
            yield i

# 4.多态 ：
for item in find(find_h):
    print(item)

for item in find(find_f):
    print(item)
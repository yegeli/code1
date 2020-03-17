"""
    内置高阶函数
"""



class Wife:
    total_money = 1000
    def __init__(self, name="", height=0, weight=0, face_score=0, money=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.face_score = face_score
        self.money = money


list_wifes = [
    Wife("双儿", 171, 100, 96, 6000),
    Wife("小郡主", 162, 90, 86, 20000),
    Wife("建宁", 168, 95, 95, 30000),
    Wife("方怡", 173, 108, 96, 5000),
    Wife("凤姐", 150, 180, 30, 10000),
    Wife("沐剑屏", 161, 100, 90, 6000),
    Wife("阿珂", 181, 88, 100, 6000),
]

# 1.
# 过滤: 查找满足条件的元素
filter()

# 2.
#
map()
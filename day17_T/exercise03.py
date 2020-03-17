


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

for i in map(lambda w:(w.name,w.height,w.weight,w.face_score,w.money),list_wifes):
    print(i)

for i in filter(lambda w:w.money<10000,list_wifes):
    print(i.__dict__)

for i in map(lambda w:(w.name,w.height),filter(lambda w:w.height>160,list_wifes)):
    print(i)

print(dict(map(lambda w: (w.name, w.money), list_wifes)))

t = dict(map(lambda w: (w.name, w.money), list_wifes))
for i in sorted(list_wifes,key=lambda w:t[w.name],reverse=True):
    print(i.__dict__)
print("------------")
print(t.items())
print(dict(sorted(t.items(),key=lambda w:w[1],reverse=True)))

list01 = [(1,2),(1,2,3),(1,2,3,4)]
print(min(list01,key=lambda item:len(item)))
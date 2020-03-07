# 1、
class Things:

    def __init__(self, book,desk):
        self.book = book
        self.desk = desk

    def talk_things(self):
        print(self.desk+"上面有"+self.book+"书籍")

td = Things("《python从入门到项目实战》","电脑桌")
td.talk_things()

# 2、    2) 创建狗类
#             实例变量：品种、爱称、年龄、体重
#             实例方法：吃、叫
#        实例化两个对象、调用其方法.

class Dog:

    def __init__(self,kind,named,age,height):
        self.kind = kind
        self.name = named
        self.age = age
        self.height = height

    def eat(self):
        print("种类：%s\t 爱称：%s\t 年龄：%s\t岁 体重：%sKG,喜欢啃骨头。" % (self.kind,self.name,self.age,self.height))

    def call(self):
        print("汪汪")

dog = Dog('獒','小花','5','20')
dd = Dog('宠物狗','小m','3','10')
dog.eat()
dog.call()
dd.eat()
dd.call()

#    定义函数,删除列表中相同元素(只保留一个)
#     list01 = [6,54,65,677,6,65,6,65]


def same_element(list01):


    for i in range(len(list01)-1,0,-1):
        for c in range(i-1,-1,-1):
            if list01[i] == list01[c]:
                del list01[i]
                list01.append(0)
    for i in range(len(list01)-1,-1,-1):
        if list01[i] == 0:
            del list01[i]
list01 = [6,54,65,677,6,65,6,65]
same_element(list01)
print(list01)

"""
        创建MyRange类，实现下列效果
        mr = My_Range(5)
        for number in mr(5):
        print(number)

"""


class My_Range:
    def __init__(self, num=0):
        self.__num = num
        self.__index = -1
    def __iter__(self):
        while self.__index < self.__num -1:
            self.__index += 1
            yield self.__index




mr = My_Range(5)
iterator = mr.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

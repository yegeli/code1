"""
        创建MyRange类，实现下列效果
        mr = My_Range(5)
        for number in mr(5):
        print(number)

"""


class My_Range:
    def __init__(self, num=0):
        self.__num = num

    def __iter__(self):
        return T(self.__num)


class T:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= self.__data -1:
            raise StopIteration()
        self.__index += 1
        return self.__index


mr = My_Range(999)
iterator = mr.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

"""
    让图形管理器可以直接参与for循环
"""
# 略

# class GraphicManager:
#     def __init__(self):
#         self.__list_graphics = []
#
#     def add_graphics(self, graphic):
#         self.__list_graphics.append(graphic)
#
#
# manager = GraphicManager()
# manager.add_graphics("圆形")
# manager.add_graphics("方形")
# manager.add_graphics("三角形")
# for item in manager:
#     print(item)

class GraphicManager:
    def __init__(self):
        self.__list_graphics = []

    def add_graphics(self, graphic):
        self.__list_graphics.append(graphic)

    def __iter__(self):
        return Myiterator(self.__list_graphics)

class Myiterator:
    def __init__(self, data):
        self.data = data
        self.index = -1
    def __next__(self):
        try:
            self.index += 1
            return self.data[self.index]
        except IndexError:
            raise StopIteration

manager = GraphicManager()
manager.add_graphics("圆形")
manager.add_graphics("三角形")
manager.add_graphics("正方形")

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

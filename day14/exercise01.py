"""
    定义图形管理器
        记录所有图形
        计算图形总面积

    图形：
        圆形 3.14 × 半径的平方
        矩形 长*宽

"""


class GraphicManager:
    """
    图形管理器
    """
    def __init__(self):
        """
        存储图形管理器列表
        """
        self.__list_graphics = []

    def add_graphics(self, graphic):
        """
        添加图形
        :param graphic: 通过变量进行组合服用
        """
        self.__list_graphics.append(graphic)

    def calculate_total_area(self):
        sum_value = 0
        for item in self.__list_graphics:
            # 编码时：调用父
            # 运行时：执行子。
            #item[Circle(10),Rectanle(10, 20)]
            sum_value += item.get_area()
        return sum_value


class Graphic:
    """
        约束所有图形,在计算面积的功能上达到统一.
    """

    def get_area(self):
        pass


# -----------------------------------

class Circle(Graphic):
    """
    圆形
    """
    def __init__(self, r):
        self.r = r

    def get_area(self):

        return 3.14 * self.r ** 2


class Rectanle(Graphic):
    """
    矩形
    """
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w


# ----------------------------
# 测试
manager = GraphicManager()
manager.add_graphics(Circle(10))
manager.add_graphics(Rectanle(10, 20))
print(manager.calculate_total_area())

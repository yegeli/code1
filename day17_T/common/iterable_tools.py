"""
    可迭代对象的工具模块
"""
class IterableHelper:

    # 做成函数都可以正常工作,如果封装到类中,就是用静态方法.
    @staticmethod
    def find(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable,func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable,func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count


    @staticmethod
    def select(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        for item in iterable:
            yield func_condition(item)

    #       需求1：在老婆列表中查找颜值最高的老婆
    #       需求2：在老婆列表中查找财产最大的老婆


    #       需求1：根据身高对老婆列表进行升序排列
    #       需求2：根据体重对老婆列表进行升序排列

    @staticmethod
    def get_sort(iterable,handle):
        for i in range(len(iterable)-1):
            for c in range(i+1,len(iterable)):
                # if iterable[i].height > iterable[c].height:
                # if iterable[i].weight > iterable[c].weight:
                if handle(iterable[i]) > handle(iterable[c]):
                    iterable[i],iterable[c] = iterable[c],iterable[i]
        # return iterable

    #       需求1： 累加老婆们的体重
    #       需求2： 累加老婆们的财产


    @staticmethod
    def add(iterable,handle):
        sum = 0
        for i in range(len(iterable)):
            sum += handle(iterable[i])
        return sum

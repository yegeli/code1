"""
    lambda 表达式
        匿名方法
"""
# 1.有参数有返回值
# def func01(p1,p2):
#     return p1 + p2
#
# print(func01(1, 2))

func01 = lambda p1, p2: p1 + p2
print(func01(1,2))

# 2.无参数有返回值
# 1.有参数有返回值
# def func01():
#     return 1000
#
# print(func01())

func01 = lambda : 1000
print(func01())

# 3.有参数无返回值
# def func01((p1,p2)):
#     print (p1,p2)
#
# print(func01(p1,p2))

# func01 = lambda p1,p2:print(p1+p2)
# print(func01 (p1,p2))


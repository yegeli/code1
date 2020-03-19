
"""
 # 新功能：打印函数执行时间
# 执行前记录时间
# 执行后用当前时间 - 执行前时间
"""
# 旧功能
import time
def print_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()#新功能逻辑
        result = func(*args, **kwargs) #旧功能逻辑
        stop = time.time()
        print("函数执行了%f秒"%(stop - start))
        return result
    return wrapper

@print_time
# x = print_time(func01)
def func01(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value
@print_time
def func02(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value

print(func01(10))
print(func02(100000))

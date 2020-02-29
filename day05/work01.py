"""

3. 在终端中获取一个整数,作为边长,打印矩形.
    例如:5
    *****
    *   *
    *   *
    *   *
    *****
"""

length = int(input("输入边长："))
print("*" * length)
for i in range(length - 2):
    print("*" + ' ' * (length - 2) + '*')
print("*" * length)

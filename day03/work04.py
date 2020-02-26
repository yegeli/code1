"""

魏老师很不幸买了一箱有虫子(1)的苹果
   虫子吃完一个苹果再吃另外一个苹果
   在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
   请打印没有被虫子吃过的苹果数量（最小也是0）
"""

number = int(input("输入苹果数量："))
time = float(input("输入时长："))
speed = float(input("输入速度："))

count = number-time * speed
print("没有被吃过的苹果数：" + str(round(count)))
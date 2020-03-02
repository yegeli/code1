"""
5. 双色球彩票
    红球:6个,1--33之间,不能重复
    蓝球:1个,1--16之间
    (1)创建随机彩票（一个列表,前六个是红球,最后一个蓝球）
    (2)在终端中购买彩票(提示:号码已经存在,号码超过范围)
    (3)自由发挥
"""
# import random
#
# list_balls = []
# while len(list_balls) < 6:
#     red_balls = random.randint(1, 33)
#     if red_balls not in list_balls:
#         list_balls.append(red_balls)
# blue_balls = random.randint(1, 16)
# print(list_balls)
# list_balls.append(blue_balls)
#
list_balls = []

while len(list_balls) < 6:
    ticket_red_number = int(input("输入第%d个红球数字号码：" % (len(list_balls)+1)))
    if ticket_red_number in list_balls:
        print("号码已存在")
    elif ticket_red_number > 33:
        print("号码超出范围")
    else:
        list_balls.append(ticket_red_number)

while len(list_balls) < 7:
    ticket_blue_number = int(input("输入您要买的蓝球号码："))
    if ticket_blue_number > 16:
        print("号码超出范围")
    elif not ticket_blue_number:
        print("号码不能为空")
    else:
        list_balls.append(ticket_blue_number)

for i in range(0, len(list_balls) - 1):
    print("您选的第%d个红色球：%s" % (i + 1, list_balls[i]))
print("您选的最后一个蓝色球：%s" % (list_balls[-1]))

'''
5. 随机加法考试题
    随机产生２个数字(1-10之间)
    在终端中获取这两个数字的和(请输入2+8=?)
    总共5道题,答对加10分,答错减5分
    最后打印总分
'''

import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
sum = number1 + number2
score, count = 0, 0

while count <= 5:
    in_sum = int(input("输入两个数的答案： "))
    if in_sum < sum:
        score -= 5
        print("输小啦")
    elif in_sum > sum:
        score -= 5
        print("输大啦")
    else:
        score += 10
        print("输对啦")
        break
print("您最后的得分是：%d" % score)

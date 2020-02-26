"""
5. 已知(在终端中录入)：位移、时间、初速度
   计算：加速度
   匀变速直线运动的速度与位移公式：
        位移 =  初速度 × 时间 + 0.5 * 加速度 * 时间的平方
"""

distance = float(input("输入位移："))
use_time = float(input("输入时间："))
init_speed = float(input("输入速度："))

accelerated = (distance - init_speed * use_time) / 0.5 * use_time ** 2

print("加速度为：" + str(round(accelerated,2)))
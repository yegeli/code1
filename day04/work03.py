
'''
6. 一个小球从100m的高度落下,每次都弹回原高度一半
    (1)计算弹起多少次,最终落地.(最小弹起高度0.01m)
    (2)全过程经历多少米
    数据
    算法

'''


height = 100
count = 0
distance = 0
while True:
    height //= 2
    distance += height * 1.5
    count += 1
    if height < 0.01:
        break
print(count)
print(distance)

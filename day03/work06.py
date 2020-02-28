"""
10. 一张纸的厚度是0.01毫米
     请计算，对折多少次超过珠穆朗玛峰(8844.43米).
"""

height = 1e-05
count = 0
while height <= 8844.43 :
    height = height *2
    count += 1
print("需要对折：" +str(count) +"次")

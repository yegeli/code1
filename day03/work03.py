"""
7. 在终端中获取一个月份，年份，打印相应的天数.
   1 3 5 7 8 10 12 --> 31天
   2 --> 28(平年)  29(闰年)
   4  6  9  11 --> 30天
"""

month = int(input("输入月份："))
year = int(input("输入年份："))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("该月份有31天")
elif month == 2:
    if year % 400 ==0 or year % 4 ==0 and year % 400 :
        print(str(year)+ "年是闰年，2月份有29天")
    else:
        print(str(year)+ "年是平年，2月份有28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("该月有30天")

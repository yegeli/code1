"""
在终端中录入一个秒数，计算是几小时零几分钟零几秒钟.

"""
second = int(input("输入一个秒数："))

get_hour = second // 3600
get_minute = second // 60 % 60
get_second = second % 60

print(str(get_hour) + "小时" + str(get_minute) + "分钟" + str(get_second) + "秒")

"""
3. 在终端中录入多个人的多个喜好
   例如：qtx:看书、编码、旅游
        lzmly:刷抖音、看电影
        有基础的王鹏鹏:起哄、学习、打豆豆
        打印所有人，所有喜好
"""
dict_hobby ={}
while True:
    name = input("录入姓名")
    if not name:
        break
    hobby = input("录入爱好")
    list_hobby = []
    while hobby:
        list_hobby.append(hobby)
        hobby = input("录入爱好")
    dict_hobby[name] = list_hobby

for name,hobbys in dict_hobby.items():
    print("姓名：%s \t 爱好：%s" %(name,'、'.join(hobbys)))
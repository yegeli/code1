"""
 定义数据结构,存储多个城市的景区与美食
    "北京":
        "景区":"长城","故宫"
        "美食":"烤鸭","豆汁胶圈","炸酱面"
    "四川":
        "景区":"九寨沟","峨眉山"
        "美食":"火锅","兔头"

    1)打印所有城市（一行一个）
    2)打印北京所有美食（一行一个）
    3)打印四川所有景区（一行一个）
    4)打印所有城市的所有景区（一行一个）
    5)为北京添加景区："天坛"
    6)删除四川美食：兔头

"""

dict = { "北京":{"景区":["长城","故宫"],"美食":["烤鸭","豆汁胶圈","炸酱面"]},
         "四川":{"景区":["九寨沟","峨眉山"],"美食":["火锅","兔头"]}}

# for city in dict.keys():
#     print(city)

# for beijing_foods in dict['北京']['美食']:
#       print(beijing_foods)

# for sichuan_scenery in dict['四川']['景区']:
#       print(sichuan_scenery)

# for i in dict.values():
#     for y in i['景区']:
#         print(y)
# dict['北京']['景区'].append("天坛")
# print(dict)

dict['四川']['美食'].remove("兔头")
print(dict)

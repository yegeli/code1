
"""
5. dict01 = {"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
   在字典中找出金条数量最多的人名

"""
dict01 = {"金海":3200,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}



for key in dict01:
    if dict01[key] == max(dict01.values()):
        print(key)
# max ="金海"
# for key in dict01:
#     if dict01[key] > dict01[max]:
#         max = key
# print(max)

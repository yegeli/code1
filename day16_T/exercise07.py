class EpidemicInformationModel:
    """
   疫情信息模型
   """

    def __init__(self, region="", confirmed=0, dead=0, cure=0, eid=0):
        self.region = region
        self.confirmed = confirmed
        self.dead = dead
        self.cure = cure
        self.eid = eid

    def __str__(self):
        return "%s--%d--%d--%d--%d" % (self.region, self.confirmed, self.dead, self.cure, self.eid)



list_epidemics =[
    EpidemicInformationModel("上海", 400, 16, 310, 102),
    EpidemicInformationModel("河南", 1200, 50, 800, 103),
    EpidemicInformationModel("湖北", 60000, 3000, 40000, 104),
    EpidemicInformationModel("西藏", 1, 0, 1, 105),
]

        # 练习1: 定义函数,查找确诊人数大于500的疫情信息
        # 练习2: 定义函数,查找上海的疫情信息

# def find_number():
#     for item in list_epidemics:
#         if item.confirmed < 500:
#             yield item
t = (item for item in list_epidemics if item.confirmed < 500)

for item in t:
    print(item)




#
# def find_number():
#     for item in list_epidemics:
#         if item.confirmed < 500 and item.dead ==0:
#             yield item.region
# t =(item.region for item in list_epidemics if item.confirmed < 500 and item.dead ==0)
#
# for item in t:
#     print(item)


# def find_number():
#     for item in list_epidemics:
#         yield (item.region,item.dead)
# t =((item.region,item.dead) for item in list_epidemics)
#
# for item in t:
#     print(item)

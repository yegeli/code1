"""
    # 商品列表 商品编号 商品名称 商品单价
    dict_commodity_infos = {
        1001: {"name": "屠龙刀", "price": 10000},
        1002: {"name": "倚天剑", "price": 10000},
        1003: {"name": "金箍棒", "price": 52100},
        1004: {"name": "口罩", "price": 20},
        1005: {"name": "酒精", "price": 30},
    }
    # 订单列表  商品编号 数量
    list_orders = [
        {"cid": 1001, "count": 1},
        {"cid": 1002, "count": 2},
    ]
    # 1. 打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.

    # 2. 打印所有订单信息,格式：订单编号xx,数量:xx.

    # 3. 打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.

    # 4. 计算订单总价格：累加商品单价 * 数量

    # 5. 查找数量最少的订单(使用自定义算法,不使用内置函数)

    # 6. 根据单价,升序排列商品信息(使用自定义算法,不使用内置函数)

"""

dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]
# # 1. 打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
for key,value in dict_commodity_infos.items():
    print("商品编号%s,商品名称%s,商品单价%d."%(key,value["name"],value["price"]))

# # 2. 打印所有订单信息,格式：订单编号xx,数量:xx.
for dict_list_order in list_orders:
    print("订单编号%s,数量:%d." % (dict_list_order['cid'],dict_list_order['count']))

# 3. 打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.

for dict_list_order in list_orders:
    print("商品名称:%s,商品单价:%d,数量%d." %(dict_commodity_infos[dict_list_order['cid']]['name'],dict_commodity_infos[dict_list_order['cid']]['price'],dict_list_order['count']))

# 4. 计算订单总价格：累加商品单价 * 数量
sum =0
for dict_list_order in list_orders:
    price = dict_list_order['count'] * dict_commodity_infos[dict_list_order['cid']]['price']
    sum += price
print("订单总价%d" %sum)

# 5. 查找数量最少的订单(使用自定义算法,不使用内置函数)
min = list_orders[0]
for r in range(1,len(list_orders)-1):
    for c in range(r+1):
        if list_orders[r]['count'] > list_orders[c]['count']:
            min =list_orders[c]
print(min['cid'])

#6. 根据单价,升序排列商品信息(使用自定义算法,不使用内置函数)
list_commodity_infos = list(dict_commodity_infos.items())
for r in range(len(list_commodity_infos)-1):
    for c in range(r+1,len(list_commodity_infos)):
       if list_commodity_infos[r][1]['price'] > list_commodity_infos[c][1]['price']:
           list_commodity_infos[r],list_commodity_infos[c] = list_commodity_infos[c],list_commodity_infos[r]
print(dict(list_commodity_infos))






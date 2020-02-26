"""
9. 商品优惠
    打折策略：如果vip客户，消费小于500,享受85折
                        否则享受8折
            否则，消费大于800,享受9折
                 否则原价
    根据账户类型和消费金额，计算折扣.
"""

type = input("账户类型：")
money = float(input("输入消费金额："))
if type == 'vip':
    if money < 500:
        print("85折")
    else:
        print("8折")
else:
    if money > 800:
        print("9折")
    else:
        print("原价")

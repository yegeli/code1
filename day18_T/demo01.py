"""
    Enclosing 外部嵌套作用域：函数嵌套

"""

def give_gife_money(money):
    print("得到了",money,"元压岁钱")

    def child_buy(target,price):
        # 函数嵌套
        nonlocal money
        money -=price
        print("孩子购买了:",target,"---->",price,"元","还剩下:",money,"元")

    return child_buy

give_money = give_gife_money(1000)
give_money("一把刀",300)
give_money("一束花",100)
give_money("一辆玛拉莎蒂",600)

a = [1,2,3]
b = [3,4,5]
c = [323,32,3]
a.extend(b)
print(a)
print(a+b+c)

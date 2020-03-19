#
#

# 新功能
def verif_permission(func):
    def wrapper(*args, **kwargs):
        print("验证权限") #新功能逻辑
        return func(*args, **kwargs) #旧功能逻辑
    return wrapper

# 旧功能
@verif_permission
def enter_background():
    print("进入后台")
@verif_permission
def delete_order():
    print("删除订单")

enter_background()
delete_order()


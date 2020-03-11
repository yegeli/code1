"""
       message = "  校 训 是：自强 不息,厚德  载物 ."
   1)查找空格数量
   2)删除前后空格
   3)删除所有空格
   4)查找"厚德"的位置

"""
message = "  校 训 是：自强 不息,厚德  载物 ."

print(message.count(' '))
message1 = message.strip()
print(message1)
message2 = message.replace(' ','')
print(message2)

message3 = message.find('厚德')
print(message3)
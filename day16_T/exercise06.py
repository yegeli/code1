
list01 = ["张无忌","赵敏","小昭"]
list02 = [201,205,232]
list03 = [5000,23232,2121]


def Zip():
    for i in range(len(list03)):
        yield (list01[i],list02[i],list03[i])


c = Zip()
for i in c:
    for x in i :
     print(x)

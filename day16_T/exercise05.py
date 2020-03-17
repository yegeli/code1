def enumerate(list01):
    for i in range(len(list01)):
        yield (i, list01[i])


list01 = [45, 3, 23, 12, 23, 2]
x = enumerate(list01)


for index, element in x:
    if element > 10:
        list01[index] = 0
print(list01)

list = [3, 2, 1]

newlist = []

for i in range(0, len(list)):
    listcopy = list.copy()
    listcopy.remove(list[i])
    arraysum = 1
    for j in listcopy:
        arraysum = arraysum * j
    newlist.append(arraysum)

print(newlist)

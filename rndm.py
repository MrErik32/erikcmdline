qinput = [1, 2, 0]

qinput.sort()
for i in range(qinput[0], len(qinput)*2):
    if i <= 0:
        pass
    else:
        if i not in qinput:
            print(i)
            break
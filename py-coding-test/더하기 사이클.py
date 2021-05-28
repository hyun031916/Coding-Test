N = int(input())
newN = -1

while newN != N:
    if (N < 10):
        strN = '0' + str(N)
        print(strN)
    else:
        strN = str(N)
    newN = int(strN[0])+int(strN[1])
    print(newN)
N = int(input())
check = N
temp = 0
newNum = 0
count = 0

while True:
    temp = N//10+N%10
    newNum = (N%10)*10+temp%10
    count += 1
    num = newNum
    if newNum == check:
        break
print(count)
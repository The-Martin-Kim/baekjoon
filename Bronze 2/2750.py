count = int(input())
num = [0] * count

for i in range(count):
    num[i] = int(input())

num.sort()

for k in num:
    print(k)

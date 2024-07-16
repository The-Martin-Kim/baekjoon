count = int(input())
num = [0] * count

for i in range(count):
    num[i] = int(input())

for i in range(count):
    print(min(num))
    num.remove(min(num))

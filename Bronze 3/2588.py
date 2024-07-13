a = int(input())
b = int(input())
result = a * b

b1 = b // 100
b %= 100

b2 = b // 10

b3 = b % 10

print(a * b3)
print(a * b2)
print(a * b1)
print(result)

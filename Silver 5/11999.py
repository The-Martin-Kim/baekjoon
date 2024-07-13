X, Y, M = map(int, input().split())
result = []
maxY = M // Y

for i in range(maxY+1):
    temp = M
    temp = temp - (Y * i)
    maxX = temp // X
    result.append(X * maxX + Y * i)

print(max(result))


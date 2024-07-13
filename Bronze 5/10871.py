A, X = map(int, input().split())
seq = list(map(int, input().split()))
result = []

for k in seq:
    if k < X:
        result.append(k)

for i in range(len(result)):
    print(result[i], end=" ")

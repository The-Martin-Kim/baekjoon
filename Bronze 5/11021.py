count = int(input())
result = [0] * count

for i in range(count):
    A, B = map(int, input().split())
    result[i] = A + B

for i in range(count):
    print(f"Case #{i + 1}: {result[i]}")

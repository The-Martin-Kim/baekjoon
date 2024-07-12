T = int(input())
result = [0] * T

for i in range(T):
    A, B = map(int, input().split())
    result[i] = A + B

for k in result:
    print(k)

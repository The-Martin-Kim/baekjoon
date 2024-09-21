import sys
input = sys.stdin.readline


def is_divided(a, numbers):
    count = 0
    for k in numbers:
        if k % a == 0:
            count += 1

    return count


N, M = map(int, input().split())

A = list(map(int, input().split()))

S = []
temp = 0
result = 0

for i in range(N):
    for k in A:
        temp += k
        S.append(temp)

    result += is_divided(M, S)
    A.pop(0)
    S = []
    temp = 0

print(result)


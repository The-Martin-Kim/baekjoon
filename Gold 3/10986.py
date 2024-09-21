import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))

remainder = [0] * M

temp = 0
for number in A:
    temp += number
    remainder[temp % M] += 1

result = remainder[0]

for i in range(M):
    result += remainder[i] * (remainder[i] - 1) // 2

print(result)

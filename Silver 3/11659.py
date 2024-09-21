import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

S = [0]
temp = 0

for k in numbers:
    temp += k
    S.append(temp)

result = [0] * M
for i in range(M):
    start, end = map(int, input().split())
    result[i] = S[end] - S[start - 1]

for k in result:
    print(k)

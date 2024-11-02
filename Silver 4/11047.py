import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0] * N

for i in range(N):
    coins[i] = int(input())

result = 0
for i in range(N - 1, -1, -1):
    if coins[i] <= K:
        result += K // coins[i]
        K %= coins[i]

print(result)

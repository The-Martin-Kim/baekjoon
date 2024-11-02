N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)

P.sort()

S = [0] * (N + 1)

for i in range(1, N + 1):
    S[i] = S[i - 1] + P[i]

print(sum(S))

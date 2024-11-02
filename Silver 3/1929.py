import math

M, N = map(int, input().split())
A = [0] * (N + 1)

for i in range(2, N + 1):
    A[i] = i

for i in range(2, int(math.sqrt(N)) + 1):
    if A[i] == 0:
        continue

    for j in range(i * 2, N + 1, i):
        A[j] = 0

count = 0
for i in range(2, N + 1):
    if A[i] != 0:
        for j in range(2, N + 1):
            temp = i ** j
            if M <= temp <= N:
                count += 1
            elif temp > N:
                break

print(count)

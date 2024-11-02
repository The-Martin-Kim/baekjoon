import sys
input = sys.stdin.readline

N = int(input())
time_table = [[0, 0]] * N

for i in range(N):
    start, end = map(int, input().split())
    time_table[i] = [start, end]

time_table.sort(key=lambda x: (x[1], x[0]))

result = 1
end = time_table[0][1]

for i in range(1, N):
    if time_table[i][0] >= end:
        result += 1
        end = time_table[i][1]

print(result)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = list(map(int, input().split()))
arr.sort()

count = 0
start = 0
end = N - 1

while start < end:
    if arr[start] + arr[end] == M:
        count += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] > M:
        end -= 1
    elif arr[start] + arr[end] < M:
        start += 1

print(count)

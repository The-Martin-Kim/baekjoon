# N = int(input())
#
# count = 0
# for i in range(1, N + 1):
#     total = 0
#     for j in range(i, N+1):
#         total += j
#         if total == N:
#             count += 1
#             break
#
# print(count)

N = int(input())

start = 1
end = 1
count = 1
total = 1

while end != N:
    if total == N:
        end += 1
        total += end
        count += 1

    elif total > N:
        total -= start
        start += 1

    elif total < N:
        end += 1
        total += end

print(count)

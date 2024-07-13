A, B = map(int, input().split())
sum_result = []

while A != 0 and B != 0:
    sum_result.append(A + B)
    A, B = map(int, input().split())

for i in range(len(sum_result)):
    print(sum_result[i])

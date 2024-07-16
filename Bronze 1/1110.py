N = int(input())
origin = N
count = 0


def calculate_cycle(num):
    a = num // 10
    b = num % 10
    c = (a + b) % 10

    return 10 * b + c


while True:
    N = calculate_cycle(N)
    count += 1

    if origin == N:
        break

print(count)





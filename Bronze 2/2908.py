A, B = map(int, input().split())


def reverse_num(num):
    a = num // 100
    num %= 100
    b = num // 10
    c = num % 10
    return 100 * c + 10 * b + a


print(max(reverse_num(A), reverse_num(B)))

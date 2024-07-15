H, M = map(int, input().split())

if H == 0:
    H = 24

total = H * 60 + M
total -= 45

H = total // 60 % 24
M = total % 60

print(H, M)

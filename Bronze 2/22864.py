cost, money, rest, threshold = map(int, input().split())

hp = 0
bank = 0
for hour in range(24):
    if hp + cost > threshold:
        if hp - rest < 0:
            hp = 0
        else:
            hp -= rest
    else:
        hp += cost
        bank += money

print(bank)

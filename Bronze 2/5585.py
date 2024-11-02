coins = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())

count = 0
for coin in coins:
    count += change // coin
    change %= coin

print(count)

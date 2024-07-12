score = int(input()) // 10
result = None

if score > 9:
    result = "A"
elif score > 8:
    result = "B"
elif score > 7:
    result = "C"
elif score > 6:
    result = "D"
else:
    result = "F"

print(result)

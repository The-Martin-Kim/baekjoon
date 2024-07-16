arr = int(input())

while arr != 0:
    arr = list(str(arr))

    if arr == arr[::-1]:
        print("yes")
    else:
        print("no")

    arr = int(input())

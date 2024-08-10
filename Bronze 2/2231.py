import sys

num = int(input())
found = False

for i in range(1, num + 1):
    if i + sum(map(int, str(i))) == num:
        print(i)
        found = True
        sys.exit(0)

if found == False:
    print(0)

n = int(input())
A = [0] * n
num_stack = [0]
stack = []

for i in range(n):
    A[i] = int(input())

num = 1
flag = True
for i in range(n):
    if num <= A[i]:
        while num < A[i]:
            num_stack.append(num)
            num += 1
            stack.append("+")
            print(num_stack)

        num_stack.pop()
        stack.append("-")

    elif num > A[i]:
        flag = False

print(flag)


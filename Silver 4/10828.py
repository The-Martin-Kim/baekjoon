def push(stack, x):
    stack.append(x)


def pop(stack):
    if empty(stack) == 1:
        return -1
    else:
        x = top(stack)
        stack.pop()
        return x


def size(stack):
    return len(stack)


def empty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0


def top(stack):
    if empty(stack) == 1:
        return -1
    else:
        return stack[-1]


stack = []
result = []

count = int(input())

for i in range(count):
    command = input()

    if command[:4] == "push":
        x = int(command[5:])
        push(stack, x)
    elif command == "pop":
        result.append(pop(stack))
    elif command == "size":
        result.append(size(stack))
    elif command == "empty":
        result.append(empty(stack))
    elif command == "top":
        result.append(top(stack))

for k in result:
    print(k)

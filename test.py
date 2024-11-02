def push(storage, x):
    storage.append(x)


def pop(storage):
    storage.pop()


stack = []
push(stack, 3)
push(stack, 4)
push(stack, 7)
pop(stack)

print(stack)


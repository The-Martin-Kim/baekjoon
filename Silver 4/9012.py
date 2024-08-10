T = int(input())
parenthesis_string = []

for i in range(T):
    parenthesis_string.append(input())

for string in parenthesis_string:
    flag = True
    stack = []
    for k in string:
        if not flag:
            continue
        else:
            if k == "(":
                stack.append(k)
            else:
                if len(stack) == 0:
                    flag = False
                else:
                    stack.pop()

    if not flag:
        print("NO")
    elif len(stack) == 0:
        print("YES")
    else:
        print("NO")

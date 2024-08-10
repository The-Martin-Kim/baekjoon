count = int(input())
sentences = []

for i in range(count):
    sentences.append(input())

for sentence in sentences:
    words = sentence.split(" ")

    stack = []
    result = []
    for word in words:
        for letter in word:
            stack.append(letter)

        while len(stack) != 0:
            temp = stack[-1]
            result.append(temp)
            stack.pop()
        result.append(" ")

    for k in result:
        print(k, end="")
    print()

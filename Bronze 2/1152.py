sentence = list(input())
count = 1

for i in range(len(sentence)):
    if sentence[i] == " ":
        count += 1

if sentence[0] == " ":
    count -= 1

if sentence[len(sentence) - 1] == " ":
    count -= 1

print(count)

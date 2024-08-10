def reverse(sentence):
    words = list(sentence.split(" "))
    for i in range(len(words)):
        words[i] = words[i][::-1]

    print(" ".join(words))


count = int(input())
sentences = []

for i in range(count):
    sentence = input()
    sentences.append(sentence)

for k in sentences:
    reverse(k)

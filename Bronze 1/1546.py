N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
avg = sum(scores) * 100 / max_score / N

print(avg)

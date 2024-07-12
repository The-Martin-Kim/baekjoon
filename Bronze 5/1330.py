A, B = map(int, input().split())
result = None

if A > B:
    result = ">"
elif A < B:
    result = "<"
else:
    result = "=="

print(result)

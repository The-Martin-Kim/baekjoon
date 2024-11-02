N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
avg = sum(scores) * 100 / max_score / N

print(avg)

# 과목의 수 N을 입력 받는다.
# 현재 성적을 리스트 형태로 입력 받는다.

# 성적 중 최댓값을 구해 M에 저장한다.

# 반복문을 통해 각 성적에 접근을 한다.
# 각 성적에 대해 M으로 나누고 100을 곱해 저장한다.

# 각 성적을 모두 더하고 과목의 수 N으로 나누어 출력한다.

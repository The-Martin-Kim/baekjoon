N = int(input())
num = list(map(int, input().split()))


def find_max(arr):
    max_num = -1000000
    for k in arr:
        if k > max_num:
            max_num = k

    return max_num


def find_min(arr):
    min_num = 1000000
    for k in arr:
        if k < min_num:
            min_num = k

    return min_num



print(find_min(num), find_max(num))

# 정수의 개수 N을 입력받는다.
# N개의 정수를 리스트 numbers에 입력받는다.
# max 함수와 min 함수를 활용하여 최댓값과 최솟값을 찾는다.
# 찾은 최댓값과 최솟값을 출력한다.

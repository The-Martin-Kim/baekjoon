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

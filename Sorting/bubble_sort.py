def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


def selection_sort(arr):
    for i in range(len(arr)):
        min_value = min(arr[i:])
        min_idx = arr.index(min_value, i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(arr)




numbers = [13, 7, 15, 1]

# bubble_sort(numbers)
# selection_sort(numbers)
# insertion_sort(numbers)


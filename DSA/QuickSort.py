import random
from IsAscending import is_ascending


def quick_sort(arr: list, left: int =None, right: int =None):

    if left is None:
        left = 0
        right = len(arr) - 1
    print(f'quicksort: {left} to {right}')
    i = left
    j = right
    key = arr[(i + j) // 2]
    print(f'key: {key}')
    while i < j:
        while arr[i] < key: i += 1
        while arr[j] > key: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            print(f'i, j = {i}, {j}')
            print(f'array: {arr}')
            i += 1
            j -= 1
    print()
    if right - left in (0, 1):
        return
    else:
        quick_sort(arr, left, j)
        quick_sort(arr, i, right)

if __name__ == '__main__':
    arr = [random.randint(10, 100)] * 16
    print(arr)
    quick_sort(arr)
    print(arr, is_ascending(arr))

import random
from IsAscending import is_ascending


def quick_sort(arr: list, left: int, right: int):
    i = left
    j = right
    pivot = arr[(left + right) // 2]
    compare = 0
    while i <= j:
        compare += 1
        while arr[i] < pivot: i += 1; compare += 1
        while arr[j] > pivot: j -= 1; compare += 1
        if i <= j:
            compare += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if left < j:
        quick_sort(arr, left, j)
    if i < right:
        quick_sort(arr, i, right)
    return compare

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(arr)
    result = quick_sort(arr, 0, len(arr) - 1 )
    print(result, is_ascending(arr))

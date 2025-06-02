import random
from IsAscending import is_ascending


def selection_sort_v1(arr: list):
    # original idea but slow because of shifting problem
    n = len(arr)
    for i in range(n - 1):
        index_min = i
        for j in range(i, n):
            if arr[j] < arr[index_min]:
                index_min = j
        min_value = arr.pop(index_min)
        arr.insert(i, min_value)
    return arr


def selection_sort_v2(arr: list):
    # selection sort without shifting problem, using swapping
    n = len(arr)
    for i in range(n - 1):
        index_min = i
        for j in range(i, n):
            if arr[j] < arr[index_min]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]
    return arr

if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    selection_sort_v1(arr)
    print(arr, is_ascending(arr))


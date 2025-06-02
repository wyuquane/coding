import random
from IsAscending import is_ascending


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr

if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    bubble_sort(arr)
    print(arr, is_ascending(arr))

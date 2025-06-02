import random
import time

from IsAscending import is_ascending


def heapify(arr: list, pos: int, last: int):

    right = 2 * pos + 2
    left = 2 * pos + 1
    if right <= last:
        if arr[pos] >= max(arr[left], arr[right]):
            return
        elif arr[left] > arr[right]:
            arr[pos], arr[left] = arr[left], arr[pos]
            heapify(arr, left, last)
        else:
            arr[pos], arr[right] = arr[right], arr[pos]
            heapify(arr, right, last)
    elif left <= last:
        if arr[pos] < arr[left]:
            arr[pos], arr[left] = arr[left], arr[pos]
            heapify(arr, left, last)

def heap_sort(arr: list):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i, len(arr) - 1)

    # print(arr)

    for i in range(len(arr) - 1):
        arr[0], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[0]
        heapify(arr, 0, len(arr) - 2 - i)


if __name__ == '__main__':
    arr = [random.randint(10, 100000) for _ in range(1000000)]
    # print(arr)
    start = time.time()
    heap_sort(arr)
    end = time.time()
    # print(arr, is_ascending(arr))
    print(end - start)

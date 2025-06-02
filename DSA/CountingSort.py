import random
from IsAscending import is_ascending


def counting_sort(arr: list[int]):
    limit = max(arr)
    count_list = [0] * (limit + 1)
    for i in range(len(arr)):
        num = arr.pop(0)
        count_list[num] += 1
    for i in range(limit + 1):
        arr.extend([i] * count_list[i])
    return arr

if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    counting_sort(arr)
    print(arr,is_ascending(arr))




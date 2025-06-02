import random
from IsAscending import is_ascending


def insertion_sort_v1(arr: list):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i + 1):
            if arr[j] >= arr[i]:
                # print('insert:', j)
                insert_value = arr.pop(i)
                arr.insert(j, insert_value)
                break
        # print(i, arr, '\n')
    return arr

def insertion_sort_v2(arr: list):
    n = len(arr)
    for i in range(1, n):
        insert_val = arr[i]
        insert_index = i
        for j in range(i - 1, -1, -1):
            if arr[j] >= insert_val:
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = insert_val
    return arr


if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    insertion_sort_v2(arr)
    print(arr, is_ascending(arr))
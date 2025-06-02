import random
from IsAscending import is_ascending


def split(arr: list):
    if len(arr) == 1:
        return arr
    arr1 = arr[0: len(arr) // 2]
    arr2 = arr[len(arr) // 2: len(arr)]
    return [split(arr1), split(arr2)]

def merge(two_arr: list):
    for arr in two_arr:
        if isinstance(arr[0], list):
            merge(arr)

    arr1 = two_arr[0]
    arr2 = two_arr[1]

    result = list()
    i = j = 0
    len1 = len(arr1)
    len2 = len(arr2)

    while i < len1 or j < len2:
        if i < len1 and j < len2:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len1:
            while i < len1:
                result.append(arr1[i])
                i += 1
        else:
            while j < len2:
                result.append(arr2[j])
                j += 1
    two_arr.clear()
    two_arr.extend(result)


def merge_sort(arr: list):
    arr = split(arr)
    merge(arr)
    return arr

if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    arr = merge_sort(arr)
    print(arr, is_ascending(arr))
def selection_sort(arr: list):
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        # print(i, arr)
        insert_val = arr[i]
        j = i - 1
        while arr[j] > insert_val and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_val

def interchange_sort(arr: list):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 2, i - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def shaker_sort(arr: list):
    surface = 0
    bottom = len(arr) - 1
    while surface < bottom:
        print(surface, bottom)
        print(arr)
        # sinking
        temp = bottom
        bottom = surface
        for i in range(surface, temp):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                bottom = i
        # floating
        temp = surface
        surface = bottom
        for i in range(bottom, temp, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                surface = i

def heapify(arr: list, pos: int, end: int):
    left = 2 * pos + 1
    right = left + 1
    if left > end:
        return
    if right > end:
        if arr[pos] < arr[left]:
            arr[pos], arr[left] = arr[left], arr[pos]
        return
    if arr[pos] < max(arr[left], arr[right]):
        if arr[left] > arr[right]:
            arr[pos], arr[left] = arr[left], arr[pos]
            heapify(arr, left, end)
        else:
            arr[pos], arr[right] = arr[right], arr[pos]
            heapify(arr, right, end)

def heap_sort(arr: list):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, i, n - 1)

    for i in range(n - 1):
        arr[0], arr[-1 - i] = arr[-1 - i], arr[0]
        heapify(arr, 0, n - 2 - i)




def merge(arr1: list, arr2: list):
    i = j = 0
    result = list()
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    if i < len(arr1):
        result += arr1[i:]
    else:
        result += arr2[j:]

    return result

def merge_sort(arr: list):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def get_tail_digit(num: int, k: int):
    if len(str(num)) < k:
        return 0
    else:
        return int(str(num)[-k])

def radix_sort(arr: list):
    length = len(str(max(arr)))
    for i in range(1, length + 1):
        container = [[], [], [], [], [], [], [], [], [], []]
        for num in arr:
            container[get_tail_digit(num, i)].append(num)

        arr.clear()
        for k in range(10):
            arr.extend(container[k])








if __name__ == '__main__':
    import random
    from IsAscending import is_ascending
    array = [random.randint(10000000, 1000000000) for _ in range(10)]
    print(array)
    radix_sort(array)
    print(array, is_ascending(array))
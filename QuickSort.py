def quick_sort(arr: list, a: int, b: int):
    i = a
    j = b
    # mid = random.randint(a, b)
    bolt = arr[(a + b) // 2]
    while i <= j:
        while arr[i] < bolt: i += 1
        while arr[j] > bolt: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if a < j:
        quick_sort(arr, a, j)
    if i < b:
        quick_sort(arr, i, b)


arr = [70, 23, 16, 90, 80, 59, 42, 6, 97, 23]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
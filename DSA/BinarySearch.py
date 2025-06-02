import random


def binary_search(target, arr: list):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# IndexError if length of arr is equal to zero

# def binary_search(target, arr: list):
#     left = 0
#     right = len(arr) - 1
#     mid = (left + right) // 2
#     while left < right:
#         if target > arr[mid]:
#             left = mid + 1
#             mid = (left + right) // 2
#         elif target < arr[mid]:
#             right = mid - 1
#             mid = (left + right) // 2
#         else:
#             return mid
#
#     return mid if target == arr[mid] else -1

if __name__ == '__main__':
    target = random.randint(10, 20)
    length = random.randint(0, 20)
    array = [random.randint(10, 20) for _ in range(length)]
    array.sort()

    print(f'target: {target}\narray: {array}')
    print(f'binary search: {binary_search(target, array)}')
    print(f'index: {array.index(target) if target in array else -1}')
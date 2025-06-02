import random


def linear_search(target, arr):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1

if __name__ == '__main__':
    target = random.randint(10, 40)
    array = [random.randint(10, 40) for _ in range(20)]
    print(f'target: {target}\narray: {array}')
    print(f'linear search: {linear_search(target, array)}')
    print(f'index: {array.index(target) if target in array else -1}')
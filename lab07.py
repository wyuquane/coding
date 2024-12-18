import random
import numpy as np

def create_checkerboard(n: int):
    arr = np.ones((n, n), dtype=int)
    arr[::2, ::2] = 0
    arr[1::2, 1::2] = 0
    return arr

def replace_odd_nums(arr: np.ndarray):
    bool_indx = arr % 2 != 0
    arr[bool_indx] = -1
    return

def create_matrix(arr: np.ndarray):
    n = arr.shape[0]
    arr = arr.reshape((int(n ** 0.5), -1))
    return arr

def random_list(n: int, i: int, k: int):
    arr = np.ones((n, ), dtype=int)
    for j in range(n):
        arr[j] = random.choice(range(i, k + 1))
    return arr

def extract_k_th_column(arr: np.ndarray, k: int):
    return arr[:, k]

def unique_rows(arr: np.ndarray):
    fancy_index = list()
    for i in range(len(arr)):
        if len(set(arr[i])) == len(arr[i]):
            fancy_index.append(i)
    return arr[fancy_index]

def compute_product(arr: np.ndarray):
    return np.prod(arr, axis=1)

def sum_between_20_50(arr: np.ndarray):
    bigger_20 = arr > 20
    smaller_50 = arr < 50
    bool_index = np.logical_and(bigger_20, smaller_50)
    return np.sum(arr[bool_index])

def reverse_vertically(arr: np.ndarray):
    if arr.ndim == 1:
        arr = arr[::-1]
    elif arr.ndim == 2:
        for i in range(arr.shape[0]):
            arr[i] = arr[i][::-1]
    return arr

def find_max_row(arr: np.ndarray):
    sum_rows = np.sum(arr, 1)
    print(sum_rows)
    for i, sum_row in enumerate(sum_rows):
        if sum_row == np.max(sum_rows):
            return arr[i]

def diagonal_matrix(arr: np.ndarray):
    n = len(arr)
    matrix = np.zeros((n * n, ), dtype= int)
    matrix[:: n + 1] = arr
    matrix = matrix.reshape((n, n))
    return matrix



if __name__ == '__main__':
    m, n = map(int, input().strip().split())
    np_list = list()
    for _ in range(m):
        np_list.append(list(random_list(n, 10, 100)))
    np_arr = np.array(np_list)
    np_arr = np_arr.flatten()
    print(np_arr)

    print(diagonal_matrix(np_arr))


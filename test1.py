import numpy as np
import random

if __name__ == '__main__':
    def random_list(n: int, i: int, k: int):
        arr = np.ones((n, ), dtype=int)
        for j in range(n):
            arr[j] = random.choice(range(i, k + 1))
        return arr

    # m, n = map(int, input().strip().split())
    m, n = 3, 4

    np_list = list()
    for _ in range(m):
        np_list.append(list(random_list(n, -10, 10)))
    arr = np.array(np_list)
    print(arr)

    even_rows = arr[::2]
    even_rows[even_rows < 0] = 0
    print(arr)

if __name__ == '__main__':
    a = np.arange(12).reshape((3, 2, 2))
    b = a + 2
    c = np.concatenate((a, b), axis=0)
    print(c)


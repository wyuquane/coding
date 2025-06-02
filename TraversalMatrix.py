import numpy as np

m = int(input()) # num of column
n = int(input()) # num of row

nums = [i for i in range(1, m * n + 1)]

matrix = [[0] * m for i in range(n)]

if m == n and m % 2 == 1:
    matrix[n // 2][m // 2] = nums[-1]
indx = 0
for i in range((n + 1) // 2):
    for j in range(i, m - 1 - i):
        # print(i, j)
        matrix[i][j] = nums[indx]
        indx += 1
    for j in range(i, n - 1 - i):
        # print(i, j)
        matrix[j][m - i - 1] = nums[indx]
        indx += 1
    for j in range(i, m - 1 - i):
        # print(i, j)
        matrix[n - i - 1][m - j - 1] = nums[indx]
        indx += 1
    for j in range(i, n - 1 - i):
        # print(i, j)
        matrix[n - 1 - j][i] = nums[indx]
        indx += 1


print(np.array(matrix))
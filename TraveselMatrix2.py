import pandas as pd

n = int(input())

nums = [i + 1 for i in range(n * n)]
matrix = [[0] * n for i in range(n)]

i = 0
j = 1
indx = 1
matrix[0][0] = nums[0]
phase = 'down' #up or down

while i < n and j < n:
    matrix[i][j] = nums[indx]
    indx += 1
    if phase == 'down' and i == n - 1:
        j += 1
        phase = 'up'
        continue
    if phase == 'up' and j == n - 1:
        i += 1
        phase = 'down'
        continue
    if phase == 'down' and j == 0:
        i += 1
        phase = 'up'
        continue
    if phase == 'up' and i == 0:
        j += 1
        phase = 'down'
        continue

    if phase == 'down':
        i += 1
        j -= 1
    if phase == 'up':
        i -= 1
        j += 1

print(pd.DataFrame(matrix))

def N_travesel(limit: int, row : int):
    nums = [i + 1 for i in range(limit)]
    matrix = list()
    column = limit // row + row
    for _ in range(row):
        matrix.append([0 for i in range(column)])

    indx = 0
    phase = 'down'
    i = j = 0
    while indx != limit:
        matrix[i][j] = nums[indx]
        indx += 1
        if phase == 'down':
            if i == row - 1:
                i -= 1
                j += 1
                phase = 'up'
            else:
                i += 1
        else:
            if i == 0:
                i += 1
                phase = 'down'
            else:
                i -= 1
                j += 1

    for eachrow in matrix:
        print(eachrow)

N_travesel(16, 4)
def min_arr_n(arr: list, n: int):
    result = 30000
    for i in range(len(arr)):
        if result > arr[i][n]:
            result = arr[i][n]
    return result

def matrix_filter(maxtrix: list, n: int) -> list:
    temp_list = list()
    for i in range(len(maxtrix)):
        if maxtrix[i][0] > n:
            temp_list.append(maxtrix[i])
    return temp_list

def time_table(matrix: list):
    result = list()
    while True:
        result.append(min_arr_n(matrix, 0))
        temp_list = list()
        for i in range(len(matrix)):
            if matrix[i][0] == min_arr_n(matrix, 0):
                temp_list.append(matrix[i])
        result.append(min_arr_n(temp_list, 1))\
        # loc so ra khoi list
        matrix = matrix_filter(matrix, result[-1])
        '''j = 0
        while j <= len(matrix) - 1:
            if matrix[j][0] <= result[-1]:
                matrix.pop(j)
            j += 1'''
        '''for i in range(len(matrix)):
            if matrix[i][0] <= result[-1]:
                matrix.pop(i)'''
        if len(matrix) == 0:
            break
    return result

def max_no_reports(arr: list):
    return int(len(arr) // 2)


if __name__ == '__main__':
    N = int(input())
    schedule = list()
    for _ in range(N):
        start, end = map(int, input().split())
        schedule.append([start, end])
    result = time_table(schedule)
    print(result)
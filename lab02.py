def sort_height(a: list, b: list):
    for i in range(len(a), 0, -1):
        for j in range(0, i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def most_appear(arr: list):
    result = list()
    appear = arr.count(0)
    for i in range(len(arr)):
        if arr.count(arr[i]) > appear:
            result.clear()
            result.append(arr[i])
            appear = arr.count(arr[i])
        elif arr.count(arr[i]) == appear and not arr[i] in result:
            result.append(arr[i])
    return result

def find_missing(arr: list):
    full = list(range(len(arr) + 1))
    for i in full:
        if not i in arr:
            return i

def k_th_largest(arr: list, k: int):
    set_num = set(arr)
    ascending_oder = list(set_num)
    ascending_oder.sort()
    # print(ascending_oder)
    return ascending_oder[-k]

def plus_one(arr: list):
    arr.reverse()
    arr[0] += 1
    for i in range(len(arr)):
        if i == len(arr) - 1:
            if arr[i] == 10:
                arr[i] = 0
                arr.append(1)
        if arr[i] == 10:
            arr[i] = 0
            arr[i + 1] += 1
    arr.reverse()
    return arr

def merge_array(a: list, b: list):
    c = a + b
    c.sort()
    return c

def no_digit(n: int):
    str_n = str(n)
    return len(str_n)

def largest_number(arr: list):
    total_digit = 0
    for num in arr:
        total_digit += no_digit(num)
    pop_list = list()
    result = 0
    for i in range(len(arr)):
        temp_value = 0
        temp_index = 0
        for j in range(len(arr)):
            if arr[j] * 10 ** (total_digit - no_digit(arr[j])) > temp_value and j not in pop_list:
                temp_index = j
                temp_value = arr[j] * 10 ** (total_digit - no_digit(arr[j]))
        pop_list.append(temp_index)
        result += temp_value
        total_digit -= no_digit(arr[temp_index])
    return result

def flip_and_invert(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - j - 1], matrix[i][j]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def sum_triplet(arr: list):
    result = list()
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp_list = [arr[i], arr[j], arr[k]]
                    temp_list.sort()
                    # print(temp_list)
                    if temp_list not in result:
                        result.append(temp_list)
    return result



if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(sum_triplet(arr))
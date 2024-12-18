import random

import numpy as np
from numpy import ndarray


def is_not_empty(s: str):
    if len(s) == 0:
        return False
    return True

def readFile(filename: str) -> list:
    file = open(filename, 'rt', encoding='utf-8')
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
    data = list(filter(is_not_empty, data))
    return data

def extract_num(s: str):
    num = str()
    for char in s:
        if char.isnumeric():
            num += char
    num = int(num)
    return num

def mergeFile(filename1: str, filename2: str) -> list:
    data1 = readFile(filename1)
    data2 = readFile(filename2)
    data = data1 + data2
    data.sort(key=extract_num)
    return data

def del_num(s: str):
    for char in s:
        if char.isnumeric():
            s = s[1: ]
        else:
            return s

def writeFile(out_file: str, content: list) -> None:
    file = open(out_file, 'wt', encoding='utf-8')
    content = list(map(del_num, content))
    for line in content:
        file.write(line + '\n')
    file.close()
    return None


def convert(filename: str) -> str:
    file = open(filename, 'rt', encoding='utf-8')
    data = file.read()
    file.close()
    data = data.replace(' ', '')
    data = data.replace('\n', ' ')
    return data

def creatMatrix(n: int, m: int, a: int, b: int):
    result = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            x = random.randint(a, b)
            result[i, j] = x
    return result

def clockwise_rotate(matrix: ndarray):
    result = list()
    row, column = matrix.shape
    for i in range(column):
        result.append([matrix[row - 1 - j, i] for j in range(row)])
    return np.array(result)

def rotateMatrix(matrix, rotate=True, times=1):
    if not rotate:
        times = times * 3
    for _ in range(times):
        matrix = clockwise_rotate(matrix)
    return matrix


if __name__ == '__main__':
    matrix = creatMatrix(4, 3, 1, 9)
    print(matrix)
    print('--------------')
    matrix = rotateMatrix(matrix, False, 1)
    print(matrix)


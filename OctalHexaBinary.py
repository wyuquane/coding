import math

def convert_octa(num: int) -> str:
    result = 0
    n = math.floor(math.log(num, 8))
    for _ in range(n):
        result += num // (8 ** n)
        result *= 10
        num %= 8 ** n
        n -= 1
    result += num
    return str(result)

def convert_hexa(num: int) -> str:
    hexa = '0123456789ABCDEF'
    result = ''
    n = math.floor(math.log(num, 16))
    k = 0
    for _ in range(n):
        k = num // (16 ** n)
        result += hexa[k]
        num %= 16 ** n
        n -= 1
    result += hexa[num]
    return result

def convert_binary(num: int) -> str:
    result = 0
    n = math.floor(math.log(num, 2))
    for _ in range(n):
        result += num // (2 ** n)
        result *= 10
        num %= 2 ** n
        n -= 1
    result += num
    return str(result)

def print_formatted(num):
    width = len(convert_binary(num))
    for i in range(1, num + 1):
        print(' ' * (width - len(str(i))), end='')
        print(i, end='')
        print(' ', end='')
        print(' ' * (width - len(convert_octa(i))), end='')
        print(convert_octa(i), end='')
        print(' ', end='')
        print(' ' * (width - len(convert_hexa(i))), end='')
        print(convert_hexa(i), end='')
        print(' ', end='')
        print(' ' * (width - len(convert_binary(i))), end='')
        print(convert_binary(i), end='')
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
def romand_number(n: int):
    result = str()
    value_table = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                   100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                   10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    value = list(value_table.keys())
    letter = list(value_table.values())
    indx = 0
    while n > 0:
        if n >= value[indx]:
            result += letter[indx]
            n -= value[indx]
        else:
            indx += 1
    return result

if __name__ == '__main__':
    n = int(input())
    print(romand_number(n))


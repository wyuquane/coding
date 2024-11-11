num = int(input())
reversed_num = 0
while num >= 10:
    digit = num % 10
    num -= digit
    num /= 10
    reversed_num += digit
    reversed_num *= 10
reversed_num += num
print(int(reversed_num))

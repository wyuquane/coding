num = int(input())
mistake = 0
first_digit = -1
second_digit = -1
while num >= 10:
    first_digit = num % 10
    second_digit = (num % 100 - first_digit) / 10
    if second_digit > first_digit:
        mistake += 1
    num -= num % 10
    num /= 10
if mistake == 0:
    print('true')
else:
    print('false')

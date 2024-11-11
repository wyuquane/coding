def prime(n: int):
    if n <= 1:
        return False
    else:
        boo = True
        for i in range(2, n):
            if n % i == 0:
                boo = False
        return boo
m, n = map(int, input().split())
sum = 0
no_num = 0
for i in range(m, n + 1):
    if prime(i):
        sum += i
        no_num += 1
if no_num == 0:
    print('-')
else:
    print('%.2f' % (sum / no_num))


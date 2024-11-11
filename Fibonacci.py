k = int(input())
if k == 1:
    print('0')
if k == 2:
    print('0 1')
u_n = 1
u_n_1 = 0
print('0 1 ', end='')
for i in range(3, k + 1):
    u = u_n + u_n_1
    print(u, end= ' ')
    u_n_1 = u_n
    u_n = u

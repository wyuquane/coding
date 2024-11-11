n = input()
n_digits = list(map(int, n))
def mu(co_so: int):
    return (co_so ** len(n_digits))
n_digits2 = list(map(mu, n_digits))
sum = 0
for num in n_digits2:
    sum += num
print(sum)
if int(n) == sum:
    print('yes')
else:
    print('no')
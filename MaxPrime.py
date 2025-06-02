def prime(num: int):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

arr = list(map(int, input().split()))
primes = list()
for num in arr:
    if prime(num):
        primes.append(num)
if len(primes) == 0:
    print('-')
else:
    maxprime = primes[0]
    for i in range(0, len(primes)):
        if maxprime <= primes[i]:
            maxprime = primes[i]
    print(maxprime)

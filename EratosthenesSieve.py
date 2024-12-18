def eratosthenes(limit: int):
    is_prime = [0, 0] + [1] * (limit - 1)
    primes = list()
    for i in range(2, limit // 2 + 1):
        if is_prime[i] == 1:
            for k in range(2, limit // i + 1):
                is_prime[k * i] = 0
    for j in range(limit + 1):
        if is_prime[j] == 1:
            primes.append(j)
    return primes

if __name__ == '__main__':
    print(eratosthenes(31))
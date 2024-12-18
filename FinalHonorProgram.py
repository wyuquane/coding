
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return

    def __str__(self):
        result = str()
        cur = self.head
        while cur is not None:
            result += str(cur.data) + ' -> '
            cur = cur.next
        result += 'None'
        return result

def list_of_factor(n: int) -> SinglyLinkedList:
    factor = list()
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factor.append(i)
    result = SinglyLinkedList()
    for num in factor:
        result.add_head(num)
    return result

def prime_sieve(n: int) -> list:
    sieve = list(range(2, n + 1))
    i = 0
    while i < int(n ** 0.5):
        for j in range(2, n // sieve[i] + 1):
            try:
                sieve.remove(sieve[i] * j)
            except:
                pass
        i += 1
    return sieve

def prime_factorization(n: int) -> None:
    primes = prime_sieve(n // 2)
    power = list()
    for prime in primes:
        temp = 0
        while n % prime == 0:
            n = n // prime
            temp += 1
        power.append(temp)
        if n == 1: break
    for i, ele in enumerate(power):
        if ele == 0:
            continue
        else:
            for j in range(ele, -1, -1):
                print(primes[i] ** j, end= ' ')
            print()

if __name__ == '__main__':
    print(list_of_factor(28))
    prime_factorization(174636)
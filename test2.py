import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Node: {self.data} ->'

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.append_list(data)

    def append_list(self, arr):
        add_list = LinkedList()
        for num in arr[::-1]:
            new_node = Node(num)
            new_node.next = add_list.head
            add_list.head = new_node

        if self.head is None:
            self.head = add_list.head
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = add_list.head
        return

    def __str__(self):
        result = str()
        cur = self.head
        while cur:
            result += str(cur.data) + ' -> '
            cur = cur.next

        result += 'None'
        return result

def remove_same_node(ll1: LinkedList, ll2: LinkedList) -> None:
    list1 = list()
    list2 = list()

    cur1 = ll1.head
    cur2 = ll2.head

    while cur1 is not None:
        list1.append(cur1.data)
        cur1 = cur1.next

    while cur2 is not None:
        list2.append(cur2.data)
        cur2 = cur2.next

    duplicate = set(list1) & set(list2)

    while ll1.head and ll1.head.data in duplicate:
        temp = ll1.head.next
        ll1.head.next = None
        ll1.head = temp

    while ll2.head and ll2.head.data in duplicate:
        temp = ll2.head.next
        ll2.head.next = None
        ll2.head = temp

    cur1 = ll1.head
    while cur1 and cur1.next is not None:
        if cur1.next.data in duplicate:
            cur1.next = cur1.next.next
        else:
            cur1 = cur1.next

    cur2 = ll2.head
    while cur2 and cur2.next is not None:
        if cur2.next.data in duplicate:
            cur2.next = cur2.next.next
        else:
            cur2 = cur2.next

    return None

def isPalindrome(ll: LinkedList) -> bool:
    if ll.head is None or ll.head.next is None: return True

    slow = ll.head
    fast = ll.head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head = slow.next
    slow.next = None

    # reverse
    before = None
    after = head.next

    while after is not None:
        head.next = before
        before = head
        head = after
        after = after.next

    head.next = before

    cur = ll.head
    while head is not None:
        if head.data != cur.data:
            return False
        head = head.next
        cur = cur.next

    return True

def generate(directors: list, n: int, k: int):
    if k == 0:
        print([])
        return

    queues = list()
    for name in directors[0: n - k + 1]:
        queues.append([name])

    for i in range(1, k):
        for j in range(len(queues)):
            element = queues.pop(0)
            for t in range(directors.index(element[-1]) + 1, n - k + i + 1):
                queues.append(element + [directors[t]])

    print(queues)
    return

def getWords(s: str):
    W = list()
    n = 0

    word = str()
    for char in s:
        if char.isalpha():
            word += char
        else:
            if len(word) != 0:
                W.append(word)
                n += 1
                word = str()

    if len(word) != 0:
        W.append(word)
        n += 1
        word = str()

    return W, n

def reverse(ll: LinkedList):
    if ll.head is None or ll.head.next is None: return

    before = None
    cur = ll.head
    after = cur.next

    while after:
        cur.next = before
        before = cur
        cur = after
        after = after.next
    cur.next = before
    ll.head = cur

    return

def trimTail(ll: LinkedList):
    reverse(ll)

    while ll.head and ll.head.data == ' ':
        cur = ll.head.next
        ll.head.next = None
        ll.head = cur

    reverse(ll)

def creatPascalMatrix(n: int):
    matrix = [[1] * n for _ in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = 0
    for row in matrix:
        print(row)

def getKthNodeFromTail(ll: LinkedList, k: int):
    if ll.head is None:
        return None
    if k <= 0:
        return None

    length = 0
    cur = ll.head
    while cur:
        length += 1
        cur = cur.next

    if k > length: return None

    result = ll.head
    for _ in range(length - k):
        result = result.next

    return result

def toBitString(n: int):
    result = str()
    while n != 0:
        digit = n % 2
        result += str(digit)
        n = n // 2

    return result[::-1]

def is_prime(n: int):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def countPrime(head: Node):
    if head is None:
        return 0

    if is_prime(head.data):
        return 1 + countPrime(head.next)
    else:
        return countPrime(head.next)

if __name__ == '__main__':
    ll = LinkedList([random.randint(1, 20) for _ in range(7)])
    print(ll)
    print(countPrime(ll.head))



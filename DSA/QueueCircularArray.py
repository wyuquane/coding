class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, size: int):
        self.head = self.create(size)
        self.size = size

    def create(self, size):
        head = Node()
        cur = head
        for _ in range(size - 1):
            cur.next = Node()
            cur = cur.next

        cur.next = head
        return head

class Queue:
    def __init__(self, max_size: int):
        self.data = CircularLinkedList(max_size)
        self.front = self.data.head
        self.rear = self.front
        self.max_size = max_size
        self.size = 0

    def enqueue(self, data):
        if self.is_full(): return
        self.rear.data = data
        self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        if self.is_empty(): return
        self.front = self.front.next
        self.size -= 1
        return True

    def front(self):
        if self.is_empty(): return
        return self.front.data

    def size(self):
        return self.size

    def is_full(self):
        return bool(self.size == self.max_size)

    def is_empty(self):
        return bool(self.size == 0)

from LinkedList import SinglyLinkedList


class QueuesLinkedList:
    def __init__(self):
        self.queues = SinglyLinkedList()
        self.length = 0

    def enqueue(self, data):
        self.queues.add_tail(data)
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        front = self.queues.head.data
        self.queues.del_head()
        self.length -= 1
        return front

    def front(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.queues.head.data

    def size(self):
        return self.length

    def is_empty(self):
        return True if self.length == 0 else False

    def __str__(self):
        if self.is_empty(): return 'queue is empty'
        result = 'front -> '
        cur = self.queues.head
        while cur:
            result += f'{cur.data}] '
            cur = cur.next
        return result

if __name__ == "__main__":
    q = QueuesLinkedList()
    q.dequeue()
    q.front()
    print(q)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.dequeue())
    print(q.front())
    print(q.size())
    print(q.is_empty())
    print(q)

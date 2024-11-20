

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' => ')
            current = current.next
        print(None)

    def addHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def removeHead(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next

    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current

    def removeAll(self):
        self.head = None
        self.tail = None

    def removeBefore(self, val):
        current = self.head
        while current:
            if current.data == val:
                self.head = current
                return
            current = current.next

    def removePos(self, pos: int):
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        if pos < 0 or pos > len - 1:
            return
        elif pos == 0:
            self.removeHead()
            return
        elif pos == len - 1:
            self.removeTail()
            return
        indx = 0
        current = self.head
        while current:
            if indx == pos - 1:
                current.next = current.next.next
            indx += 1
            current = current.next

if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.addHead(4)
    ll.addHead(5)
    ll.addTail(3)
    ll.addTail(2)
    ll.addTail(1)
    ll.display()
    ll.removePos(5)
    ll.display()




























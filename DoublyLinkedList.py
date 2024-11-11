class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLL:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def delete_head(self):
        if self.head is None: return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # def delete_tail(self):
    #     if self.head is None: return
    #     if self.head.next is None:
    #         self.head = None
    #     cur = self.head
    #     while cur.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

    def is_palindrome(self) -> bool:
        from_head = self.head
        from_tail = self.head
        while from_tail.next:
            from_tail = from_tail.next
        while from_tail.prev is not None and from_head.next is not None:
            if from_head.data != from_tail.data:
                return False
            from_head = from_head.next
            from_tail = from_tail.prev
        return True


if __name__ == '__main__':
    l = doublyLL()
    l.add_head(1)
    l.add_head(2)
    l.add_head(3)
    l.add_head(3)
    l.add_head(2)
    l.add_head(1)
    # l.delete_head()
    l.display()
    boo = l.is_palindrome()
    print(boo)



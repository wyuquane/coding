class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node
        return

    def del_head(self):
        if self.head is None: return
        self.head = self.head.next
        return

    def del_tail(self):
        if self.head is None: return
        if self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        return

    def add_tail(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        return

    def __str__(self):
        result = str()
        cur = self.head
        while cur:
            result += str(cur.data) + ' -> '
            cur = cur.next
        result += 'None'
        return result


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

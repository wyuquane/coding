class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Stack:
    def __init__(self, limit = 1000):
        self.data = None
        self.limit = limit

    def push(self, item):
        # add head
        new_node = Node(item)
        if self.data is None:
            self.data = new_node
        else:
            new_node.next = self.data
            self.data = new_node

    def pop(self):
        # delete head
        if self.data is None: return None
        else:
            del_item = self.data.key
            self.data = self.data.next
            return del_item



    def top(self):
        return self.data.key

    def len(self):
        count = 0
        cur = self.data
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def is_full(self):
        if self.len() < self.limit:
            return False
        else:
            return True

    def is_empty(self):
        if self.data is None:
            return True
        else:
            return False

    def size(self):
        return self.len()
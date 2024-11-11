class Stack:
    def __init__(self, limit = 1000):
        self.data = []
        self.limit = limit

    def push(self, item):
        self.data.append(item)

    def pop(self):
        del_item = self.data[-1]
        self.data.pop()
        return del_item

    def top(self):
        return self.data[-1]

    def is_full(self):
        if len(self.data) < self.limit:
            return False
        else:
            return True

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.data)
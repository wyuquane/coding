from LinkedList import SinglyLinkedList


class StackLinkedList:
    def __init__(self):
        self.stack = SinglyLinkedList()
        self.length = 0

    def push(self, data):
        self.stack.add_head(data)
        self.length += 1

    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return
        popped_ele = self.stack.head.data
        self.stack.del_head()
        self.length -= 1
        return popped_ele

    def peek(self):
        if self.is_empty():
            print('stack is empty')
            return
        return self.stack.head.data

    def is_empty(self):
        return True if self.length == 0 else False

    def size(self):
        return self.length

    def __str__(self):
        if self.is_empty(): return 'stack is empty'
        result = 'top -> '
        cur = self.stack.head
        while cur:
            result += f'{cur.data}] '
            cur = cur.next
        return result

class StackList:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print('stack is empty')
            return
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def __str__(self):
        if self.is_empty(): return 'stack is empty'
        result = 'top -> '
        for ele in self.stack[::-1]:
            result += f'{ele}] '
        return result


if __name__ == '__main__':
    st = StackList()
    st.pop()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.peek())
    print(st.is_empty())
    print(st.size())
    print(st)
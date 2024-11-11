class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def del_begin(self):
        if self.head is None: return
        self.head = self.head.next

    def add_end(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, '-> ', end='')
            current = current.next
        print(None)

    def append_list(self, arr: list):
        for ele in arr[ : : -1]:
            self.add_begin(ele)



linked1 = SingleLinkedList()
linked1.append_list([1, 3, 4, 5, 7])
linked1.add_end(10)

linked2 = SingleLinkedList()
linked2.append_list([2, 3, 4, 6, 8, 9])
linked2.add_end(13)

linked1.display()
linked2.display()

cur1 = linked1.head
cur2 = linked2.head

# result = SingleLinkedList()
#
# while cur1 is not None or cur2 is not None:
#     if cur1 is None:
#         while cur2:
#             result.add_end(cur2.data)
#             cur2 = cur2.next
#         break
#     if cur2 is None:
#         while cur2:
#             result.add_end(cur1.data)
#             cur1 = cur1.next
#         break
#     if cur1.data < cur2.data:
#         result.add_end(cur1.data)
#         cur1 = cur1.next
#     else:
#         result.add_end(cur2.data)
#         cur2 = cur2.next

if cur1.data <= cur2.data: # lay cur1 lam chu, bien doi cur1
    # cur1 = cur1.next
    while cur1.next is not None or cur2 is not None:
        if cur2 is None:
            while cur1.next:
                cur1 = cur1.next
        if cur1.next is None:
            cur1.next = cur2
            break
        if cur1.next.data <= cur2.data:
            cur1 = cur1.next
        else:
            temp = cur2
            cur2 = cur2.next
            cur1.next = temp
            temp.next = cur1.next.next
            cur1 = cur1.next
        linked1.display()


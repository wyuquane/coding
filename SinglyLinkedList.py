class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

    def __str__(self):
        return f'{self.data} -> '


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_tail(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print(None)

    def count_prime(self):
        result = 0
        current = self.head
        while current:
            if checkprime(current.data):
                result += 1
            current = current.next
        return result

    def delete_second_node(self):
        current = self.head
        if current is None:
            return
        if current.next is None:
            return
        current.next = current.next.next

    def append_list(self, arr: list):
        for ele in arr[:: -1]:
            self.add_head(ele)

    def add_position(self, data, pos):
        pass

    def find_first_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return -1

    def check_balance(self):
        sum_llist = 0
        current = self.head
        while current:
            sum_llist += current.data
            current = current.next
        sum_first_k_node = 0
        count = 1
        current = self.head
        while current:
            sum_first_k_node += current.data
            if abs(sum_first_k_node - (sum_llist - sum_first_k_node)) < sum_llist / 2:
                return count
            count += 1
            current = current.next
        return -1

    def reverse_llist(self):
        '''reverse linked list without creat new one'''
        if self.head is None:
            return
        if self.head.next is None:
            return
        before = None
        cur = self.head
        after = self.head.next
        while after is not None:
            cur.next = before
            before = cur
            cur = after
            after = after.next
        cur.next = before
        self.head = cur
        return self

def merge_llist(llist1: SinglyLinkedList, llist2: SinglyLinkedList) -> SinglyLinkedList:
    cur1 = llist1.head
    cur2 = llist2.head
    result = SinglyLinkedList()
    while cur1 is not None or cur2 is not None:
        if cur1 is None:
            while cur2:
                result.add_tail(cur2.data)
                cur2 = cur2.next
            break
        if cur2 is None:
            while cur2:
                result.add_tail(cur1.data)
                cur1 = cur1.next
            break
        if cur1.data < cur2.data:
            result.add_tail(cur1.data)
            cur1 = cur1.next
        else:
            result.add_tail(cur2.data)
            cur2 = cur2.next
    return result


def checkprime(n: int):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    ll1 = SinglyLinkedList()
    ll2 = SinglyLinkedList()
    ll1.append_list([1, 3, 5, 7, 6, 8])
    ll2.append_list([2, 5, 6, 8, 9])
    a = ll2.head
    b = ll2.head
    while b.next is not None and b.next.next is not None:
        a = a.next
        b = b.next.next
    print(a.data)

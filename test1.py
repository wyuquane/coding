#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

def reverse(ll: SinglyLinkedList):
    result = SinglyLinkedList()
    cur = ll.head
    while cur:
        result.insert_node(cur.data)
        cur = cur.next
    return result

def ispalindrome(ll: SinglyLinkedList):
    if ll.head is None:
        return True
    if ll.head.next is None:
        return True
    reversed = reverse(ll)
    cur1 = ll.head
    cur2 = reversed.head
    while cur1:
        if cur1.data != cur2.data:
            return False
        cur1 = cur1.next
        cur2 = cur2.next
    return True




if __name__ == '__main__':

    nums = list(map(int, input().strip().split()))

    list = SinglyLinkedList()

    for num in nums:
        list.insert_node(num)

    print_singly_linked_list(reverse(list).head, sep=" ")
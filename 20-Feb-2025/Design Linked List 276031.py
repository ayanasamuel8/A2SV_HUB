# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        while index and current:
            current = current.next
            index -= 1
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        prev = None
        current = self.head
        while index and current:
            prev = current
            current = current.next
            index -= 1

        if index == 0:
            new_node = Node(val)
            prev.next = new_node
            new_node.next = current

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while index and current:
            prev = current
            current = current.next
            index -= 1

        if index == 0 and prev and current:
            prev.next = current.next

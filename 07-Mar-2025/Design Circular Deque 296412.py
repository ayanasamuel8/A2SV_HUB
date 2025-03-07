# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self,val = -1, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = k
        self.size = 0
    def insertFront(self, value: int) -> bool:
        if self.size >= self.capacity: return False
        new_node = Node(value,self.head.next, self.head)
        self.head.next.prev= new_node
        self.head.next  = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.capacity: return False
        new_node = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size <= 0: return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size <= 0: return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size <= 0: return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.size <= 0: return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.size <= 0 : return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity: return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
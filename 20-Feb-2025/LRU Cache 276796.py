# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, val=None):
        self.prev = None
        self.val = val
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.lru_cache = {}
        self.capacity = capacity
        self.running_capacity = 0

        self.head = Node()  
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_least_recently_used(self):
        lru_node = self.tail.prev
        del self.lru_cache[lru_node.val[1]] 
        self._remove_node(lru_node)

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            node = self.lru_cache[key]
            self._move_to_front(node) 
            return node.val[0]
        return -1

    def put(self, key: int, value: int):
        if key in self.lru_cache:
            node = self.lru_cache[key]
            node.val[0] = value
            self._move_to_front(node) 
        else:
            if self.running_capacity >= self.capacity:
                self._remove_least_recently_used()
                self.running_capacity -= 1

            new_node = Node([value, key])
            self.lru_cache[key] = new_node
            self._add_to_front(new_node)
            self.running_capacity += 1

# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.prio = random.randint(1, 1 << 30)
        self.left = None
        self.right = None
        self.size = 1

def size(node):
    return node.size if node else 0

def update(node):
    if node:
        node.size = 1 + size(node.left) + size(node.right)

def split(node, key):
    if not node:
        return (None, None)
    if key <= node.key:
        left, right = split(node.left, key)
        node.left = right
        update(node)
        return (left, node)
    else:
        left, right = split(node.right, key)
        node.right = left
        update(node)
        return (node, right)

def merge(left, right):
    if not left or not right:
        return left or right
    if left.prio > right.prio:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

class TreapSet:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if not node:
            return TreapNode(key)
        if key == node.key:
            return node  # already in set
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        update(node)
        return self._balance(node)

    def _balance(self, node):
        if node.left and node.left.prio > node.prio:
            node = self._rotate_right(node)
        elif node.right and node.right.prio > node.prio:
            node = self._rotate_left(node)
        return node

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        update(node)
        update(right)
        return right

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        update(node)
        update(left)
        return left

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _erase(self, node, key):
        if not node:
            return None
        if key == node.key:
            return merge(node.left, node.right)
        elif key < node.key:
            node.left = self._erase(node.left, key)
        else:
            node.right = self._erase(node.right, key)
        update(node)
        return node

    def erase(self, key):
        self.root = self._erase(self.root, key)

    def kth(self, k):
        return self._kth(self.root, k)

    def _kth(self, node, k):
        if not node:
            return None
        left_size = size(node.left)
        if k < left_size:
            return self._kth(node.left, k)
        elif k == left_size:
            return node.key
        else:
            return self._kth(node.right, k - left_size - 1)

    def size(self):
        return size(self.root)

    def find_missing(self):
        l, r = 0, self.size()
        while l < r:
            m = (l + r) // 2
            val = self.kth(m)
            if val == m + 1:
                l = m + 1
            else:
                r = m
        return l + 1


class SmallestInfiniteSet:

    def __init__(self):
        self.s = TreapSet()
        

    def popSmallest(self) -> int:
        smallest = self.s.find_missing()
        self.s.insert(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        self.s.erase(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

import sys,math
from collections import Counter, defaultdict
from functools import cmp_to_key

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]


class Node:
    def __init__(self, val = [0, 0], next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

def delete(node):

    if node.val[1] == node.prev.val[1]:
        if node.prev.val[0] < node.val[0]:
            node.prev.val[1] += node.val[1]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return prev_node 
        else:
            node.val[1] += node.prev.val[1]
            prev_node = node.prev.prev
            node.prev = prev_node
            prev_node.next = node
            return node
    else:
        if node.val[0] < node.next.val[0]:
            node.val[1] += node.next.val[1]
            next_node = node.next.next
            node.next = next_node
            next_node.prev = node 
            return node
        else:
            node.next.val[1] += node.val[1]
            prev_node = node.prev
            next = node.next
            prev_node.next = next
            next.prev = prev_node
            return next

def solve():
    n,k = INTS()
    array = LIST()
    ugliness = LIST()

    doubly = Node([1, k])
    doubly.next = doubly
    doubly.prev = doubly
    hashmap = {1: doubly}

    count = 2
    size = 1

    for i in range(n):
        node = hashmap[array[i]]
        new_node = Node([count, ugliness[i]])
        hashmap[count] = new_node

        next = node.next
        node.next = new_node
        new_node.prev= node
        new_node.next = next
        next.prev= new_node
        size += 1

        while new_node != new_node.prev and ((new_node.prev.val[1] == new_node.val[1]) or (new_node.val[1] == new_node.next.val[1])):
            new_node = delete(new_node)

            size -= 1
        count += 1
        output(f"{size} ")

def main():
    t = INT()
    for _ in range(t):
        solve()
        output('\n')

if __name__ == '__main__':
    main()

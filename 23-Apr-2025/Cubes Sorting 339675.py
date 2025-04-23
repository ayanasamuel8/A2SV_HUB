# Problem: Cubes Sorting - https://codeforces.com/gym/451300/problem/B

import sys, math, threading, heapq
from operator import itemgetter
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right

# ==================== FAST I/O ====================
input = sys.stdin.readline
output = sys.stdout.write

# ==================== QUICK INPUT ====================
INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
CHAR_LIST = lambda: list(input().strip())
LINE = lambda: input().strip()
MATRIX = lambda n: [LIST() for _ in range(n)]
CHAR_MATRIX = lambda n: [list(input().strip()) for _ in range(n)]
def yesNo(boolean): output("YES\n" if boolean else "NO\n")

# ==================== BINARY INDEXED TREE ====================
class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)
    
    def update(self, i, delta = 1):
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i
    
    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

# ==================== COORDINATE COMPRESSION ====================
def compress(arr):
    sorted_unique = sorted(set(arr))
    mapping = {val: idx for idx, val in enumerate(sorted_unique)}
    return [mapping[x] for x in arr], len(sorted_unique)

# ==================== SOLUTION ====================
def solve():
    n = INT()
    nums = LIST()
    max_swap = (n * (n - 1) // 2) - 1
    indexed, n = compress(nums)

    bit = BIT(n)
    total = 0

    for idx in indexed:
        bit.update(idx)
        total += bit.range_query(idx + 1, n - 1)

    yesNo(total <= max_swap)


# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()

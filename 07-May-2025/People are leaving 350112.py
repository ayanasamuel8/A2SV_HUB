# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

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

# ==================== CONSTANTS & UTILS ====================
MOD = 10**9 + 7
INF = float('inf')

def yesNo(boolean): output("YES\n" if boolean else "NO\n")

# ==================== SOLUTION ====================
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = size
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x):
        y = x + 1
        if y >= self.size:
            self.parent[x] = -1
            return
        self.parent[x] = self.find(y)
        

def solve():
    # n = INT()
    # nums = LIST()
    n, m = LIST()
    dsu = UnionFind(n)
    for _ in range(m):
        op, num = input().split()
        num = int(num) - 1
        if op == '-':
            dsu.union(num)
        else:
            ret = dsu.find(num)
            output(f"{ret + 1 if ret != -1 else -1}\n")

# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
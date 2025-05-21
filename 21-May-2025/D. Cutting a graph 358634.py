# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

#==================== BASIC IMPORTS ====================
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
LIST_LINE = lambda : input().split()

# ==================== CONSTANTS & UTILS ====================
MOD = 10**9 + 7
INF = float('inf')

def yesNo(boolean): return ("YES\n" if boolean else "NO\n")

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m

# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

#==================== UNION FIND ====================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

# ==================== SOLUTION ====================
def solve():
    n, m, k = LIST()
    # nums = LIST()
    edges = []
    for i in range(m):
        u,v = LIST()
        edges.append((u - 1, v - 1))
    instructions = []
    for i in range(k):
        op, u, v = LIST_LINE()
        u = int(u) - 1
        v = int(v) - 1
        instructions.append((op, u, v))
    instructions.reverse()
    dsu = UnionFind(n)
    ans = []
    for op, u, v in instructions:
        if op == 'ask':
            ans.append(yesNo(dsu.find(u) == dsu.find(v)))
        else:
            dsu.union(u,v)
    ans.reverse()
    output(f"{''.join(ans)}")

# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
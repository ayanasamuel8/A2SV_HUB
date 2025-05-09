# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

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

# ==================== CONSTANTS & UTILS ====================
MOD = 10**9 + 7
INF = float('inf')

def yesNo(boolean): output("YES\n" if boolean else "NO\n")

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m

# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

#==================== UNION FIND ====================
class UnionFind:
    def __init__(self, n, countries):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.countries = countries

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if xroot in self.countries:
            self.parent[yroot] = xroot
            rank = self.rank[yroot] - self.rank[xroot]
            self.rank[xroot] = self.rank[yroot] + 1 if rank <= 0 else self.rank[xroot]
            self.size[xroot] += self.size[yroot]
        elif yroot in self.countries:
            self.parent[xroot] = yroot
            rank = self.rank[xroot] - self.rank[yroot]
            self.rank[yroot] = self.rank[xroot] + 1 if rank <= 0 else self.rank[yroot]
            self.size[yroot] += self.size[xroot]
        else:
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
                self.size[yroot] += self.size[xroot] 
            else:
                self.parent[yroot] = xroot
                if self.rank[xroot] == self.rank[yroot]:
                    self.rank[xroot] += 1
                self.size[xroot] += self.size[yroot] 

# ==================== SOLUTION ====================
def solve():
    n, m, k = LIST()
    c = [i - 1 for i in LIST()]
    edges = []
    dsu = UnionFind(n, c)
    c = set(c)
    for i in range(m):
        u, v = LIST()
        u -= 1
        v -= 1
        edges.append((u,v))
        dsu.union(u,v)

    country_size = defaultdict(int)
    for i in range(n):
        root = dsu.find(i)
        if root in c:
            country_size[root] = dsu.size[root]
  
    country_size = sorted([val for val in country_size.values()])
    deleted = set()
    ret = 0
    
    for i in range(n):
        root = dsu.find(i)
        if root in c or root in deleted:
            continue
        size = dsu.size[root]
        country_size[-1] += size
        deleted.add(root)
    for i in country_size:
        ret += i * (i - 1) // 2
    output(f"{ret - m}")


# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
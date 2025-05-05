# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
        self.rank = [0] * size
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y:
            return True
        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_y] = r_x
            self.rank[r_x] += 1
        return False

def solve():
    n, m = LIST()
    edges = []
    for i in range(m):
        u, v, w = LIST()
        u -= 1
        v -= 1
        edges.append((w, u, v))
    
    edges.sort()
    dsu = UnionFind(n)
    total_weight = 0
    for w, u, v in edges:
        is_connected = dsu.union(u, v)
        if not is_connected:
            total_weight += w
    
    output(f"{total_weight}\n")

# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
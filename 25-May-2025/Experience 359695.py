# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.value = defaultdict(int)

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
            self.value[xroot] -= self.value[yroot]
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
            self.value[yroot] -= self.value[xroot]
    def add(self, x, val):
        xroot = self.find(x)
        self.value[xroot] += val
    def get(self, x):
        if self.parent[x] == x:
            # print('in: ',self.value[x])
            return self.value[x]
        # print('out: ', self.value[x], x, self.parent[x])
        return self.get(self.parent[x]) + self.value[x]

# ==================== SOLUTION ====================
def solve():
    # n = INT()
    # nums = LIST()
    n, m = LIST()
    dsu = UnionFind(n)
    for _ in range(m):
        op, *numbers = input().split() 
        if op == 'add':
            u,v = map(int, numbers)
            u -= 1
            dsu.add(u, v)
        elif op == 'join':
            u, v = map(int, numbers)
            u -= 1
            v -= 1
            dsu.union(u,v)
        else:
            v = int(numbers[0])
            v -= 1
            output(f"{dsu.get(v)}\n")


# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
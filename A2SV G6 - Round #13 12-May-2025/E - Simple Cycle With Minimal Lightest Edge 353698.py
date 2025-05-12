# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

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
        self.size = size
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
        self.size -= 1
        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_y] = r_x
            self.rank[r_x] += 1
        return False

found = False
ans = []
path = []

def dfs(v, p, MST, target):
    global found, ans, path
    path.append(v)
    if v == target:
        ans = path[:]
        found = True
        return
    for u in MST[v]:
        if u != p:
            dfs(u, v, MST, target)
            if found:
                return
    path.pop()

def solve():
    global found, ans, path
    n, m = LIST()
    edges = []
    for i in range(m):
        u, v, w = LIST()
        edges.append([w, u, v])
    
    edges.sort(reverse=True)
    
    dsu = UnionFind(n + 1)
    MST = defaultdict(list)
    
    ret = []
    for w, u, v in edges:
        is_connected = dsu.union(u, v)
        
        if not is_connected:
            MST[u].append(v)
            MST[v].append(u)
        else:
            ret = [u,v, w]
        
    found = False
    path = []
    dfs(ret[0], -1, MST, ret[1])

    print(ret[2], len(ans))
    print(*ans)

# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__': 
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
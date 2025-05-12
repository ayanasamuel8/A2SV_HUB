# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import sys, math, threading, heapq
from operator import itemgetter
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from types import GeneratorType

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

# ==================== SOLUTION ====================
def solve():
    n, m = LIST()
    string = LINE()

    graph = defaultdict(list)
    indeg = [0] * n
    indeg2 = [0] * n
    for i in range(m):
        u,v = LIST()
        u -= 1
        v -= 1
        graph[u].append(v)
        indeg[v] += 1
        indeg2[v] += 1
        
    sorted_graph = []
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    while q:
        u = q.popleft()
        sorted_graph.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(sorted_graph) < n:
        output(f"-1\n")
        return
    dp = [[1 if string[j] == chr(97 + i) else 0 for i in range(26)] for j in range(n)]
    
    q = deque()
    for i in range(n):
        if indeg2[i] == 0:
            q.append(i)
    while q:
        u = q.popleft()
    
        for v in graph[u]:
            indeg2[v] -= 1
            for i in range(26):
                dp[v][i] = max(dp[v][i], dp[u][i] + (1 if string[v] == chr(97 + i) else 0))
            if indeg2[v] == 0:
                q.append(v)
    _max = 1
    for i in range(n):
        for j in range(26):
            _max = max(_max, dp[i][j])
    output(f"{_max}\n")



# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()

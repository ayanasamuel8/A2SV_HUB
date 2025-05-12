# Problem: E - Direct Without Regret - https://codeforces.com/gym/606404/problem/E

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
from collections import defaultdict, deque

def solve():
    n, m = LIST()
    directed_graph = defaultdict(list)
    indegree = [0] * n
    undirected_edges = []

    for _ in range(m):
        t, u, v = LIST()
        u -= 1
        v -= 1
        if t == 1:
            directed_graph[u].append(v)
            indegree[v] += 1
        else:
            undirected_edges.append((u, v))

    queue = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in directed_graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo_order) != n:
        print("NO")
        return

    position = [0] * n
    for idx, node in enumerate(topo_order):
        position[node] = idx

    result_edges = []
    for u in range(n):
        for v in directed_graph[u]:
            result_edges.append((u + 1, v + 1))

    for u, v in undirected_edges:
        if position[u] < position[v]:
            result_edges.append((u + 1, v + 1))
        else:
            result_edges.append((v + 1, u + 1))

    print("YES")
    for u, v in result_edges:
        print(f"{u} {v}")


# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
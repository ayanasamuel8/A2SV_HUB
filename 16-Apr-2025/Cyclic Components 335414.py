# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import sys, math
from collections import Counter, defaultdict,deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def isCycle(nodes, indegree):
    for node in nodes:
        if indegree[node] != 2:
            return False
    return True

def bfs(node, adj, colors, color, visited):
    queue = deque([node])
    while queue:
        root = queue.popleft()
        colors[color].append(root)
        for nbr in adj[root]:
            if not visited[nbr]:
                visited[nbr] = True
                queue.append(nbr)

def solve():
    # n = INT()
    n, m = LIST()
    # nums = LIST()
    graph = defaultdict(list)
    indegree = [0] * n
    visited = [False] * n

    for _ in range(m):
        u, v = LIST()

        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        indegree[u - 1] += 1
        indegree[v - 1] += 1
    
    colors = defaultdict(list)
    start = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i, graph, colors, start, visited)
            start += 1
    
    count = 0
    for val in colors.values():
        count += isCycle(val, indegree)
    
    output(f"{count}")
    





    

def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()

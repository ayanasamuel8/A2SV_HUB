# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

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

def yesNo(boolean): output("YES\n" if boolean else "NO\n")

# ==================== SOLUTION ====================
def solve():
    n = INT()
    # nums = LIST()
    graph = defaultdict(list)
    for i in range(n - 1):
        u,v = LIST()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if type(to) is GeneratorType:
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        to = stack[-1].send(to)
                return to
        return wrappedfunc

    num_of_leaves = [0] * n
    visited = [False] * n
    @bootstrap
    def dfs(node):
        visited[node] = True
        if  len(graph[node]) == 1 and visited[graph[node][0]]:
            num_of_leaves[node] = 1
            yield 1
        for v in graph[node]:
            if not visited[v]:
                num_of_leaves[node] += yield dfs(v)
        yield num_of_leaves[node]
    
    dfs(0)

    q = INT()
    for i in range(q):
        first, second = LIST()
        first -= 1
        second -= 1
        output(f"{num_of_leaves[first] * num_of_leaves[second]}\n")


# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
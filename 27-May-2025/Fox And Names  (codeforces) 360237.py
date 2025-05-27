# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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
LINE_LIST = lambda n: [input().strip() for i in range(n)]
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

# ==================== SOLUTION ====================
def solve():
    n = INT()
    # nums = LIST()
    words = LINE_LIST(n)

    graph = defaultdict(list)
    indeg = [0] * 26
                
    
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                output('Impossible\n')
                return
            if words[i][j] != words[i + 1][j]:
                graph[ord(words[i][j]) - 97].append(ord(words[i + 1][j]) - 97)
                indeg[ord(words[i + 1][j]) - 97] += 1
                break
    q = deque()
    for key in range(26):
        if indeg[key] == 0:
            q.append(key)
    toposorted = []
    while q:
        front = q.popleft()
        toposorted.append(chr(front + 97))
        for v in graph[front]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(toposorted) != len(indeg):
        output('Impossible\n')
        return
    output(f"{''.join(toposorted)}\n")

# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
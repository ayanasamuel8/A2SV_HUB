# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

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

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m

# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

# ==================== SOLUTION ====================
def solve():
    n, m, k = LIST()
    # nums = LIST()
    _map = CHAR_MATRIX(n)

    lakes = []
    visited = [[False] * m for _ in range(n)]

    def bfs(row, col):
        lake  = deque([(row, col)])
        _lakes = [[row, col]]
        is_lake = True
        while lake:
            row, col = lake.popleft()
            if row == 0 or col == 0 or row == n - 1 or col == m - 1:
                is_lake = False
            for dr, dc in dirs_4:
                nrow, ncol = row + dr, col + dc
                if inBound(nrow, ncol, n, m) and _map[nrow][ncol] == '.' and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    _lakes.append([nrow, ncol])
                    lake.append((nrow, ncol))
        return is_lake, _lakes

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and _map[i][j] == '.':
                visited[i][j] = True
                is_lake, lake = bfs(i, j)
                if is_lake:
                    lakes.append(lake)
    
    lakes.sort(key=len)
    to_fill = len(lakes) - k
    filled = 0

    for i in range(to_fill):
        for row, col in lakes[i]:
            _map[row][col] = '*'
            filled += 1

    output(f"{str(filled)}\n")
    for i in _map:
        output(f"{''.join(i)}\n")
    





# ==================== MAIN ====================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
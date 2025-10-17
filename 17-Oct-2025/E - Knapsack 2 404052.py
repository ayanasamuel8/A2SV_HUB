# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

#==================== BASIC IMPORTS ====================
import sys, math, threading, heapq
from operator import itemgetter
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
#==================== FAST I/O =========================
input = sys.stdin.readline
output = sys.stdout.write
#==================== QUICK INPUT ======================
INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
CHAR_LIST = lambda: list(input().strip())
LINE = lambda: input().strip()
MATRIX = lambda n: [LIST() for _ in range(n)]
CHAR_MATRIX = lambda n: [list(input().strip()) for _ in range(n)]
#==================== CONSTANTS & UTILS ================
MOD = 10**9 + 7
INF = float('inf')
def yesNo(boolean): output("YES\n" if boolean else "NO\n")

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m
# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

#==================== SOLUTION =========================
def solve():
    # n = INT()
    # nums = LIST()
    n, w = LIST()
    items = []
    max_value = 0
    for _ in range(n):
        wi, vi = LIST()
        items.append([wi, vi])
        max_value += vi
    dp = [INF] * (max_value + 1)
    dp[0] = 0
    for wi, vi in items:
        for value in range(max_value, vi -1, -1):
            dp[value] = min(dp[value], dp[value - vi] + wi)
    
    for i in range(max_value, -1, -1):
        if dp[i] <= w:
            print(i)
            return


#==================== MAIN =============================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
  main()
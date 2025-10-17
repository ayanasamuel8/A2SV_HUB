# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

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
    n = INT()
    # nums = LIST()
    dp = [[0, 0, 0], LIST()]
    for _ in range(n - 1):
        a,b,c = LIST()
        dp.append([a + max(dp[-1][1:]), b + max(dp[-1][0], dp[-1][2]), c + max(dp[-1][:-1])])
    
    print(max(dp[-1]))


#==================== MAIN =============================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
  main()
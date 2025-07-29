# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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
def trail_division(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors
def solve():
    n = INT()
    cnt = 0
    for i in range(6, n + 1):
        factors = trail_division(i)
        if len(factors) == 2:
            cnt += 1
    output(f"{cnt}")


#==================== MAIN =============================
def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
  main()
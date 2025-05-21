# Problem: Creating Keys for StORages Has Become My Main Skill - https://codeforces.com/contest/2072/problem/C

#==================== BASIC IMPORTS ====================
import sys, math, threading, heapq
from operator import itemgetter
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import cmp_to_key, reduce
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

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m

# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

# ==================== SOLUTION ====================
def solve():
    n, x = LIST()
    if n == 1:
        output(f'{x}\n')
        return
    ans = []
    i = 0
    while True and len(ans) < n:
        if i & x == i:
            ans.append(i)
        else:
            break
        i += 1
    
    red = reduce(lambda a,b:a|b, ans)
    if red == x and len(ans) == n:
        output(f"{' '.join(map(str, ans))}\n")
        return
    if len(ans) == n:
        ans.pop()
    while len(ans) < n:
        ans.append(x)
    output(f"{' '.join(map(str,ans))}\n")


# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
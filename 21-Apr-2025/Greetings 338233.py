# Problem: Greetings - https://codeforces.com/contest/1915/problem/F

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

def inBound(x, y, n, m): return 0 <= x < n and 0 <= y < m

# directions for grids
dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dirs_8 = [(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

# ==================== INVERSION COUNT ====================
def count_inversions(arr):
    sorted_arr = sorted(set(arr))
    ranks = {v: i+1 for i, v in enumerate(sorted_arr)} 
    bit = [0] * (len(sorted_arr) + 2)
    
    def update(idx):
        while idx < len(bit):
            bit[idx] += 1
            idx += idx & -idx

    def query(idx):
        res = 0
        while idx > 0:
            res += bit[idx]
            idx -= idx & -idx
        return res

    inversions = 0
    for x in reversed(arr):
        rank = ranks[x]
        inversions += query(rank - 1)
        update(rank)
    return inversions

# ==================== SOLUTION ====================
def solve():
    n = INT()
    people = []
    for _ in range(n):
        a, b = LIST()
        people.append((a, b))
    people.sort()
    b_list = [b for a, b in people]
    result = count_inversions(b_list)
    output(str(result) + '\n')


# ==================== MAIN ====================
def main():
    T = 1
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()

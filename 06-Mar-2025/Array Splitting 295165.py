# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys, math
from collections import Counter, defaultdict,deque
from functools import cmp_to_key

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n, k = INTS()
    array = LIST()
    difference = [0] * n
    for i in range(n - 1):
        difference[i] = abs(array[i + 1] - array[i])
    difference.sort()
    difference = difference[:n - k + 1]
    output(f"{sum(difference)}")

def main():
    solve()

if __name__ == '__main__':
    main()
